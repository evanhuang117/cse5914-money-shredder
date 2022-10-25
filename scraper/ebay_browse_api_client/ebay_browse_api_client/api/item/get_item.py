from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient
from ...models.item import Item
from ...types import UNSET, Response, Unset


def _get_kwargs(
    item_id: str,
    *,
    client: AuthenticatedClient,
    fieldgroups: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/item/{item_id}".format(client.base_url, item_id=item_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["fieldgroups"] = fieldgroups

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, Item]]:
    if response.status_code == 200:
        response_200 = Item.from_dict(response.json())

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


def _build_response(*, response: httpx.Response) -> Response[Union[Any, Item]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    item_id: str,
    *,
    client: AuthenticatedClient,
    fieldgroups: Union[Unset, None, str] = UNSET,
) -> Response[Union[Any, Item]]:
    """<p>This method retrieves the details of a specific item, such as description, price, category, all
    item aspects, condition, return policies, seller feedback and score, shipping options, shipping
    costs, estimated delivery, and other information the buyer needs to make a purchasing
    decision.</p><p>The Buy APIs are designed to let you create an eBay shopping experience in your app
    or website. This means you will need to know when something, such as the availability, quantity,
    etc., has changed in any eBay item you are offering. You can do this easily by setting the <b>
    fieldgroups</b> URI parameter. This parameter lets you control what is returned in the response.</p>
    <p>Setting <b> fieldgroups</b> to <code>COMPACT</code> reduces the response to only those fields
    that you need in order to check if any item detail has changed.  Setting <b> fieldgroups</b> to
    <code>PRODUCT</code>, adds additional fields to the default response that return information about
    the product of the item. You can use either <code>COMPACT</code> or <code>PRODUCT</code> but not
    both. For more information, see <a href=\"/api-
    docs/buy/browse/resources/item/methods/getItem#uri.fieldgroups\">fieldgroups</a>.</p>      <h3>URLs
    for this method</h3>           <p><ul>            <li><b> Production URL: </b>
    <code>https://api.ebay.com/buy/browse/v1/item/{item_id}</code></li>            <li><b> Sandbox URL:
    </b><code>https://api.sandbox.ebay.com/buy/browse/v1/item/{item_id}</code></li>           </ul>
    </p>                   <h3><b> Request headers</b></h3> This method uses the  <b>X-EBAY-C-
    ENDUSERCTX</b> request header to support revenue sharing for eBay Partner Networks and to improve
    the accuracy of shipping and delivery time estimations.  For details see, <a href=\"/api-
    docs/buy/static/api-browse.html#Headers\">Request headers</a> in the Buying Integration Guide.
    <h3><b> Restrictions </b></h3> <p>For a list of supported sites and other restrictions, see <a
    href=\"/api-docs/buy/browse/overview.html#API\">API Restrictions</a>.</p> <span
    class=\"tablenote\"><b>eBay Partner Network: </b> In order to be commissioned for your sales, you
    must use the URL returned in the <code>itemAffiliateWebUrl</code> field to forward your buyer to the
    ebay.com site. </span>

    Args:
        item_id (str):
        fieldgroups (Union[Unset, None, str]):

    Returns:
        Response[Union[Any, Item]]
    """

    kwargs = _get_kwargs(
        item_id=item_id,
        client=client,
        fieldgroups=fieldgroups,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    item_id: str,
    *,
    client: AuthenticatedClient,
    fieldgroups: Union[Unset, None, str] = UNSET,
) -> Optional[Union[Any, Item]]:
    """<p>This method retrieves the details of a specific item, such as description, price, category, all
    item aspects, condition, return policies, seller feedback and score, shipping options, shipping
    costs, estimated delivery, and other information the buyer needs to make a purchasing
    decision.</p><p>The Buy APIs are designed to let you create an eBay shopping experience in your app
    or website. This means you will need to know when something, such as the availability, quantity,
    etc., has changed in any eBay item you are offering. You can do this easily by setting the <b>
    fieldgroups</b> URI parameter. This parameter lets you control what is returned in the response.</p>
    <p>Setting <b> fieldgroups</b> to <code>COMPACT</code> reduces the response to only those fields
    that you need in order to check if any item detail has changed.  Setting <b> fieldgroups</b> to
    <code>PRODUCT</code>, adds additional fields to the default response that return information about
    the product of the item. You can use either <code>COMPACT</code> or <code>PRODUCT</code> but not
    both. For more information, see <a href=\"/api-
    docs/buy/browse/resources/item/methods/getItem#uri.fieldgroups\">fieldgroups</a>.</p>      <h3>URLs
    for this method</h3>           <p><ul>            <li><b> Production URL: </b>
    <code>https://api.ebay.com/buy/browse/v1/item/{item_id}</code></li>            <li><b> Sandbox URL:
    </b><code>https://api.sandbox.ebay.com/buy/browse/v1/item/{item_id}</code></li>           </ul>
    </p>                   <h3><b> Request headers</b></h3> This method uses the  <b>X-EBAY-C-
    ENDUSERCTX</b> request header to support revenue sharing for eBay Partner Networks and to improve
    the accuracy of shipping and delivery time estimations.  For details see, <a href=\"/api-
    docs/buy/static/api-browse.html#Headers\">Request headers</a> in the Buying Integration Guide.
    <h3><b> Restrictions </b></h3> <p>For a list of supported sites and other restrictions, see <a
    href=\"/api-docs/buy/browse/overview.html#API\">API Restrictions</a>.</p> <span
    class=\"tablenote\"><b>eBay Partner Network: </b> In order to be commissioned for your sales, you
    must use the URL returned in the <code>itemAffiliateWebUrl</code> field to forward your buyer to the
    ebay.com site. </span>

    Args:
        item_id (str):
        fieldgroups (Union[Unset, None, str]):

    Returns:
        Response[Union[Any, Item]]
    """

    return sync_detailed(
        item_id=item_id,
        client=client,
        fieldgroups=fieldgroups,
    ).parsed


async def asyncio_detailed(
    item_id: str,
    *,
    client: AuthenticatedClient,
    fieldgroups: Union[Unset, None, str] = UNSET,
) -> Response[Union[Any, Item]]:
    """<p>This method retrieves the details of a specific item, such as description, price, category, all
    item aspects, condition, return policies, seller feedback and score, shipping options, shipping
    costs, estimated delivery, and other information the buyer needs to make a purchasing
    decision.</p><p>The Buy APIs are designed to let you create an eBay shopping experience in your app
    or website. This means you will need to know when something, such as the availability, quantity,
    etc., has changed in any eBay item you are offering. You can do this easily by setting the <b>
    fieldgroups</b> URI parameter. This parameter lets you control what is returned in the response.</p>
    <p>Setting <b> fieldgroups</b> to <code>COMPACT</code> reduces the response to only those fields
    that you need in order to check if any item detail has changed.  Setting <b> fieldgroups</b> to
    <code>PRODUCT</code>, adds additional fields to the default response that return information about
    the product of the item. You can use either <code>COMPACT</code> or <code>PRODUCT</code> but not
    both. For more information, see <a href=\"/api-
    docs/buy/browse/resources/item/methods/getItem#uri.fieldgroups\">fieldgroups</a>.</p>      <h3>URLs
    for this method</h3>           <p><ul>            <li><b> Production URL: </b>
    <code>https://api.ebay.com/buy/browse/v1/item/{item_id}</code></li>            <li><b> Sandbox URL:
    </b><code>https://api.sandbox.ebay.com/buy/browse/v1/item/{item_id}</code></li>           </ul>
    </p>                   <h3><b> Request headers</b></h3> This method uses the  <b>X-EBAY-C-
    ENDUSERCTX</b> request header to support revenue sharing for eBay Partner Networks and to improve
    the accuracy of shipping and delivery time estimations.  For details see, <a href=\"/api-
    docs/buy/static/api-browse.html#Headers\">Request headers</a> in the Buying Integration Guide.
    <h3><b> Restrictions </b></h3> <p>For a list of supported sites and other restrictions, see <a
    href=\"/api-docs/buy/browse/overview.html#API\">API Restrictions</a>.</p> <span
    class=\"tablenote\"><b>eBay Partner Network: </b> In order to be commissioned for your sales, you
    must use the URL returned in the <code>itemAffiliateWebUrl</code> field to forward your buyer to the
    ebay.com site. </span>

    Args:
        item_id (str):
        fieldgroups (Union[Unset, None, str]):

    Returns:
        Response[Union[Any, Item]]
    """

    kwargs = _get_kwargs(
        item_id=item_id,
        client=client,
        fieldgroups=fieldgroups,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    item_id: str,
    *,
    client: AuthenticatedClient,
    fieldgroups: Union[Unset, None, str] = UNSET,
) -> Optional[Union[Any, Item]]:
    """<p>This method retrieves the details of a specific item, such as description, price, category, all
    item aspects, condition, return policies, seller feedback and score, shipping options, shipping
    costs, estimated delivery, and other information the buyer needs to make a purchasing
    decision.</p><p>The Buy APIs are designed to let you create an eBay shopping experience in your app
    or website. This means you will need to know when something, such as the availability, quantity,
    etc., has changed in any eBay item you are offering. You can do this easily by setting the <b>
    fieldgroups</b> URI parameter. This parameter lets you control what is returned in the response.</p>
    <p>Setting <b> fieldgroups</b> to <code>COMPACT</code> reduces the response to only those fields
    that you need in order to check if any item detail has changed.  Setting <b> fieldgroups</b> to
    <code>PRODUCT</code>, adds additional fields to the default response that return information about
    the product of the item. You can use either <code>COMPACT</code> or <code>PRODUCT</code> but not
    both. For more information, see <a href=\"/api-
    docs/buy/browse/resources/item/methods/getItem#uri.fieldgroups\">fieldgroups</a>.</p>      <h3>URLs
    for this method</h3>           <p><ul>            <li><b> Production URL: </b>
    <code>https://api.ebay.com/buy/browse/v1/item/{item_id}</code></li>            <li><b> Sandbox URL:
    </b><code>https://api.sandbox.ebay.com/buy/browse/v1/item/{item_id}</code></li>           </ul>
    </p>                   <h3><b> Request headers</b></h3> This method uses the  <b>X-EBAY-C-
    ENDUSERCTX</b> request header to support revenue sharing for eBay Partner Networks and to improve
    the accuracy of shipping and delivery time estimations.  For details see, <a href=\"/api-
    docs/buy/static/api-browse.html#Headers\">Request headers</a> in the Buying Integration Guide.
    <h3><b> Restrictions </b></h3> <p>For a list of supported sites and other restrictions, see <a
    href=\"/api-docs/buy/browse/overview.html#API\">API Restrictions</a>.</p> <span
    class=\"tablenote\"><b>eBay Partner Network: </b> In order to be commissioned for your sales, you
    must use the URL returned in the <code>itemAffiliateWebUrl</code> field to forward your buyer to the
    ebay.com site. </span>

    Args:
        item_id (str):
        fieldgroups (Union[Unset, None, str]):

    Returns:
        Response[Union[Any, Item]]
    """

    return (
        await asyncio_detailed(
            item_id=item_id,
            client=client,
            fieldgroups=fieldgroups,
        )
    ).parsed
