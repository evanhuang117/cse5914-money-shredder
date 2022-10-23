from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient
from ...models.item import Item
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    fieldgroups: Union[Unset, None, str] = UNSET,
    legacy_item_id: str,
    legacy_variation_id: Union[Unset, None, str] = UNSET,
    legacy_variation_sku: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/item/get_item_by_legacy_id".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["fieldgroups"] = fieldgroups

    params["legacy_item_id"] = legacy_item_id

    params["legacy_variation_id"] = legacy_variation_id

    params["legacy_variation_sku"] = legacy_variation_sku

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
    *,
    client: AuthenticatedClient,
    fieldgroups: Union[Unset, None, str] = UNSET,
    legacy_item_id: str,
    legacy_variation_id: Union[Unset, None, str] = UNSET,
    legacy_variation_sku: Union[Unset, None, str] = UNSET,
) -> Response[Union[Any, Item]]:
    """<p>This method is a bridge between the eBay legacy APIs, such as  <b> Shopping</b>, and <b>
    Finding</b> and the eBay Buy APIs. There are differences between how legacy APIs and RESTful APIs
    return the identifier of an \"item\" and what the item ID represents. This method lets you use the
    legacy item ids retrieve the details of a specific item, such as description, price, and other
    information the buyer needs to make a purchasing decision. It also returns the RESTful item ID,
    which you can use with all the Buy API  methods.</p>  <p>For more information about how to use
    legacy ids with the Buy APIs, see <a href=\"/api-docs/buy/static/api-browse.html#Legacy\">Legacy API
    compatibility</a> in the Buying Integration guide.</p>  <p>This method returns the item details and
    requires you to pass in either the item ID of a non-variation item or the item ids of both the
    parent and child of an item group. An item group is an item that has various aspect differences,
    such as color, size, storage capacity, etc.</p> <p>When an item group is created, one of the item
    variations, such as the red shirt size L, is chosen as the \"parent\". All the other items in the
    group are the children, such as the blue shirt size L, red shirt size M, etc.</p>    <p>The <b>
    fieldgroups</b> URI parameter lets you control what is returned in the response. Setting <b>
    fieldgroups</b> to <code>PRODUCT</code>, adds additional fields to the default response that return
    information about the product of the item. For more information, see <a href=\"/api-
    docs/buy/browse/resources/item/methods/getItemByLegacyItem#uri.fieldgroups\">fieldgroups</a>.</p>
    <h3>URLs for this method</h3>           <p><ul>            <li><b> Production URL: </b>
    <code>https://api.ebay.com/buy/browse/v1/item/get_item_by_legacy_id?</code></li>            <li><b>
    Sandbox URL:
    </b><code>https://api.sandbox.ebay.com/buy/browse/v1/item/get_item_by_legacy_id?</code></li>
    </ul>    </p>              <h3><b> Request headers</b></h3> This method uses the  <b>X-EBAY-C-
    ENDUSERCTX</b> request header to support revenue sharing for eBay Partner Networks and to improve
    the accuracy of shipping and delivery time estimations.   For details see, <a href=\"/api-
    docs/buy/static/api-browse.html#Headers\">Request headers</a> in the Buying Integration Guide.
    <h3><b> Restrictions </b></h3> <p>For a list of supported sites and other restrictions, see <a
    href=\"/api-docs/buy/browse/overview.html#API\">API Restrictions</a>.</p> <span
    class=\"tablenote\"><b>eBay Partner Network: </b> In order to be commissioned for your sales, you
    must use the URL returned in the <code>itemAffiliateWebUrl</code> field to forward your buyer to the
    ebay.com site. </span>

    Args:
        fieldgroups (Union[Unset, None, str]):
        legacy_item_id (str):
        legacy_variation_id (Union[Unset, None, str]):
        legacy_variation_sku (Union[Unset, None, str]):

    Returns:
        Response[Union[Any, Item]]
    """

    kwargs = _get_kwargs(
        client=client,
        fieldgroups=fieldgroups,
        legacy_item_id=legacy_item_id,
        legacy_variation_id=legacy_variation_id,
        legacy_variation_sku=legacy_variation_sku,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: AuthenticatedClient,
    fieldgroups: Union[Unset, None, str] = UNSET,
    legacy_item_id: str,
    legacy_variation_id: Union[Unset, None, str] = UNSET,
    legacy_variation_sku: Union[Unset, None, str] = UNSET,
) -> Optional[Union[Any, Item]]:
    """<p>This method is a bridge between the eBay legacy APIs, such as  <b> Shopping</b>, and <b>
    Finding</b> and the eBay Buy APIs. There are differences between how legacy APIs and RESTful APIs
    return the identifier of an \"item\" and what the item ID represents. This method lets you use the
    legacy item ids retrieve the details of a specific item, such as description, price, and other
    information the buyer needs to make a purchasing decision. It also returns the RESTful item ID,
    which you can use with all the Buy API  methods.</p>  <p>For more information about how to use
    legacy ids with the Buy APIs, see <a href=\"/api-docs/buy/static/api-browse.html#Legacy\">Legacy API
    compatibility</a> in the Buying Integration guide.</p>  <p>This method returns the item details and
    requires you to pass in either the item ID of a non-variation item or the item ids of both the
    parent and child of an item group. An item group is an item that has various aspect differences,
    such as color, size, storage capacity, etc.</p> <p>When an item group is created, one of the item
    variations, such as the red shirt size L, is chosen as the \"parent\". All the other items in the
    group are the children, such as the blue shirt size L, red shirt size M, etc.</p>    <p>The <b>
    fieldgroups</b> URI parameter lets you control what is returned in the response. Setting <b>
    fieldgroups</b> to <code>PRODUCT</code>, adds additional fields to the default response that return
    information about the product of the item. For more information, see <a href=\"/api-
    docs/buy/browse/resources/item/methods/getItemByLegacyItem#uri.fieldgroups\">fieldgroups</a>.</p>
    <h3>URLs for this method</h3>           <p><ul>            <li><b> Production URL: </b>
    <code>https://api.ebay.com/buy/browse/v1/item/get_item_by_legacy_id?</code></li>            <li><b>
    Sandbox URL:
    </b><code>https://api.sandbox.ebay.com/buy/browse/v1/item/get_item_by_legacy_id?</code></li>
    </ul>    </p>              <h3><b> Request headers</b></h3> This method uses the  <b>X-EBAY-C-
    ENDUSERCTX</b> request header to support revenue sharing for eBay Partner Networks and to improve
    the accuracy of shipping and delivery time estimations.   For details see, <a href=\"/api-
    docs/buy/static/api-browse.html#Headers\">Request headers</a> in the Buying Integration Guide.
    <h3><b> Restrictions </b></h3> <p>For a list of supported sites and other restrictions, see <a
    href=\"/api-docs/buy/browse/overview.html#API\">API Restrictions</a>.</p> <span
    class=\"tablenote\"><b>eBay Partner Network: </b> In order to be commissioned for your sales, you
    must use the URL returned in the <code>itemAffiliateWebUrl</code> field to forward your buyer to the
    ebay.com site. </span>

    Args:
        fieldgroups (Union[Unset, None, str]):
        legacy_item_id (str):
        legacy_variation_id (Union[Unset, None, str]):
        legacy_variation_sku (Union[Unset, None, str]):

    Returns:
        Response[Union[Any, Item]]
    """

    return sync_detailed(
        client=client,
        fieldgroups=fieldgroups,
        legacy_item_id=legacy_item_id,
        legacy_variation_id=legacy_variation_id,
        legacy_variation_sku=legacy_variation_sku,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    fieldgroups: Union[Unset, None, str] = UNSET,
    legacy_item_id: str,
    legacy_variation_id: Union[Unset, None, str] = UNSET,
    legacy_variation_sku: Union[Unset, None, str] = UNSET,
) -> Response[Union[Any, Item]]:
    """<p>This method is a bridge between the eBay legacy APIs, such as  <b> Shopping</b>, and <b>
    Finding</b> and the eBay Buy APIs. There are differences between how legacy APIs and RESTful APIs
    return the identifier of an \"item\" and what the item ID represents. This method lets you use the
    legacy item ids retrieve the details of a specific item, such as description, price, and other
    information the buyer needs to make a purchasing decision. It also returns the RESTful item ID,
    which you can use with all the Buy API  methods.</p>  <p>For more information about how to use
    legacy ids with the Buy APIs, see <a href=\"/api-docs/buy/static/api-browse.html#Legacy\">Legacy API
    compatibility</a> in the Buying Integration guide.</p>  <p>This method returns the item details and
    requires you to pass in either the item ID of a non-variation item or the item ids of both the
    parent and child of an item group. An item group is an item that has various aspect differences,
    such as color, size, storage capacity, etc.</p> <p>When an item group is created, one of the item
    variations, such as the red shirt size L, is chosen as the \"parent\". All the other items in the
    group are the children, such as the blue shirt size L, red shirt size M, etc.</p>    <p>The <b>
    fieldgroups</b> URI parameter lets you control what is returned in the response. Setting <b>
    fieldgroups</b> to <code>PRODUCT</code>, adds additional fields to the default response that return
    information about the product of the item. For more information, see <a href=\"/api-
    docs/buy/browse/resources/item/methods/getItemByLegacyItem#uri.fieldgroups\">fieldgroups</a>.</p>
    <h3>URLs for this method</h3>           <p><ul>            <li><b> Production URL: </b>
    <code>https://api.ebay.com/buy/browse/v1/item/get_item_by_legacy_id?</code></li>            <li><b>
    Sandbox URL:
    </b><code>https://api.sandbox.ebay.com/buy/browse/v1/item/get_item_by_legacy_id?</code></li>
    </ul>    </p>              <h3><b> Request headers</b></h3> This method uses the  <b>X-EBAY-C-
    ENDUSERCTX</b> request header to support revenue sharing for eBay Partner Networks and to improve
    the accuracy of shipping and delivery time estimations.   For details see, <a href=\"/api-
    docs/buy/static/api-browse.html#Headers\">Request headers</a> in the Buying Integration Guide.
    <h3><b> Restrictions </b></h3> <p>For a list of supported sites and other restrictions, see <a
    href=\"/api-docs/buy/browse/overview.html#API\">API Restrictions</a>.</p> <span
    class=\"tablenote\"><b>eBay Partner Network: </b> In order to be commissioned for your sales, you
    must use the URL returned in the <code>itemAffiliateWebUrl</code> field to forward your buyer to the
    ebay.com site. </span>

    Args:
        fieldgroups (Union[Unset, None, str]):
        legacy_item_id (str):
        legacy_variation_id (Union[Unset, None, str]):
        legacy_variation_sku (Union[Unset, None, str]):

    Returns:
        Response[Union[Any, Item]]
    """

    kwargs = _get_kwargs(
        client=client,
        fieldgroups=fieldgroups,
        legacy_item_id=legacy_item_id,
        legacy_variation_id=legacy_variation_id,
        legacy_variation_sku=legacy_variation_sku,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    fieldgroups: Union[Unset, None, str] = UNSET,
    legacy_item_id: str,
    legacy_variation_id: Union[Unset, None, str] = UNSET,
    legacy_variation_sku: Union[Unset, None, str] = UNSET,
) -> Optional[Union[Any, Item]]:
    """<p>This method is a bridge between the eBay legacy APIs, such as  <b> Shopping</b>, and <b>
    Finding</b> and the eBay Buy APIs. There are differences between how legacy APIs and RESTful APIs
    return the identifier of an \"item\" and what the item ID represents. This method lets you use the
    legacy item ids retrieve the details of a specific item, such as description, price, and other
    information the buyer needs to make a purchasing decision. It also returns the RESTful item ID,
    which you can use with all the Buy API  methods.</p>  <p>For more information about how to use
    legacy ids with the Buy APIs, see <a href=\"/api-docs/buy/static/api-browse.html#Legacy\">Legacy API
    compatibility</a> in the Buying Integration guide.</p>  <p>This method returns the item details and
    requires you to pass in either the item ID of a non-variation item or the item ids of both the
    parent and child of an item group. An item group is an item that has various aspect differences,
    such as color, size, storage capacity, etc.</p> <p>When an item group is created, one of the item
    variations, such as the red shirt size L, is chosen as the \"parent\". All the other items in the
    group are the children, such as the blue shirt size L, red shirt size M, etc.</p>    <p>The <b>
    fieldgroups</b> URI parameter lets you control what is returned in the response. Setting <b>
    fieldgroups</b> to <code>PRODUCT</code>, adds additional fields to the default response that return
    information about the product of the item. For more information, see <a href=\"/api-
    docs/buy/browse/resources/item/methods/getItemByLegacyItem#uri.fieldgroups\">fieldgroups</a>.</p>
    <h3>URLs for this method</h3>           <p><ul>            <li><b> Production URL: </b>
    <code>https://api.ebay.com/buy/browse/v1/item/get_item_by_legacy_id?</code></li>            <li><b>
    Sandbox URL:
    </b><code>https://api.sandbox.ebay.com/buy/browse/v1/item/get_item_by_legacy_id?</code></li>
    </ul>    </p>              <h3><b> Request headers</b></h3> This method uses the  <b>X-EBAY-C-
    ENDUSERCTX</b> request header to support revenue sharing for eBay Partner Networks and to improve
    the accuracy of shipping and delivery time estimations.   For details see, <a href=\"/api-
    docs/buy/static/api-browse.html#Headers\">Request headers</a> in the Buying Integration Guide.
    <h3><b> Restrictions </b></h3> <p>For a list of supported sites and other restrictions, see <a
    href=\"/api-docs/buy/browse/overview.html#API\">API Restrictions</a>.</p> <span
    class=\"tablenote\"><b>eBay Partner Network: </b> In order to be commissioned for your sales, you
    must use the URL returned in the <code>itemAffiliateWebUrl</code> field to forward your buyer to the
    ebay.com site. </span>

    Args:
        fieldgroups (Union[Unset, None, str]):
        legacy_item_id (str):
        legacy_variation_id (Union[Unset, None, str]):
        legacy_variation_sku (Union[Unset, None, str]):

    Returns:
        Response[Union[Any, Item]]
    """

    return (
        await asyncio_detailed(
            client=client,
            fieldgroups=fieldgroups,
            legacy_item_id=legacy_item_id,
            legacy_variation_id=legacy_variation_id,
            legacy_variation_sku=legacy_variation_sku,
        )
    ).parsed
