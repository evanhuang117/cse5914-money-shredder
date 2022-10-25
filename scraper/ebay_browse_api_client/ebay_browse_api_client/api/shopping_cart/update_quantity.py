from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient
from ...models.remote_shopcart_response import RemoteShopcartResponse
from ...models.update_cart_item_input import UpdateCartItemInput
from ...types import Response


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    json_body: UpdateCartItemInput,
) -> Dict[str, Any]:
    url = "{}/shopping_cart/update_quantity".format(client.base_url)

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
    json_body: UpdateCartItemInput,
) -> Response[Union[Any, RemoteShopcartResponse]]:
    """<span class=\"tablenote\"><b>Note: </b><img src=\"/cms/img/docs/experimental-icon.svg\"
    class=\"legend-icon experimental-icon\" alt=\"Experimental Release\" title=\"Experimental Release\"
    />  This is an <a href=\"https://developer.ebay.com/api-
    docs/static/versioning.html#experimental\">experimental</a> method that is available as a <a
    href=\"https://developer.ebay.com/api-docs/static/versioning.html#limited\" target=\"_blank\"> <img
    src=\"/cms/img/docs/partners-api.svg\" class=\"legend-icon partners-icon\" title=\"Limited Release\"
    alt=\"Limited Release\" />(Limited Release)</a> to select developers approved by business
    units.</span>  <p>This method updates the quantity value of a specific item in the eBay member's
    cart. You specify the ID of the item in the cart (<b>cartItemId</b>) and the new value for the
    quantity. If the <b> quantity</b> value is greater than the number of available, the <b>
    quantity</b> value is changed to the number available and a warning is returned. For example, if
    there are 15 baseballs available and you set the <b> quantity</b> value to 50, the service
    automatically changes the value of <b>quantity</b> to 15.   <br /><br />The response returns all the
    items in the eBay member's cart; items added to the cart while on ebay.com as well as items added to
    the cart using the Browse API.   The quantity and state of an item changes often. If the item
    becomes \"unavailable\" such as, the listing has ended or the item is out of stock, the item will be
    returned in the <b> unavailableCartItems</b> container.</p>  <p span class=\"tablenote\"><b>Note:
    </b> The  <b> cartItemId</b> is not the same as the item ID. The <b> cartItemId</b> is the
    identifier of a specific item <i>in</i> the cart and is generated when the item was added to the
    cart.</span></p>                 <h3><b>URLs for this method</b></h3>           <p><ul>  <li><b>
    Production URL: </b>
    <code>https://api.ebay.com/buy/browse/v1/shopping_cart/update_quantity</code></li>
    <li><b> Sandbox URL:
    </b><code>https://api.sandbox.ebay.com/buy/browse/v1/shopping_cart/update_quantity</code>  <br /><br
    /><b>Note: </b>This method is not available in the eBay API Explorer.</li>    </ul>    </p>
    <h3><b>Restrictions </b></h3> <p>This method can be used only for eBay members. For a list of
    supported sites and other restrictions, see <a href=\"/api-docs/buy/browse/overview.html#API\">API
    Restrictions</a>.</p>

    Args:
        json_body (UpdateCartItemInput): The type that defines the fields for the
            <b>updateQuantity</b> request.

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
    json_body: UpdateCartItemInput,
) -> Optional[Union[Any, RemoteShopcartResponse]]:
    """<span class=\"tablenote\"><b>Note: </b><img src=\"/cms/img/docs/experimental-icon.svg\"
    class=\"legend-icon experimental-icon\" alt=\"Experimental Release\" title=\"Experimental Release\"
    />  This is an <a href=\"https://developer.ebay.com/api-
    docs/static/versioning.html#experimental\">experimental</a> method that is available as a <a
    href=\"https://developer.ebay.com/api-docs/static/versioning.html#limited\" target=\"_blank\"> <img
    src=\"/cms/img/docs/partners-api.svg\" class=\"legend-icon partners-icon\" title=\"Limited Release\"
    alt=\"Limited Release\" />(Limited Release)</a> to select developers approved by business
    units.</span>  <p>This method updates the quantity value of a specific item in the eBay member's
    cart. You specify the ID of the item in the cart (<b>cartItemId</b>) and the new value for the
    quantity. If the <b> quantity</b> value is greater than the number of available, the <b>
    quantity</b> value is changed to the number available and a warning is returned. For example, if
    there are 15 baseballs available and you set the <b> quantity</b> value to 50, the service
    automatically changes the value of <b>quantity</b> to 15.   <br /><br />The response returns all the
    items in the eBay member's cart; items added to the cart while on ebay.com as well as items added to
    the cart using the Browse API.   The quantity and state of an item changes often. If the item
    becomes \"unavailable\" such as, the listing has ended or the item is out of stock, the item will be
    returned in the <b> unavailableCartItems</b> container.</p>  <p span class=\"tablenote\"><b>Note:
    </b> The  <b> cartItemId</b> is not the same as the item ID. The <b> cartItemId</b> is the
    identifier of a specific item <i>in</i> the cart and is generated when the item was added to the
    cart.</span></p>                 <h3><b>URLs for this method</b></h3>           <p><ul>  <li><b>
    Production URL: </b>
    <code>https://api.ebay.com/buy/browse/v1/shopping_cart/update_quantity</code></li>
    <li><b> Sandbox URL:
    </b><code>https://api.sandbox.ebay.com/buy/browse/v1/shopping_cart/update_quantity</code>  <br /><br
    /><b>Note: </b>This method is not available in the eBay API Explorer.</li>    </ul>    </p>
    <h3><b>Restrictions </b></h3> <p>This method can be used only for eBay members. For a list of
    supported sites and other restrictions, see <a href=\"/api-docs/buy/browse/overview.html#API\">API
    Restrictions</a>.</p>

    Args:
        json_body (UpdateCartItemInput): The type that defines the fields for the
            <b>updateQuantity</b> request.

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
    json_body: UpdateCartItemInput,
) -> Response[Union[Any, RemoteShopcartResponse]]:
    """<span class=\"tablenote\"><b>Note: </b><img src=\"/cms/img/docs/experimental-icon.svg\"
    class=\"legend-icon experimental-icon\" alt=\"Experimental Release\" title=\"Experimental Release\"
    />  This is an <a href=\"https://developer.ebay.com/api-
    docs/static/versioning.html#experimental\">experimental</a> method that is available as a <a
    href=\"https://developer.ebay.com/api-docs/static/versioning.html#limited\" target=\"_blank\"> <img
    src=\"/cms/img/docs/partners-api.svg\" class=\"legend-icon partners-icon\" title=\"Limited Release\"
    alt=\"Limited Release\" />(Limited Release)</a> to select developers approved by business
    units.</span>  <p>This method updates the quantity value of a specific item in the eBay member's
    cart. You specify the ID of the item in the cart (<b>cartItemId</b>) and the new value for the
    quantity. If the <b> quantity</b> value is greater than the number of available, the <b>
    quantity</b> value is changed to the number available and a warning is returned. For example, if
    there are 15 baseballs available and you set the <b> quantity</b> value to 50, the service
    automatically changes the value of <b>quantity</b> to 15.   <br /><br />The response returns all the
    items in the eBay member's cart; items added to the cart while on ebay.com as well as items added to
    the cart using the Browse API.   The quantity and state of an item changes often. If the item
    becomes \"unavailable\" such as, the listing has ended or the item is out of stock, the item will be
    returned in the <b> unavailableCartItems</b> container.</p>  <p span class=\"tablenote\"><b>Note:
    </b> The  <b> cartItemId</b> is not the same as the item ID. The <b> cartItemId</b> is the
    identifier of a specific item <i>in</i> the cart and is generated when the item was added to the
    cart.</span></p>                 <h3><b>URLs for this method</b></h3>           <p><ul>  <li><b>
    Production URL: </b>
    <code>https://api.ebay.com/buy/browse/v1/shopping_cart/update_quantity</code></li>
    <li><b> Sandbox URL:
    </b><code>https://api.sandbox.ebay.com/buy/browse/v1/shopping_cart/update_quantity</code>  <br /><br
    /><b>Note: </b>This method is not available in the eBay API Explorer.</li>    </ul>    </p>
    <h3><b>Restrictions </b></h3> <p>This method can be used only for eBay members. For a list of
    supported sites and other restrictions, see <a href=\"/api-docs/buy/browse/overview.html#API\">API
    Restrictions</a>.</p>

    Args:
        json_body (UpdateCartItemInput): The type that defines the fields for the
            <b>updateQuantity</b> request.

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
    json_body: UpdateCartItemInput,
) -> Optional[Union[Any, RemoteShopcartResponse]]:
    """<span class=\"tablenote\"><b>Note: </b><img src=\"/cms/img/docs/experimental-icon.svg\"
    class=\"legend-icon experimental-icon\" alt=\"Experimental Release\" title=\"Experimental Release\"
    />  This is an <a href=\"https://developer.ebay.com/api-
    docs/static/versioning.html#experimental\">experimental</a> method that is available as a <a
    href=\"https://developer.ebay.com/api-docs/static/versioning.html#limited\" target=\"_blank\"> <img
    src=\"/cms/img/docs/partners-api.svg\" class=\"legend-icon partners-icon\" title=\"Limited Release\"
    alt=\"Limited Release\" />(Limited Release)</a> to select developers approved by business
    units.</span>  <p>This method updates the quantity value of a specific item in the eBay member's
    cart. You specify the ID of the item in the cart (<b>cartItemId</b>) and the new value for the
    quantity. If the <b> quantity</b> value is greater than the number of available, the <b>
    quantity</b> value is changed to the number available and a warning is returned. For example, if
    there are 15 baseballs available and you set the <b> quantity</b> value to 50, the service
    automatically changes the value of <b>quantity</b> to 15.   <br /><br />The response returns all the
    items in the eBay member's cart; items added to the cart while on ebay.com as well as items added to
    the cart using the Browse API.   The quantity and state of an item changes often. If the item
    becomes \"unavailable\" such as, the listing has ended or the item is out of stock, the item will be
    returned in the <b> unavailableCartItems</b> container.</p>  <p span class=\"tablenote\"><b>Note:
    </b> The  <b> cartItemId</b> is not the same as the item ID. The <b> cartItemId</b> is the
    identifier of a specific item <i>in</i> the cart and is generated when the item was added to the
    cart.</span></p>                 <h3><b>URLs for this method</b></h3>           <p><ul>  <li><b>
    Production URL: </b>
    <code>https://api.ebay.com/buy/browse/v1/shopping_cart/update_quantity</code></li>
    <li><b> Sandbox URL:
    </b><code>https://api.sandbox.ebay.com/buy/browse/v1/shopping_cart/update_quantity</code>  <br /><br
    /><b>Note: </b>This method is not available in the eBay API Explorer.</li>    </ul>    </p>
    <h3><b>Restrictions </b></h3> <p>This method can be used only for eBay members. For a list of
    supported sites and other restrictions, see <a href=\"/api-docs/buy/browse/overview.html#API\">API
    Restrictions</a>.</p>

    Args:
        json_body (UpdateCartItemInput): The type that defines the fields for the
            <b>updateQuantity</b> request.

    Returns:
        Response[Union[Any, RemoteShopcartResponse]]
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
        )
    ).parsed
