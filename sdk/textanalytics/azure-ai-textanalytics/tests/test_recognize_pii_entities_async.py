# coding=utf-8
# ------------------------------------
# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
# ------------------------------------

import pytest
import platform

from azure.core.exceptions import HttpResponseError, ClientAuthenticationError
from azure.core.pipeline.transport import AioHttpTransport
from multidict import CIMultiDict, CIMultiDictProxy
from azure.ai.textanalytics.aio import TextAnalyticsClient
from azure.ai.textanalytics import (
    VERSION,
    DetectLanguageInput,
    TextDocumentInput,
    TextAnalyticsApiKeyCredential
)

from testcase import GlobalTextAnalyticsAccountPreparer
from asynctestcase import AsyncTextAnalyticsTest

class AiohttpTestTransport(AioHttpTransport):
    """Workaround to vcrpy bug: https://github.com/kevin1024/vcrpy/pull/461
    """
    async def send(self, request, **config):
        response = await super(AiohttpTestTransport, self).send(request, **config)
        if not isinstance(response.headers, CIMultiDictProxy):
            response.headers = CIMultiDictProxy(CIMultiDict(response.internal_response.headers))
            response.content_type = response.headers.get("content-type")
        return response


class TestRecognizePIIEntities(AsyncTextAnalyticsTest):

    @GlobalTextAnalyticsAccountPreparer()
    @AsyncTextAnalyticsTest.await_prepared_test
    async def test_no_single_input(self, resource_group, location, text_analytics_account, text_analytics_account_key):
        text_analytics = TextAnalyticsClient(text_analytics_account, TextAnalyticsApiKeyCredential(text_analytics_account_key))
        with self.assertRaises(TypeError):
            response = await text_analytics.recognize_pii_entities("hello world")

    @GlobalTextAnalyticsAccountPreparer()
    @AsyncTextAnalyticsTest.await_prepared_test
    async def test_all_successful_passing_dict(self, resource_group, location, text_analytics_account, text_analytics_account_key):
        text_analytics = TextAnalyticsClient(text_analytics_account, TextAnalyticsApiKeyCredential(text_analytics_account_key))

        docs = [{"id": "1", "text": "My SSN is 555-55-5555."},
                {"id": "2", "text": "Your ABA number - 111000025 - is the first 9 digits in the lower left hand corner of your personal check."},
                {"id": "3", "text": "Is 998.214.865-68 your Brazilian CPF number?"}]

        response = await text_analytics.recognize_pii_entities(docs, show_stats=True)
        self.assertEqual(response[0].entities[0].text, "555-55-5555")
        self.assertEqual(response[0].entities[0].category, "U.S. Social Security Number (SSN)")
        self.assertEqual(response[1].entities[0].text, "111000025")
        # self.assertEqual(response[1].entities[0].category, "ABA Routing Number")  # Service is currently returning PhoneNumber here
        self.assertEqual(response[2].entities[0].text, "998.214.865-68")
        self.assertEqual(response[2].entities[0].category, "Brazil CPF Number")
        for doc in response:
            self.assertIsNotNone(doc.id)
            self.assertIsNotNone(doc.statistics)
            for entity in doc.entities:
                self.assertIsNotNone(entity.text)
                self.assertIsNotNone(entity.category)
                self.assertIsNotNone(entity.grapheme_offset)
                self.assertIsNotNone(entity.grapheme_length)
                self.assertIsNotNone(entity.score)

    @GlobalTextAnalyticsAccountPreparer()
    @AsyncTextAnalyticsTest.await_prepared_test
    async def test_all_successful_passing_text_document_input(self, resource_group, location, text_analytics_account, text_analytics_account_key):
        text_analytics = TextAnalyticsClient(text_analytics_account, TextAnalyticsApiKeyCredential(text_analytics_account_key))

        docs = [
            TextDocumentInput(id="1", text="My SSN is 555-55-5555."),
            TextDocumentInput(id="2", text="Your ABA number - 111000025 - is the first 9 digits in the lower left hand corner of your personal check."),
            TextDocumentInput(id="3", text="Is 998.214.865-68 your Brazilian CPF number?")
        ]

        response = await text_analytics.recognize_pii_entities(docs, show_stats=True)
        self.assertEqual(response[0].entities[0].text, "555-55-5555")
        self.assertEqual(response[0].entities[0].category, "U.S. Social Security Number (SSN)")
        self.assertEqual(response[1].entities[0].text, "111000025")
        # self.assertEqual(response[1].entities[0].category, "ABA Routing Number")  # Service is currently returning PhoneNumber here
        self.assertEqual(response[2].entities[0].text, "998.214.865-68")
        self.assertEqual(response[2].entities[0].category, "Brazil CPF Number")
        for doc in response:
            self.assertIsNotNone(doc.id)
            self.assertIsNotNone(doc.statistics)
            for entity in doc.entities:
                self.assertIsNotNone(entity.text)
                self.assertIsNotNone(entity.category)
                self.assertIsNotNone(entity.grapheme_offset)
                self.assertIsNotNone(entity.grapheme_length)
                self.assertIsNotNone(entity.score)

    @GlobalTextAnalyticsAccountPreparer()
    @AsyncTextAnalyticsTest.await_prepared_test
    async def test_length_with_emoji(self, resource_group, location, text_analytics_account, text_analytics_account_key):
        text_analytics = TextAnalyticsClient(text_analytics_account, TextAnalyticsApiKeyCredential(text_analytics_account_key))

        result = await text_analytics.recognize_pii_entities(["👩 SSN: 123-12-1234"])
        self.assertEqual(result[0].entities[0].grapheme_offset, 7)
        self.assertEqual(result[0].entities[0].grapheme_length, 11)

    @GlobalTextAnalyticsAccountPreparer()
    @AsyncTextAnalyticsTest.await_prepared_test
    async def test_passing_only_string(self, resource_group, location, text_analytics_account, text_analytics_account_key):
        text_analytics = TextAnalyticsClient(text_analytics_account, TextAnalyticsApiKeyCredential(text_analytics_account_key))

        docs = [
            u"My SSN is 555-55-5555.",
            u"Your ABA number - 111000025 - is the first 9 digits in the lower left hand corner of your personal check.",
            u"Is 998.214.865-68 your Brazilian CPF number?",
            u""
        ]

        response = await text_analytics.recognize_pii_entities(docs, show_stats=True)
        self.assertEqual(response[0].entities[0].text, "555-55-5555")
        self.assertEqual(response[0].entities[0].category, "U.S. Social Security Number (SSN)")
        self.assertEqual(response[1].entities[0].text, "111000025")
        # self.assertEqual(response[1].entities[0].category, "ABA Routing Number")  # Service is currently returning PhoneNumber here
        self.assertEqual(response[2].entities[0].text, "998.214.865-68")
        self.assertEqual(response[2].entities[0].category, "Brazil CPF Number")
        self.assertTrue(response[3].is_error)

    @GlobalTextAnalyticsAccountPreparer()
    @AsyncTextAnalyticsTest.await_prepared_test
    async def test_input_with_some_errors(self, resource_group, location, text_analytics_account, text_analytics_account_key):
        text_analytics = TextAnalyticsClient(text_analytics_account, TextAnalyticsApiKeyCredential(text_analytics_account_key))

        docs = [{"id": "1", "language": "es", "text": "hola"},
                {"id": "2", "text": ""},
                {"id": "3", "text": "Is 998.214.865-68 your Brazilian CPF number?"}]

        response = await text_analytics.recognize_pii_entities(docs)
        self.assertTrue(response[0].is_error)
        self.assertTrue(response[1].is_error)
        self.assertFalse(response[2].is_error)

    @GlobalTextAnalyticsAccountPreparer()
    @AsyncTextAnalyticsTest.await_prepared_test
    async def test_input_with_all_errors(self, resource_group, location, text_analytics_account, text_analytics_account_key):
        text_analytics = TextAnalyticsClient(text_analytics_account, TextAnalyticsApiKeyCredential(text_analytics_account_key))

        docs = [{"id": "1", "language": "es", "text": "hola"},
                {"id": "2", "text": ""}]

        response = await text_analytics.recognize_pii_entities(docs)
        self.assertTrue(response[0].is_error)
        self.assertTrue(response[1].is_error)

    @GlobalTextAnalyticsAccountPreparer()
    @AsyncTextAnalyticsTest.await_prepared_test
    async def test_empty_credential_class(self, resource_group, location, text_analytics_account, text_analytics_account_key):
        text_analytics = TextAnalyticsClient(text_analytics_account, TextAnalyticsApiKeyCredential(""))
        with self.assertRaises(ClientAuthenticationError):
            response = await text_analytics.recognize_pii_entities(
                ["This is written in English."]
            )

    @GlobalTextAnalyticsAccountPreparer()
    @AsyncTextAnalyticsTest.await_prepared_test
    async def test_bad_credentials(self, resource_group, location, text_analytics_account, text_analytics_account_key):
        text_analytics = TextAnalyticsClient(text_analytics_account, TextAnalyticsApiKeyCredential("xxxxxxxxxxxx"))
        with self.assertRaises(ClientAuthenticationError):
            response = await text_analytics.recognize_pii_entities(
                ["This is written in English."]
            )

    @GlobalTextAnalyticsAccountPreparer()
    @AsyncTextAnalyticsTest.await_prepared_test
    async def test_bad_model_version(self, resource_group, location, text_analytics_account, text_analytics_account_key):
        text_analytics = TextAnalyticsClient(text_analytics_account, TextAnalyticsApiKeyCredential(text_analytics_account_key))
        with self.assertRaises(HttpResponseError):
            response = await text_analytics.recognize_pii_entities(
                inputs=["Microsoft was founded by Bill Gates."],
                model_version="old"
            )

    @GlobalTextAnalyticsAccountPreparer()
    @AsyncTextAnalyticsTest.await_prepared_test
    async def test_bad_document_input(self, resource_group, location, text_analytics_account, text_analytics_account_key):
        text_analytics = TextAnalyticsClient(text_analytics_account, TextAnalyticsApiKeyCredential(text_analytics_account_key))

        docs = "This is the wrong type"

        with self.assertRaises(TypeError):
            response = await text_analytics.recognize_pii_entities(docs)

    @GlobalTextAnalyticsAccountPreparer()
    @AsyncTextAnalyticsTest.await_prepared_test
    async def test_mixing_inputs(self, resource_group, location, text_analytics_account, text_analytics_account_key):
        text_analytics = TextAnalyticsClient(text_analytics_account, TextAnalyticsApiKeyCredential(text_analytics_account_key))
        docs = [
            {"id": "1", "text": "Microsoft was founded by Bill Gates and Paul Allen."},
            TextDocumentInput(id="2", text="I did not like the hotel we stayed at. It was too expensive."),
            u"You cannot mix string input with the above inputs"
        ]
        with self.assertRaises(TypeError):
            response = await text_analytics.recognize_pii_entities(docs)

    @GlobalTextAnalyticsAccountPreparer()
    @AsyncTextAnalyticsTest.await_prepared_test
    async def test_out_of_order_ids(self, resource_group, location, text_analytics_account, text_analytics_account_key):
        text_analytics = TextAnalyticsClient(text_analytics_account, TextAnalyticsApiKeyCredential(text_analytics_account_key))

        docs = [{"id": "56", "text": ":)"},
                {"id": "0", "text": ":("},
                {"id": "22", "text": ""},
                {"id": "19", "text": ":P"},
                {"id": "1", "text": ":D"}]

        response = await text_analytics.recognize_pii_entities(docs)
        in_order = ["56", "0", "22", "19", "1"]
        for idx, resp in enumerate(response):
            self.assertEqual(resp.id, in_order[idx])

    @GlobalTextAnalyticsAccountPreparer()
    @AsyncTextAnalyticsTest.await_prepared_test
    async def test_show_stats_and_model_version(self, resource_group, location, text_analytics_account, text_analytics_account_key):
        text_analytics = TextAnalyticsClient(text_analytics_account, TextAnalyticsApiKeyCredential(text_analytics_account_key))

        def callback(response):
            self.assertIsNotNone(response.model_version)
            self.assertIsNotNone(response.raw_response)
            self.assertEqual(response.statistics.document_count, 5)
            self.assertEqual(response.statistics.transaction_count, 4)
            self.assertEqual(response.statistics.valid_document_count, 4)
            self.assertEqual(response.statistics.erroneous_document_count, 1)

        docs = [{"id": "56", "text": ":)"},
                {"id": "0", "text": ":("},
                {"id": "22", "text": ""},
                {"id": "19", "text": ":P"},
                {"id": "1", "text": ":D"}]

        response = await text_analytics.recognize_pii_entities(
            docs,
            show_stats=True,
            model_version="latest",
            raw_response_hook=callback
        )

    @GlobalTextAnalyticsAccountPreparer()
    @AsyncTextAnalyticsTest.await_prepared_test
    async def test_batch_size_over_limit(self, resource_group, location, text_analytics_account, text_analytics_account_key):
        text_analytics = TextAnalyticsClient(text_analytics_account, TextAnalyticsApiKeyCredential(text_analytics_account_key))

        docs = [u"hello world"] * 1050
        with self.assertRaises(HttpResponseError):
            response = await text_analytics.recognize_pii_entities(docs)

    @GlobalTextAnalyticsAccountPreparer()
    @AsyncTextAnalyticsTest.await_prepared_test
    async def test_whole_batch_language_hint(self, resource_group, location, text_analytics_account, text_analytics_account_key):
        text_analytics = TextAnalyticsClient(text_analytics_account, TextAnalyticsApiKeyCredential(text_analytics_account_key))

        def callback(resp):
            language_str = "\"language\": \"fr\""
            language = resp.http_request.body.count(language_str)
            self.assertEqual(language, 3)

        docs = [
            u"This was the best day of my life.",
            u"I did not like the hotel we stayed at. It was too expensive.",
            u"The restaurant was not as good as I hoped."
        ]

        response = await text_analytics.recognize_pii_entities(docs, language="fr", raw_response_hook=callback)

    @GlobalTextAnalyticsAccountPreparer()
    @AsyncTextAnalyticsTest.await_prepared_test
    async def test_whole_batch_dont_use_language_hint(self, resource_group, location, text_analytics_account, text_analytics_account_key):
        text_analytics = TextAnalyticsClient(text_analytics_account, TextAnalyticsApiKeyCredential(text_analytics_account_key))

        def callback(resp):
            language_str = "\"language\": \"\""
            language = resp.http_request.body.count(language_str)
            self.assertEqual(language, 3)

        docs = [
            u"This was the best day of my life.",
            u"I did not like the hotel we stayed at. It was too expensive.",
            u"The restaurant was not as good as I hoped."
        ]

        response = await text_analytics.recognize_pii_entities(docs, language="", raw_response_hook=callback)

    @GlobalTextAnalyticsAccountPreparer()
    @AsyncTextAnalyticsTest.await_prepared_test
    async def test_per_item_dont_use_language_hint(self, resource_group, location, text_analytics_account, text_analytics_account_key):
        text_analytics = TextAnalyticsClient(text_analytics_account, TextAnalyticsApiKeyCredential(text_analytics_account_key))

        def callback(resp):
            language_str = "\"language\": \"\""
            language = resp.http_request.body.count(language_str)
            self.assertEqual(language, 2)
            language_str = "\"language\": \"en\""
            language = resp.http_request.body.count(language_str)
            self.assertEqual(language, 1)


        docs = [{"id": "1", "language": "", "text": "I will go to the park."},
                {"id": "2", "language": "", "text": "I did not like the hotel we stayed at."},
                {"id": "3", "text": "The restaurant had really good food."}]

        response = await text_analytics.recognize_pii_entities(docs, raw_response_hook=callback)

    @GlobalTextAnalyticsAccountPreparer()
    @AsyncTextAnalyticsTest.await_prepared_test
    async def test_whole_batch_language_hint_and_obj_input(self, resource_group, location, text_analytics_account, text_analytics_account_key):
        text_analytics = TextAnalyticsClient(text_analytics_account, TextAnalyticsApiKeyCredential(text_analytics_account_key))

        def callback(resp):
            language_str = "\"language\": \"de\""
            language = resp.http_request.body.count(language_str)
            self.assertEqual(language, 3)

        docs = [
            TextDocumentInput(id="1", text="I should take my cat to the veterinarian."),
            TextDocumentInput(id="4", text="Este es un document escrito en Español."),
            TextDocumentInput(id="3", text="猫は幸せ"),
        ]

        response = await text_analytics.recognize_pii_entities(docs, language="de", raw_response_hook=callback)

    @GlobalTextAnalyticsAccountPreparer()
    @AsyncTextAnalyticsTest.await_prepared_test
    async def test_whole_batch_language_hint_and_obj_per_item_hints(self, resource_group, location, text_analytics_account, text_analytics_account_key):
        text_analytics = TextAnalyticsClient(text_analytics_account, TextAnalyticsApiKeyCredential(text_analytics_account_key))

        def callback(resp):
            language_str = "\"language\": \"es\""
            language = resp.http_request.body.count(language_str)
            self.assertEqual(language, 2)
            language_str = "\"language\": \"en\""
            language = resp.http_request.body.count(language_str)
            self.assertEqual(language, 1)

        docs = [
            TextDocumentInput(id="1", text="I should take my cat to the veterinarian.", language="es"),
            TextDocumentInput(id="2", text="Este es un document escrito en Español.", language="es"),
            TextDocumentInput(id="3", text="猫は幸せ"),
        ]

        response = await text_analytics.recognize_pii_entities(docs, language="en", raw_response_hook=callback)

    @GlobalTextAnalyticsAccountPreparer()
    @AsyncTextAnalyticsTest.await_prepared_test
    async def test_whole_batch_language_hint_and_dict_per_item_hints(self, resource_group, location, text_analytics_account, text_analytics_account_key):
        text_analytics = TextAnalyticsClient(text_analytics_account, TextAnalyticsApiKeyCredential(text_analytics_account_key))

        def callback(resp):
            language_str = "\"language\": \"es\""
            language = resp.http_request.body.count(language_str)
            self.assertEqual(language, 2)
            language_str = "\"language\": \"en\""
            language = resp.http_request.body.count(language_str)
            self.assertEqual(language, 1)


        docs = [{"id": "1", "language": "es", "text": "I will go to the park."},
                {"id": "2", "language": "es", "text": "I did not like the hotel we stayed at."},
                {"id": "3", "text": "The restaurant had really good food."}]

        response = await text_analytics.recognize_pii_entities(docs, language="en", raw_response_hook=callback)

    @GlobalTextAnalyticsAccountPreparer()
    @AsyncTextAnalyticsTest.await_prepared_test
    async def test_client_passed_default_language_hint(self, resource_group, location, text_analytics_account, text_analytics_account_key):
        text_analytics = TextAnalyticsClient(text_analytics_account, TextAnalyticsApiKeyCredential(text_analytics_account_key), default_language="es")

        def callback(resp):
            language_str = "\"language\": \"es\""
            language = resp.http_request.body.count(language_str)
            self.assertEqual(language, 3)

        def callback_2(resp):
            language_str = "\"language\": \"en\""
            language = resp.http_request.body.count(language_str)
            self.assertEqual(language, 3)

        docs = [{"id": "1", "text": "I will go to the park."},
                {"id": "2", "text": "I did not like the hotel we stayed at."},
                {"id": "3", "text": "The restaurant had really good food."}]

        response = await text_analytics.recognize_pii_entities(docs, raw_response_hook=callback)
        response = await text_analytics.recognize_pii_entities(docs, language="en", raw_response_hook=callback_2)
        response = await text_analytics.recognize_pii_entities(docs, raw_response_hook=callback)

    @GlobalTextAnalyticsAccountPreparer()
    @AsyncTextAnalyticsTest.await_prepared_test
    async def test_rotate_subscription_key(self, resource_group, location, text_analytics_account, text_analytics_account_key):
        credential = TextAnalyticsApiKeyCredential(text_analytics_account_key)
        text_analytics = TextAnalyticsClient(text_analytics_account, credential)

        docs = [{"id": "1", "text": "I will go to the park."},
                {"id": "2", "text": "I did not like the hotel we stayed at."},
                {"id": "3", "text": "The restaurant had really good food."}]

        response = await text_analytics.recognize_pii_entities(docs)
        self.assertIsNotNone(response)

        credential.update_key("xxx")  # Make authentication fail
        with self.assertRaises(ClientAuthenticationError):
            response = await text_analytics.recognize_pii_entities(docs)

        credential.update_key(text_analytics_account_key)  # Authenticate successfully again
        response = await text_analytics.recognize_pii_entities(docs)
        self.assertIsNotNone(response)

    @GlobalTextAnalyticsAccountPreparer()
    @AsyncTextAnalyticsTest.await_prepared_test
    async def test_user_agent(self, resource_group, location, text_analytics_account, text_analytics_account_key):
        text_analytics = TextAnalyticsClient(text_analytics_account, TextAnalyticsApiKeyCredential(text_analytics_account_key))

        def callback(resp):
            self.assertIn("azsdk-python-azure-ai-textanalytics/{} Python/{} ({})".format(
                VERSION, platform.python_version(), platform.platform()),
                resp.http_request.headers["User-Agent"]
            )

        docs = [{"id": "1", "text": "I will go to the park."},
                {"id": "2", "text": "I did not like the hotel we stayed at."},
                {"id": "3", "text": "The restaurant had really good food."}]

        response = await text_analytics.recognize_pii_entities(docs, raw_response_hook=callback)

    @GlobalTextAnalyticsAccountPreparer()
    @AsyncTextAnalyticsTest.await_prepared_test
    async def test_document_attribute_error_no_result_attribute(self, resource_group, location, text_analytics_account, text_analytics_account_key):
        text_analytics = TextAnalyticsClient(text_analytics_account, TextAnalyticsApiKeyCredential(text_analytics_account_key))

        docs = [{"id": "1", "text": ""}]
        response = await text_analytics.recognize_pii_entities(docs)

        # Attributes on DocumentError
        self.assertTrue(response[0].is_error)
        self.assertEqual(response[0].id, "1")
        self.assertIsNotNone(response[0].error)

        # Result attribute not on DocumentError, custom error message
        try:
            entities = response[0].entities
        except AttributeError as custom_error:
            self.assertEqual(
                custom_error.args[0],
                '\'DocumentError\' object has no attribute \'entities\'. '
                'The service was unable to process this document:\nDocument Id: 1\nError: '
                'invalidDocument - Document text is empty.\n'
            )

    @GlobalTextAnalyticsAccountPreparer()
    @AsyncTextAnalyticsTest.await_prepared_test
    async def test_document_attribute_error_nonexistent_attribute(self, resource_group, location, text_analytics_account, text_analytics_account_key):
        text_analytics = TextAnalyticsClient(text_analytics_account, TextAnalyticsApiKeyCredential(text_analytics_account_key))

        docs = [{"id": "1", "text": ""}]
        response = await text_analytics.recognize_pii_entities(docs)

        # Attribute not found on DocumentError or result obj, default behavior/message
        try:
            entities = response[0].attribute_not_on_result_or_error
        except AttributeError as default_behavior:
            self.assertEqual(
                default_behavior.args[0],
                '\'DocumentError\' object has no attribute \'attribute_not_on_result_or_error\''
            )

    @GlobalTextAnalyticsAccountPreparer()
    @AsyncTextAnalyticsTest.await_prepared_test
    async def test_bad_model_version_error(self, resource_group, location, text_analytics_account, text_analytics_account_key):
        text_analytics = TextAnalyticsClient(text_analytics_account, TextAnalyticsApiKeyCredential(text_analytics_account_key))
        docs = [{"id": "1", "language": "english", "text": "I did not like the hotel we stayed at."}]

        try:
            result = await text_analytics.recognize_pii_entities(docs, model_version="bad")
        except HttpResponseError as err:
            self.assertEqual(err.error_code, "InvalidRequest")
            self.assertIsNotNone(err.message)

    @GlobalTextAnalyticsAccountPreparer()
    @AsyncTextAnalyticsTest.await_prepared_test
    async def test_document_errors(self, resource_group, location, text_analytics_account, text_analytics_account_key):
        text_analytics = TextAnalyticsClient(text_analytics_account, TextAnalyticsApiKeyCredential(text_analytics_account_key))
        text = ""
        for _ in range(5121):
            text += "x"

        docs = [{"id": "1", "text": ""},
                {"id": "2", "language": "english", "text": "I did not like the hotel we stayed at."},
                {"id": "3", "text": text}]

        doc_errors = await text_analytics.recognize_pii_entities(docs)
        self.assertEqual(doc_errors[0].error.code, "invalidDocument")
        self.assertIsNotNone(doc_errors[0].error.message)
        self.assertEqual(doc_errors[1].error.code, "unsupportedLanguageCode")
        self.assertIsNotNone(doc_errors[1].error.message)
        self.assertEqual(doc_errors[2].error.code, "invalidDocument")
        self.assertIsNotNone(doc_errors[2].error.message)

    @GlobalTextAnalyticsAccountPreparer()
    @AsyncTextAnalyticsTest.await_prepared_test
    async def test_missing_input_records_error(self, resource_group, location, text_analytics_account, text_analytics_account_key):
        text_analytics = TextAnalyticsClient(text_analytics_account, TextAnalyticsApiKeyCredential(text_analytics_account_key))
        docs = []
        try:
            result = await text_analytics.recognize_pii_entities(docs)
        except HttpResponseError as err:
            self.assertEqual(err.error_code, "MissingInputRecords")
            self.assertIsNotNone(err.message)

    @GlobalTextAnalyticsAccountPreparer()
    @AsyncTextAnalyticsTest.await_prepared_test
    async def test_duplicate_ids_error(self, resource_group, location, text_analytics_account, text_analytics_account_key):
        text_analytics = TextAnalyticsClient(text_analytics_account, TextAnalyticsApiKeyCredential(text_analytics_account_key))
        # Duplicate Ids
        docs = [{"id": "1", "text": "hello world"},
                {"id": "1", "text": "I did not like the hotel we stayed at."}]
        try:
            result = await text_analytics.recognize_pii_entities(docs)
        except HttpResponseError as err:
            self.assertEqual(err.error_code, "InvalidDocument")
            self.assertIsNotNone(err.message)

    @GlobalTextAnalyticsAccountPreparer()
    @AsyncTextAnalyticsTest.await_prepared_test
    async def test_batch_size_over_limit_error(self, resource_group, location, text_analytics_account, text_analytics_account_key):
        text_analytics = TextAnalyticsClient(text_analytics_account, TextAnalyticsApiKeyCredential(text_analytics_account_key))
        # Batch size over limit
        docs = [u"hello world"] * 1001
        try:
            response = await text_analytics.recognize_pii_entities(docs)
        except HttpResponseError as err:
            self.assertEqual(err.error_code, "InvalidDocumentBatch")
            self.assertIsNotNone(err.message)

    @GlobalTextAnalyticsAccountPreparer()
    @AsyncTextAnalyticsTest.await_prepared_test
    async def test_language_kwarg_english(self, resource_group, location, text_analytics_account, text_analytics_account_key):
        text_analytics = TextAnalyticsClient(text_analytics_account, TextAnalyticsApiKeyCredential(text_analytics_account_key))

        def callback(response):
            language_str = "\"language\": \"en\""
            self.assertEqual(response.http_request.body.count(language_str), 1)
            self.assertIsNotNone(response.model_version)
            self.assertIsNotNone(response.statistics)

        res = await text_analytics.recognize_pii_entities(
            inputs=["Bill Gates is the CEO of Microsoft."],
            model_version="latest",
            show_stats=True,
            language="en",
            raw_response_hook=callback
        )
