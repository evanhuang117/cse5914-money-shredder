from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient
from ...models.add_cart_item_input import AddCartItemInput
from ...models.remote_shopcart_response import RemoteShopcartResponse
from ...types import Response


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    json_body: AddCartItemInput,
) -> Dict[str, Any]:
    url = "{}/shopping_cart/add_item".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body = json_body.to_dict()

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, RemoteShopcartResponse]]:
    if response.status_code == 200:
        response_200 = RemoteShopcartResponse.from_dict(response.json())

        return response_200
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204
    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400
    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403
    if response.status_code == 409:
        response_409 = cast(Any, None)
        return response_409
    if response.status_code == 500:
        response_500 = cast(Any, None)
        return response_500
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Any, RemoteShopcartResponse]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    json_body: AddCartItemInput,
) -> Response[Union[Any, RemoteShopcartResponse]]:
    """<span class=\"tablenote\"><b>Note: </b><img src=\"/cms/img/docs/experimental-icon.svg\"
    class=\"legend-icon experimental-icon\" alt=\"Experimental Release\" title=\"Experimental Release\"
    alt=\"Experimental Release\" title=\"Experimental Release\" />  This is an <a
    href=\"https://developer.ebay.com/api-docs/static/versioning.html#experimental\">Experimental</a>
    method that is available as a <a href=\"https://developer.ebay.com/api-
    docs/static/versioning.html#limited\" target=\"_blank\"> <img src=\"/cms/img/docs/partners-api.svg\"
    class=\"legend-icon partners-icon\" title=\"Limited Release\"  alt=\"Limited Release\" />(Limited
    Release)</a> to select developers approved by business units.</span>  <p>This method creates an eBay
    cart for the eBay member, if one does not exist, and adds items to that cart. Because a cart never
    expires, any item added to the cart will remain in the cart until it is removed.  <br /><br />To use
    this method, you must submit a RESTful item ID and the quantity of the item. If the <b> quantity</b>
    value is greater than the number of available, the <b> quantity</b> value is changed to the number
    available and a warning is returned. For example, if there are 15 baseballs available and you set
    the <b> quantity</b> value to 50, the service automatically changes the value of <b>quantity</b> to
    15.    <br /><br />The response returns all the items in the eBay member's cart; items added to the
    cart while on ebay.com as well as items added to the cart using the Browse API.   The quantity and
    state of an item changes often. If the item becomes \"unavailable\" such as, when the listing has
    ended or the item is out of stock, whether it has just been added to the cart or has been in the
    cart for some time, the item will be returned in the <b> unavailableCartItems</b> container.</p>
    <p span class=\"tablenote\"><b>Note: </b>There are differences between how legacy APIs, such as
    Finding, and RESTful APIs, such as Browse, return the identifier of an \"item\" and what the item ID
    represents. If you have an item ID from one of the legacy APIs, you can use the legacy item ID with
    the <a href=\"/api-docs/buy/browse/resources/item/methods/getItemByLegacyId\"> getItemByLegacyId</a>
    method to retrieve the RESTful ID for that item. For more information about how to use legacy IDs
    with the Buy APIs, see <a href=\"/api-docs/buy/static/api-browse.html#Legacy\">Legacy API
    compatibility</a> in the Buying Integration guide.</p>           <h3><b>URLs for this
    method</b></h3>           <p><ul>  <li><b> Production URL: </b>
    <code>https://api.ebay.com/buy/browse/v1/shopping_cart/add_item</code></li>            <li><b>
    Sandbox URL:  </b><code>https://api.sandbox.ebay.com/buy/browse/v1/shopping_cart/add_item</code>
    <br /><br /><b>Note: </b>This method is not available in the eBay API Explorer.</li>    </ul>
    </p>            <h3><b>Restrictions </b></h3> <ul> <li>This method can be used only for eBay
    members.</li>  <li>You can only add FIXED_PRICE items.  </li> </ul> <p>For a list of supported sites
    and other restrictions, see <a href=\"/api-docs/buy/browse/overview.html#API\">API
    Restrictions</a>.</p>

    Args:
        json_body (AddCartItemInput): The type that defines the fields for the <b>addItems</b>
            request.

    Returns:
        Response[Union[Any, RemoteShopcartResponse]]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: AuthenticatedClient,
    json_body: AddCartItemInput,
) -> Optional[Union[Any, RemoteShopcartResponse]]:
    """<span class=\"tablenote\"><b>Note: </b><img src=\"/cms/img/docs/experimental-icon.svg\"
    class=\"legend-icon experimental-icon\" alt=\"Experimental Release\" title=\"Experimental Release\"
    alt=\"Experimental Release\" title=\"Experimental Release\" />  This is an <a
    href=\"https://developer.ebay.com/api-docs/static/versioning.html#experimental\">Experimental</a>
    method that is available as a <a href=\"https://developer.ebay.com/api-
    docs/static/versioning.html#limited\" target=\"_blank\"> <img src=\"/cms/img/docs/partners-api.svg\"
    class=\"legend-icon partners-icon\" title=\"Limited Release\"  alt=\"Limited Release\" />(Limited
    Release)</a> to select developers approved by business units.</span>  <p>This method creates an eBay
    cart for the eBay member, if one does not exist, and adds items to that cart. Because a cart never
    expires, any item added to the cart will remain in the cart until it is removed.  <br /><br />To use
    this method, you must submit a RESTful item ID and the quantity of the item. If the <b> quantity</b>
    value is greater than the number of available, the <b> quantity</b> value is changed to the number
    available and a warning is returned. For example, if there are 15 baseballs available and you set
    the <b> quantity</b> value to 50, the service automatically changes the value of <b>quantity</b> to
    15.    <br /><br />The response returns all the items in the eBay member's cart; items added to the
    cart while on ebay.com as well as items added to the cart using the Browse API.   The quantity and
    state of an item changes often. If the item becomes \"unavailable\" such as, when the listing has
    ended or the item is out of stock, whether it has just been added to the cart or has been in the
    cart for some time, the item will be returned in the <b> unavailableCartItems</b> container.</p>
    <p span class=\"tablenote\"><b>Note: </b>There are differences between how legacy APIs, such as
    Finding, and RESTful APIs, such as Browse, return the identifier of an \"item\" and what the item ID
    represents. If you have an item ID from one of the legacy APIs, you can use the legacy item ID with
    the <a href=\"/api-docs/buy/browse/resources/item/methods/getItemByLegacyId\"> getItemByLegacyId</a>
    method to retrieve the RESTful ID for that item. For more information about how to use legacy IDs
    with the Buy APIs, see <a href=\"/api-docs/buy/static/api-browse.html#Legacy\">Legacy API
    compatibility</a> in the Buying Integration guide.</p>           <h3><b>URLs for this
    method</b></h3>           <p><ul>  <li><b> Production URL: </b>
    <code>https://api.ebay.com/buy/browse/v1/shopping_cart/add_item</code></li>            <li><b>
    Sandbox URL:  </b><code>https://api.sandbox.ebay.com/buy/browse/v1/shopping_cart/add_item</code>
    <br /><br /><b>Note: </b>This method is not available in the eBay API Explorer.</li>    </ul>
    </p>            <h3><b>Restrictions </b></h3> <ul> <li>This method can be used only for eBay
    members.</li>  <li>You can only add FIXED_PRICE items.  </li> </ul> <p>For a list of supported sites
    and other restrictions, see <a href=\"/api-docs/buy/browse/overview.html#API\">API
    Restrictions</a>.</p>

    Args:
        json_body (AddCartItemInput): The type that defines the fields for the <b>addItems</b>
            request.

    Returns:
        Response[Union[Any, RemoteShopcartResponse]]
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    json_body: AddCartItemInput,
) -> Response[Union[Any, RemoteShopcartResponse]]:
    """<span class=\"tablenote\"><b>Note: </b><img src=\"/cms/img/docs/experimental-icon.svg\"
    class=\"legend-icon experimental-icon\" alt=\"Experimental Release\" title=\"Experimental Release\"
    alt=\"Experimental Release\" title=\"Experimental Release\" />  This is an <a
    href=\"https://developer.ebay.com/api-docs/static/versioning.html#experimental\">Experimental</a>
    method that is available as a <a href=\"https://developer.ebay.com/api-
    docs/static/versioning.html#limited\" target=\"_blank\"> <img src=\"/cms/img/docs/partners-api.svg\"
    class=\"legend-icon partners-icon\" title=\"Limited Release\"  alt=\"Limited Release\" />(Limited
    Release)</a> to select developers approved by business units.</span>  <p>This method creates an eBay
    cart for the eBay member, if one does not exist, and adds items to that cart. Because a cart never
    expires, any item added to the cart will remain in the cart until it is removed.  <br /><br />To use
    this method, you must submit a RESTful item ID and the quantity of the item. If the <b> quantity</b>
    value is greater than the number of available, the <b> quantity</b> value is changed to the number
    available and a warning is returned. For example, if there are 15 baseballs available and you set
    the <b> quantity</b> value to 50, the service automatically changes the value of <b>quantity</b> to
    15.    <br /><br />The response returns all the items in the eBay member's cart; items added to the
    cart while on ebay.com as well as items added to the cart using the Browse API.   The quantity and
    state of an item changes often. If the item becomes \"unavailable\" such as, when the listing has
    ended or the item is out of stock, whether it has just been added to the cart or has been in the
    cart for some time, the item will be returned in the <b> unavailableCartItems</b> container.</p>
    <p span class=\"tablenote\"><b>Note: </b>There are differences between how legacy APIs, such as
    Finding, and RESTful APIs, such as Browse, return the identifier of an \"item\" and what the item ID
    represents. If you have an item ID from one of the legacy APIs, you can use the legacy item ID with
    the <a href=\"/api-docs/buy/browse/resources/item/methods/getItemByLegacyId\"> getItemByLegacyId</a>
    method to retrieve the RESTful ID for that item. For more information about how to use legacy IDs
    with the Buy APIs, see <a href=\"/api-docs/buy/static/api-browse.html#Legacy\">Legacy API
    compatibility</a> in the Buying Integration guide.</p>           <h3><b>URLs for this
    method</b></h3>           <p><ul>  <li><b> Production URL: </b>
    <code>https://api.ebay.com/buy/browse/v1/shopping_cart/add_item</code></li>            <li><b>
    Sandbox URL:  </b><code>https://api.sandbox.ebay.com/buy/browse/v1/shopping_cart/add_item</code>
    <br /><br /><b>Note: </b>This method is not available in the eBay API Explorer.</li>    </ul>
    </p>            <h3><b>Restrictions </b></h3> <ul> <li>This method can be used only for eBay
    members.</li>  <li>You can only add FIXED_PRICE items.  </li> </ul> <p>For a list of supported sites
    and other restrictions, see <a href=\"/api-docs/buy/browse/overview.html#API\">API
    Restrictions</a>.</p>

    Args:
        json_body (AddCartItemInput): The type that defines the fields for the <b>addItems</b>
            request.

    Returns:
        Response[Union[Any, RemoteShopcartResponse]]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    json_body: AddCartItemInput,
) -> Optional[Union[Any, RemoteShopcartResponse]]:
    """<span class=\"tablenote\"><b>Note: </b><img src=\"/cms/img/docs/experimental-icon.svg\"
    class=\"legend-icon experimental-icon\" alt=\"Experimental Release\" title=\"Experimental Release\"
    alt=\"Experimental Release\" title=\"Experimental Release\" />  This is an <a
    href=\"https://developer.ebay.com/api-docs/static/versioning.html#experimental\">Experimental</a>
    method that is available as a <a href=\"https://developer.ebay.com/api-
    docs/static/versioning.html#limited\" target=\"_blank\"> <img src=\"/cms/img/docs/partners-api.svg\"
    class=\"legend-icon partners-icon\" title=\"Limited Release\"  alt=\"Limited Release\" />(Limited
    Release)</a> to select developers approved by business units.</span>  <p>This method creates an eBay
    cart for the eBay member, if one does not exist, and adds items to that cart. Because a cart never
    expires, any item added to the cart will remain in the cart until it is removed.  <br /><br />To use
    this method, you must submit a RESTful item ID and the quantity of the item. If the <b> quantity</b>
    value is greater than the number of available, the <b> quantity</b> value is changed to the number
    available and a warning is returned. For example, if there are 15 baseballs available and you set
    the <b> quantity</b> value to 50, the service automatically changes the value of <b>quantity</b> to
    15.    <br /><br />The response returns all the items in the eBay member's cart; items added to the
    cart while on ebay.com as well as items added to the cart using the Browse API.   The quantity and
    state of an item changes often. If the item becomes \"unavailable\" such as, when the listing has
    ended or the item is out of stock, whether it has just been added to the cart or has been in the
    cart for some time, the item will be returned in the <b> unavailableCartItems</b> container.</p>
    <p span class=\"tablenote\"><b>Note: </b>There are differences between how legacy APIs, such as
    Finding, and RESTful APIs, such as Browse, return the identifier of an \"item\" and what the item ID
    represents. If you have an item ID from one of the legacy APIs, you can use the legacy item ID with
    the <a href=\"/api-docs/buy/browse/resources/item/methods/getItemByLegacyId\"> getItemByLegacyId</a>
    method to retrieve the RESTful ID for that item. For more information about how to use legacy IDs
    with the Buy APIs, see <a href=\"/api-docs/buy/static/api-browse.html#Legacy\">Legacy API
    compatibility</a> in the Buying Integration guide.</p>           <h3><b>URLs for this
    method</b></h3>           <p><ul>  <li><b> Production URL: </b>
    <code>https://api.ebay.com/buy/browse/v1/shopping_cart/add_item</code></li>            <li><b>
    Sandbox URL:  </b><code>https://api.sandbox.ebay.com/buy/browse/v1/shopping_cart/add_item</code>
    <br /><br /><b>Note: </b>This method is not available in the eBay API Explorer.</li>    </ul>
    </p>            <h3><b>Restrictions </b></h3> <ul> <li>This method can be used only for eBay
    members.</li>  <li>You can only add FIXED_PRICE items.  </li> </ul> <p>For a list of supported sites
    and other restrictions, see <a href=\"/api-docs/buy/browse/overview.html#API\">API
    Restrictions</a>.</p>

    Args:
        json_body (AddCartItemInput): The type that defines the fields for the <b>addItems</b>
            request.

    Returns:
        Response[Union[Any, RemoteShopcartResponse]]
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
        )
    ).parsed
