# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class JobScheduleExecutionInformation(Model):
    """Contains information about jobs that have been and will be run under a job
    schedule.

    :param next_run_time: The next time at which a job will be created under
     this schedule. This property is meaningful only if the schedule is in the
     active state when the time comes around. For example, if the schedule is
     disabled, no job will be created at nextRunTime unless the job is enabled
     before then.
    :type next_run_time: datetime
    :param recent_job: Information about the most recent job under the job
     schedule. This property is present only if the at least one job has run
     under the schedule.
    :type recent_job: :class:`RecentJob <azure.batch.models.RecentJob>`
    :param end_time: The time at which the schedule ended. This property is
     set only if the job schedule is in the completed state.
    :type end_time: datetime
    """ 

    _attribute_map = {
        'next_run_time': {'key': 'nextRunTime', 'type': 'iso-8601'},
        'recent_job': {'key': 'recentJob', 'type': 'RecentJob'},
        'end_time': {'key': 'endTime', 'type': 'iso-8601'},
    }

    def __init__(self, next_run_time=None, recent_job=None, end_time=None):
        self.next_run_time = next_run_time
        self.recent_job = recent_job
        self.end_time = end_time
