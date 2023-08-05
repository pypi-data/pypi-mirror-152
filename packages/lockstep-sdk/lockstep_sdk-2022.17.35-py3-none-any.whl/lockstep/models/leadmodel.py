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
class LeadModel:
    """
    Represents leads for creating new ERP connectors
    """

    leadId: str | None = None
    name: str | None = None
    company: str | None = None
    email: str | None = None
    erpSystem: str | None = None

