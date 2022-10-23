from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient
from ...models.item_group import ItemGroup
from ...types import UNSET, Response


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    item_group_id: str,
) -> Dict[str, Any]:
    url = "{}/item/get_items_by_item_group".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["item_group_id"] = item_group_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, ItemGroup]]:
    if response.status_code == 200:
        response_200 = ItemGroup.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400
    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404
    if response.status_code == 409:
        response_409 = cast(Any, None)
        return response_409
    if response.status_code == 500:
        response_500 = cast(Any, None)
        return response_500
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Any, ItemGroup]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    item_group_id: str,
) -> Response[Union[Any, ItemGroup]]:
    """<p>This method retrieves the details of the individual items in an item group. An item group is an
    item that has various aspect differences, such as color, size, storage capacity, etc. </p>  <p>You
    pass in the item group ID as a URI parameter. You use this method to show the item details of items
    with multiple aspects, such as color, size, storage capacity, etc.  </p>  <p>This method returns two
    main containers;  <b> items</b> and <b> commonDescriptions</b>. The <b> items</b> container has an
    array of  containers with the details of each item in the group. The <b> commonDescriptions</b>
    container has an array of containers for a description and the item ids of all the items that have
    this exact description. Because items within an item group often have the same description, this
    decreases the size of the response. </p>         <h3>URLs for this method</h3>           <p><ul>
    <li><b> Production URL: </b>
    <code>https://api.ebay.com/buy/browse/v1/item/get_items_by_item_group?</code></li>
    <li><b> Sandbox URL:
    </b><code>https://api.sandbox.ebay.com/buy/browse/v1/item/get_items_by_item_group?</code></li>
    </ul>    </p>            <h3><b> Request headers</b></h3> This method uses the  <b>X-EBAY-C-
    ENDUSERCTX</b> request header to support revenue sharing for eBay Partner Networks and to improve
    the accuracy of shipping and delivery time estimations.   For details see, <a href=\"/api-
    docs/buy/static/api-browse.html#Headers\">Request headers</a> in the Buying Integration Guide.
    <h3><b> Restrictions </b></h3> <p>For a list of supported sites and other restrictions, see <a
    href=\"/api-docs/buy/browse/overview.html#API\">API Restrictions</a>.</p> <span
    class=\"tablenote\"><b>eBay Partner Network: </b> In order to be commissioned for your sales, you
    must use the URL returned in the <code>itemAffiliateWebUrl</code> field to forward your buyer to the
    ebay.com site. </span>

    Args:
        item_group_id (str):

    Returns:
        Response[Union[Any, ItemGroup]]
    """

    kwargs = _get_kwargs(
        client=client,
        item_group_id=item_group_id,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: AuthenticatedClient,
    item_group_id: str,
) -> Optional[Union[Any, ItemGroup]]:
    """<p>This method retrieves the details of the individual items in an item group. An item group is an
    item that has various aspect differences, such as color, size, storage capacity, etc. </p>  <p>You
    pass in the item group ID as a URI parameter. You use this method to show the item details of items
    with multiple aspects, such as color, size, storage capacity, etc.  </p>  <p>This method returns two
    main containers;  <b> items</b> and <b> commonDescriptions</b>. The <b> items</b> container has an
    array of  containers with the details of each item in the group. The <b> commonDescriptions</b>
    container has an array of containers for a description and the item ids of all the items that have
    this exact description. Because items within an item group often have the same description, this
    decreases the size of the response. </p>         <h3>URLs for this method</h3>           <p><ul>
    <li><b> Production URL: </b>
    <code>https://api.ebay.com/buy/browse/v1/item/get_items_by_item_group?</code></li>
    <li><b> Sandbox URL:
    </b><code>https://api.sandbox.ebay.com/buy/browse/v1/item/get_items_by_item_group?</code></li>
    </ul>    </p>            <h3><b> Request headers</b></h3> This method uses the  <b>X-EBAY-C-
    ENDUSERCTX</b> request header to support revenue sharing for eBay Partner Networks and to improve
    the accuracy of shipping and delivery time estimations.   For details see, <a href=\"/api-
    docs/buy/static/api-browse.html#Headers\">Request headers</a> in the Buying Integration Guide.
    <h3><b> Restrictions </b></h3> <p>For a list of supported sites and other restrictions, see <a
    href=\"/api-docs/buy/browse/overview.html#API\">API Restrictions</a>.</p> <span
    class=\"tablenote\"><b>eBay Partner Network: </b> In order to be commissioned for your sales, you
    must use the URL returned in the <code>itemAffiliateWebUrl</code> field to forward your buyer to the
    ebay.com site. </span>

    Args:
        item_group_id (str):

    Returns:
        Response[Union[Any, ItemGroup]]
    """

    return sync_detailed(
        client=client,
        item_group_id=item_group_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    item_group_id: str,
) -> Response[Union[Any, ItemGroup]]:
    """<p>This method retrieves the details of the individual items in an item group. An item group is an
    item that has various aspect differences, such as color, size, storage capacity, etc. </p>  <p>You
    pass in the item group ID as a URI parameter. You use this method to show the item details of items
    with multiple aspects, such as color, size, storage capacity, etc.  </p>  <p>This method returns two
    main containers;  <b> items</b> and <b> commonDescriptions</b>. The <b> items</b> container has an
    array of  containers with the details of each item in the group. The <b> commonDescriptions</b>
    container has an array of containers for a description and the item ids of all the items that have
    this exact description. Because items within an item group often have the same description, this
    decreases the size of the response. </p>         <h3>URLs for this method</h3>           <p><ul>
    <li><b> Production URL: </b>
    <code>https://api.ebay.com/buy/browse/v1/item/get_items_by_item_group?</code></li>
    <li><b> Sandbox URL:
    </b><code>https://api.sandbox.ebay.com/buy/browse/v1/item/get_items_by_item_group?</code></li>
    </ul>    </p>            <h3><b> Request headers</b></h3> This method uses the  <b>X-EBAY-C-
    ENDUSERCTX</b> request header to support revenue sharing for eBay Partner Networks and to improve
    the accuracy of shipping and delivery time estimations.   For details see, <a href=\"/api-
    docs/buy/static/api-browse.html#Headers\">Request headers</a> in the Buying Integration Guide.
    <h3><b> Restrictions </b></h3> <p>For a list of supported sites and other restrictions, see <a
    href=\"/api-docs/buy/browse/overview.html#API\">API Restrictions</a>.</p> <span
    class=\"tablenote\"><b>eBay Partner Network: </b> In order to be commissioned for your sales, you
    must use the URL returned in the <code>itemAffiliateWebUrl</code> field to forward your buyer to the
    ebay.com site. </span>

    Args:
        item_group_id (str):

    Returns:
        Response[Union[Any, ItemGroup]]
    """

    kwargs = _get_kwargs(
        client=client,
        item_group_id=item_group_id,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    item_group_id: str,
) -> Optional[Union[Any, ItemGroup]]:
    """<p>This method retrieves the details of the individual items in an item group. An item group is an
    item that has various aspect differences, such as color, size, storage capacity, etc. </p>  <p>You
    pass in the item group ID as a URI parameter. You use this method to show the item details of items
    with multiple aspects, such as color, size, storage capacity, etc.  </p>  <p>This method returns two
    main containers;  <b> items</b> and <b> commonDescriptions</b>. The <b> items</b> container has an
    array of  containers with the details of each item in the group. The <b> commonDescriptions</b>
    container has an array of containers for a description and the item ids of all the items that have
    this exact description. Because items within an item group often have the same description, this
    decreases the size of the response. </p>         <h3>URLs for this method</h3>           <p><ul>
    <li><b> Production URL: </b>
    <code>https://api.ebay.com/buy/browse/v1/item/get_items_by_item_group?</code></li>
    <li><b> Sandbox URL:
    </b><code>https://api.sandbox.ebay.com/buy/browse/v1/item/get_items_by_item_group?</code></li>
    </ul>    </p>            <h3><b> Request headers</b></h3> This method uses the  <b>X-EBAY-C-
    ENDUSERCTX</b> request header to support revenue sharing for eBay Partner Networks and to improve
    the accuracy of shipping and delivery time estimations.   For details see, <a href=\"/api-
    docs/buy/static/api-browse.html#Headers\">Request headers</a> in the Buying Integration Guide.
    <h3><b> Restrictions </b></h3> <p>For a list of supported sites and other restrictions, see <a
    href=\"/api-docs/buy/browse/overview.html#API\">API Restrictions</a>.</p> <span
    class=\"tablenote\"><b>eBay Partner Network: </b> In order to be commissioned for your sales, you
    must use the URL returned in the <code>itemAffiliateWebUrl</code> field to forward your buyer to the
    ebay.com site. </span>

    Args:
        item_group_id (str):

    Returns:
        Response[Union[Any, ItemGroup]]
    """

    return (
        await asyncio_detailed(
            client=client,
            item_group_id=item_group_id,
        )
    ).parsed
