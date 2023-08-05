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

from lockstep.lockstep_response import LockstepResponse
from lockstep.error_result import ErrorResult
from lockstep.fetch_result import FetchResult
from lockstep.models.creditmemoappliedmodel import CreditMemoAppliedModel

class CreditMemoAppliedClient:
    """
    API methods related to CreditMemoApplied
    """
    from lockstep.lockstep_api import LockstepApi

    def __init__(self, client: LockstepApi):
        self.client = client

    def retrieve_credit_memo_application(self, id: str, include: str) -> LockstepResponse[CreditMemoAppliedModel]:
        """
        Retrieves the Credit Memo Application specified by this unique
        identifier, optionally including nested data sets.

        Credit Memos reflect credits granted to a customer for various
        reasons, such as discounts or refunds. Credit Memos may be
        applied to Invoices as Payments. When a Credit Memo is applied
        as payment to an Invoice, Lockstep creates a Credit Memo
        Application record to track the amount from the Credit Memo that
        was applied as payment to the Invoice. You can examine Credit
        Memo Application records to track which Invoices were paid using
        this Credit.

        Parameters
        ----------
        id : str
            The unique Lockstep Platform ID number of this Credit Memo
            Application; NOT the customer's ERP key
        include : str
            To fetch additional data on this object, specify the list of
            elements to retrieve. Available collections: Attachments,
            CustomFields, Notes
        """
        path = f"/api/v1/CreditMemoApplied/{id}"
        result = self.client.send_request("GET", path, None, {"include": include}, None)
        if result.status_code >= 200 and result.status_code < 300:
            return LockstepResponse(True, result.status_code, CreditMemoAppliedModel(**result.json()), None)
        else:
            return LockstepResponse(False, result.status_code, None, ErrorResult(**result.json()))

    def update_credit_memo_application(self, id: str, body: object) -> LockstepResponse[CreditMemoAppliedModel]:
        """
        Updates an existing Credit memo Application with the information
        supplied to this PATCH call.

        The PATCH method allows you to change specific values on the
        object while leaving other values alone. As input you should
        supply a list of field names and new values. If you do not
        provide the name of a field, that field will remain unchanged.
        This allows you to ensure that you are only updating the
        specific fields desired.

        Credit Memos reflect credits granted to a customer for various
        reasons, such as discounts or refunds. Credit Memos may be
        applied to Invoices as Payments. When a Credit Memo is applied
        as payment to an Invoice, Lockstep creates a Credit Memo
        Application record to track the amount from the Credit Memo that
        was applied as payment to the Invoice. You can examine Credit
        Memo Application records to track which Invoices were paid using
        this Credit.

        Parameters
        ----------
        id : str
            The unique Lockstep Platform ID number of the Credit Memo
            Application to update; NOT the customer's ERP key
        body : object
            A list of changes to apply to this Credit Memo Application
        """
        path = f"/api/v1/CreditMemoApplied/{id}"
        result = self.client.send_request("PATCH", path, body, {}, None)
        if result.status_code >= 200 and result.status_code < 300:
            return LockstepResponse(True, result.status_code, CreditMemoAppliedModel(**result.json()), None)
        else:
            return LockstepResponse(False, result.status_code, None, ErrorResult(**result.json()))

    def delete_credit_memo_application(self, id: str) -> LockstepResponse[CreditMemoAppliedModel]:
        """
        Deletes the Credit Memo Application referred to by this unique
        identifier.

        Credit Memos reflect credits granted to a customer for various
        reasons, such as discounts or refunds. Credit Memos may be
        applied to Invoices as Payments. When a Credit Memo is applied
        as payment to an Invoice, Lockstep creates a Credit Memo
        Application record to track the amount from the Credit Memo that
        was applied as payment to the Invoice. You can examine Credit
        Memo Application records to track which Invoices were paid using
        this Credit.

        Parameters
        ----------
        id : str
            The unique Lockstep Platform ID number of the Credit Memo
            Application to delete; NOT the customer's ERP key
        """
        path = f"/api/v1/CreditMemoApplied/{id}"
        result = self.client.send_request("DELETE", path, None, {}, None)
        if result.status_code >= 200 and result.status_code < 300:
            return LockstepResponse(True, result.status_code, CreditMemoAppliedModel(**result.json()), None)
        else:
            return LockstepResponse(False, result.status_code, None, ErrorResult(**result.json()))

    def create_credit_memo_applications(self, body: list[CreditMemoAppliedModel]) -> LockstepResponse[list[CreditMemoAppliedModel]]:
        """
        Creates one or more Credit Memo Applications within this account
        and returns the records as created.

        Credit Memos reflect credits granted to a customer for various
        reasons, such as discounts or refunds. Credit Memos may be
        applied to Invoices as Payments. When a Credit Memo is applied
        as payment to an Invoice, Lockstep creates a Credit Memo
        Application record to track the amount from the Credit Memo that
        was applied as payment to the Invoice. You can examine Credit
        Memo Application records to track which Invoices were paid using
        this Credit.

        Parameters
        ----------
        body : list[CreditMemoAppliedModel]
            The Credit Memo Applications to create
        """
        path = "/api/v1/CreditMemoApplied"
        result = self.client.send_request("POST", path, body, {}, None)
        if result.status_code >= 200 and result.status_code < 300:
            return LockstepResponse(True, result.status_code, list[CreditMemoAppliedModel](**result.json()), None)
        else:
            return LockstepResponse(False, result.status_code, None, ErrorResult(**result.json()))

    def query_credit_memo_applications(self, filter: str, include: str, order: str, pageSize: int, pageNumber: int) -> LockstepResponse[FetchResult[CreditMemoAppliedModel]]:
        """
        Queries Credit Memo Applications for this account using the
        specified filtering, sorting, nested fetch, and pagination rules
        requested.

        More information on querying can be found on the [Searchlight
        Query Language](https://developer.lockstep.io/docs/querying-with-searchlight)
        page on the Lockstep Developer website.

        Credit Memos reflect credits granted to a customer for various
        reasons, such as discounts or refunds. Credit Memos may be
        applied to Invoices as Payments. When a Credit Memo is applied
        as payment to an Invoice, Lockstep creates a Credit Memo
        Application record to track the amount from the Credit Memo that
        was applied as payment to the Invoice. You can examine Credit
        Memo Application records to track which Invoices were paid using
        this Credit.

        Parameters
        ----------
        filter : str
            The filter for this query. See [Searchlight Query
            Language](https://developer.lockstep.io/docs/querying-with-searchlight)
        include : str
            To fetch additional data on this object, specify the list of
            elements to retrieve. Available collections: Attachments,
            CustomFields, Notes
        order : str
            The sort order for this query. See See [Searchlight Query
            Language](https://developer.lockstep.io/docs/querying-with-searchlight)
        pageSize : int
            The page size for results (default 200). See [Searchlight
            Query Language](https://developer.lockstep.io/docs/querying-with-searchlight)
        pageNumber : int
            The page number for results (default 0). See [Searchlight
            Query Language](https://developer.lockstep.io/docs/querying-with-searchlight)
        """
        path = "/api/v1/CreditMemoApplied/query"
        result = self.client.send_request("GET", path, None, {"filter": filter, "include": include, "order": order, "pageSize": pageSize, "pageNumber": pageNumber}, None)
        if result.status_code >= 200 and result.status_code < 300:
            return LockstepResponse(True, result.status_code, FetchResult[CreditMemoAppliedModel](**result.json()), None)
        else:
            return LockstepResponse(False, result.status_code, None, ErrorResult(**result.json()))
