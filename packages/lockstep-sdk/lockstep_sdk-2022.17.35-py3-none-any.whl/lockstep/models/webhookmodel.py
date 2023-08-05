#
# Lockstep Platform SDK for Python
#
# (c) 2021-2022 Lockstep, Inc.
#
# For the full copyright and license information, please view the LICENSE
# file that was distributed with this source code.
#
# @author     Lockstep Network <support@lockstep.io>
# @copyright  2021-2022 Lockstep, Inc.
# @link       https://github.com/Lockstep-Network/lockstep-sdk-python
#


from dataclasses import dataclass

@dataclass
class WebhookModel:
    """
    A Webhook is a subscription to receive notifications automatically
    to the supplied callback url when changes are made to a supported
    object. Currently supported objects: * `SyncRequest` - Receive a
    notification when a new sync request has completed for the group
    key.
    """

    webhookId: str | None = None
    groupKey: str | None = None
    name: str | None = None
    statusCode: str | None = None
    statusMessage: str | None = None
    clientSecret: str | None = None
    requestContentType: str | None = None
    callbackHttpMethod: str | None = None
    callbackUrl: str | None = None
    expirationDate: str | None = None
    retryCount: int | None = None
    created: str | None = None
    createdUserId: str | None = None
    modified: str | None = None
    modifiedUserId: str | None = None
    partitionKey: str | None = None

