from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient
from ...models.items import Items
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    item_ids: Union[Unset, None, str] = UNSET,
    item_group_ids: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/item/".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["item_ids"] = item_ids

    params["item_group_ids"] = item_group_ids

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, Items]]:
    if response.status_code == 200:
        response_200 = Items.from_dict(response.json())

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


def _build_response(*, response: httpx.Response) -> Response[Union[Any, Items]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    item_ids: Union[Unset, None, str] = UNSET,
    item_group_ids: Union[Unset, None, str] = UNSET,
) -> Response[Union[Any, Items]]:
    """This method retrieves the details of specific items that the buyer needs to make a purchasing
    decision.  <br><br><span class=\"tablenote\"> <b>Note:</b> This is a <a
    href=\"https://developer.ebay.com/api-docs/static/versioning.html#limited \" target=\"_blank\"> <img
    src=\"/cms/img/docs/partners-api.svg\" class=\"legend-icon partners-icon\" title=\"Limited Release\"
    alt=\"Limited Release\" />(Limited Release)</a> available only to select Partners. <br><br>For this
    method, only the following fields are returned: <code>bidCount</code>, <code>currentBidPrice</code>,
    <code>eligibleForInlineCheckout</code>, <code>enabledForGuestCheckout</code>,
    <code>estimatedAvailabilities</code>, <code>itemAffiliateWebUrl</code>,
    <code>itemCreationDate</code>, <code>itemId</code>, <code>itemWebUrl</code>,
    <code>legacyItemId</code>, <code>minimumPriceToBid</code>, <code>price</code>,
    <code>priorityListing</code>, <code>reservePriceMet</code>, <code>sellerItemRevision</code>,
    <code>taxes</code>, <code>topRatedBuyingExperience</code>, and <code>uniqueBidderCount</code>.<br
    /><br />The array <code>shippingOptions</code>, which comprises multiple fields, is also
    returned.</span> <h3>URLs for this method</h3>           <p><ul>            <li><b> Production URL:
    </b> <code>https://api.ebay.com/buy/browse/v1/item?</code></li>            <li><b> Sandbox URL:
    </b><code>https://api.sandbox.ebay.com/buy/browse/v1/item?</code></li>           </ul>    </p>
    <h3><b> Request headers</b></h3> This method uses the  <b>X-EBAY-C-ENDUSERCTX</b> request header to
    support revenue sharing for eBay Partner Networks and to improve the accuracy of shipping and
    delivery time estimations.   For details see, <a href=\"/api-docs/buy/static/api-
    browse.html#Headers\">Request headers</a> in the Buying Integration Guide.   <h3><b> Restrictions
    </b></h3> <p>For a list of supported sites and other restrictions, see <a href=\"/api-
    docs/buy/browse/overview.html#API\">API Restrictions</a>.</p> <span class=\"tablenote\"><b>eBay
    Partner Network:</b> In order to be commissioned for your sales, you must use the URL returned in
    the itemAffiliateWebUrl field to forward your buyer to the ebay.com site.

    Args:
        item_ids (Union[Unset, None, str]):
        item_group_ids (Union[Unset, None, str]):

    Returns:
        Response[Union[Any, Items]]
    """

    kwargs = _get_kwargs(
        client=client,
        item_ids=item_ids,
        item_group_ids=item_group_ids,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: AuthenticatedClient,
    item_ids: Union[Unset, None, str] = UNSET,
    item_group_ids: Union[Unset, None, str] = UNSET,
) -> Optional[Union[Any, Items]]:
    """This method retrieves the details of specific items that the buyer needs to make a purchasing
    decision.  <br><br><span class=\"tablenote\"> <b>Note:</b> This is a <a
    href=\"https://developer.ebay.com/api-docs/static/versioning.html#limited \" target=\"_blank\"> <img
    src=\"/cms/img/docs/partners-api.svg\" class=\"legend-icon partners-icon\" title=\"Limited Release\"
    alt=\"Limited Release\" />(Limited Release)</a> available only to select Partners. <br><br>For this
    method, only the following fields are returned: <code>bidCount</code>, <code>currentBidPrice</code>,
    <code>eligibleForInlineCheckout</code>, <code>enabledForGuestCheckout</code>,
    <code>estimatedAvailabilities</code>, <code>itemAffiliateWebUrl</code>,
    <code>itemCreationDate</code>, <code>itemId</code>, <code>itemWebUrl</code>,
    <code>legacyItemId</code>, <code>minimumPriceToBid</code>, <code>price</code>,
    <code>priorityListing</code>, <code>reservePriceMet</code>, <code>sellerItemRevision</code>,
    <code>taxes</code>, <code>topRatedBuyingExperience</code>, and <code>uniqueBidderCount</code>.<br
    /><br />The array <code>shippingOptions</code>, which comprises multiple fields, is also
    returned.</span> <h3>URLs for this method</h3>           <p><ul>            <li><b> Production URL:
    </b> <code>https://api.ebay.com/buy/browse/v1/item?</code></li>            <li><b> Sandbox URL:
    </b><code>https://api.sandbox.ebay.com/buy/browse/v1/item?</code></li>           </ul>    </p>
    <h3><b> Request headers</b></h3> This method uses the  <b>X-EBAY-C-ENDUSERCTX</b> request header to
    support revenue sharing for eBay Partner Networks and to improve the accuracy of shipping and
    delivery time estimations.   For details see, <a href=\"/api-docs/buy/static/api-
    browse.html#Headers\">Request headers</a> in the Buying Integration Guide.   <h3><b> Restrictions
    </b></h3> <p>For a list of supported sites and other restrictions, see <a href=\"/api-
    docs/buy/browse/overview.html#API\">API Restrictions</a>.</p> <span class=\"tablenote\"><b>eBay
    Partner Network:</b> In order to be commissioned for your sales, you must use the URL returned in
    the itemAffiliateWebUrl field to forward your buyer to the ebay.com site.

    Args:
        item_ids (Union[Unset, None, str]):
        item_group_ids (Union[Unset, None, str]):

    Returns:
        Response[Union[Any, Items]]
    """

    return sync_detailed(
        client=client,
        item_ids=item_ids,
        item_group_ids=item_group_ids,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    item_ids: Union[Unset, None, str] = UNSET,
    item_group_ids: Union[Unset, None, str] = UNSET,
) -> Response[Union[Any, Items]]:
    """This method retrieves the details of specific items that the buyer needs to make a purchasing
    decision.  <br><br><span class=\"tablenote\"> <b>Note:</b> This is a <a
    href=\"https://developer.ebay.com/api-docs/static/versioning.html#limited \" target=\"_blank\"> <img
    src=\"/cms/img/docs/partners-api.svg\" class=\"legend-icon partners-icon\" title=\"Limited Release\"
    alt=\"Limited Release\" />(Limited Release)</a> available only to select Partners. <br><br>For this
    method, only the following fields are returned: <code>bidCount</code>, <code>currentBidPrice</code>,
    <code>eligibleForInlineCheckout</code>, <code>enabledForGuestCheckout</code>,
    <code>estimatedAvailabilities</code>, <code>itemAffiliateWebUrl</code>,
    <code>itemCreationDate</code>, <code>itemId</code>, <code>itemWebUrl</code>,
    <code>legacyItemId</code>, <code>minimumPriceToBid</code>, <code>price</code>,
    <code>priorityListing</code>, <code>reservePriceMet</code>, <code>sellerItemRevision</code>,
    <code>taxes</code>, <code>topRatedBuyingExperience</code>, and <code>uniqueBidderCount</code>.<br
    /><br />The array <code>shippingOptions</code>, which comprises multiple fields, is also
    returned.</span> <h3>URLs for this method</h3>           <p><ul>            <li><b> Production URL:
    </b> <code>https://api.ebay.com/buy/browse/v1/item?</code></li>            <li><b> Sandbox URL:
    </b><code>https://api.sandbox.ebay.com/buy/browse/v1/item?</code></li>           </ul>    </p>
    <h3><b> Request headers</b></h3> This method uses the  <b>X-EBAY-C-ENDUSERCTX</b> request header to
    support revenue sharing for eBay Partner Networks and to improve the accuracy of shipping and
    delivery time estimations.   For details see, <a href=\"/api-docs/buy/static/api-
    browse.html#Headers\">Request headers</a> in the Buying Integration Guide.   <h3><b> Restrictions
    </b></h3> <p>For a list of supported sites and other restrictions, see <a href=\"/api-
    docs/buy/browse/overview.html#API\">API Restrictions</a>.</p> <span class=\"tablenote\"><b>eBay
    Partner Network:</b> In order to be commissioned for your sales, you must use the URL returned in
    the itemAffiliateWebUrl field to forward your buyer to the ebay.com site.

    Args:
        item_ids (Union[Unset, None, str]):
        item_group_ids (Union[Unset, None, str]):

    Returns:
        Response[Union[Any, Items]]
    """

    kwargs = _get_kwargs(
        client=client,
        item_ids=item_ids,
        item_group_ids=item_group_ids,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    item_ids: Union[Unset, None, str] = UNSET,
    item_group_ids: Union[Unset, None, str] = UNSET,
) -> Optional[Union[Any, Items]]:
    """This method retrieves the details of specific items that the buyer needs to make a purchasing
    decision.  <br><br><span class=\"tablenote\"> <b>Note:</b> This is a <a
    href=\"https://developer.ebay.com/api-docs/static/versioning.html#limited \" target=\"_blank\"> <img
    src=\"/cms/img/docs/partners-api.svg\" class=\"legend-icon partners-icon\" title=\"Limited Release\"
    alt=\"Limited Release\" />(Limited Release)</a> available only to select Partners. <br><br>For this
    method, only the following fields are returned: <code>bidCount</code>, <code>currentBidPrice</code>,
    <code>eligibleForInlineCheckout</code>, <code>enabledForGuestCheckout</code>,
    <code>estimatedAvailabilities</code>, <code>itemAffiliateWebUrl</code>,
    <code>itemCreationDate</code>, <code>itemId</code>, <code>itemWebUrl</code>,
    <code>legacyItemId</code>, <code>minimumPriceToBid</code>, <code>price</code>,
    <code>priorityListing</code>, <code>reservePriceMet</code>, <code>sellerItemRevision</code>,
    <code>taxes</code>, <code>topRatedBuyingExperience</code>, and <code>uniqueBidderCount</code>.<br
    /><br />The array <code>shippingOptions</code>, which comprises multiple fields, is also
    returned.</span> <h3>URLs for this method</h3>           <p><ul>            <li><b> Production URL:
    </b> <code>https://api.ebay.com/buy/browse/v1/item?</code></li>            <li><b> Sandbox URL:
    </b><code>https://api.sandbox.ebay.com/buy/browse/v1/item?</code></li>           </ul>    </p>
    <h3><b> Request headers</b></h3> This method uses the  <b>X-EBAY-C-ENDUSERCTX</b> request header to
    support revenue sharing for eBay Partner Networks and to improve the accuracy of shipping and
    delivery time estimations.   For details see, <a href=\"/api-docs/buy/static/api-
    browse.html#Headers\">Request headers</a> in the Buying Integration Guide.   <h3><b> Restrictions
    </b></h3> <p>For a list of supported sites and other restrictions, see <a href=\"/api-
    docs/buy/browse/overview.html#API\">API Restrictions</a>.</p> <span class=\"tablenote\"><b>eBay
    Partner Network:</b> In order to be commissioned for your sales, you must use the URL returned in
    the itemAffiliateWebUrl field to forward your buyer to the ebay.com site.

    Args:
        item_ids (Union[Unset, None, str]):
        item_group_ids (Union[Unset, None, str]):

    Returns:
        Response[Union[Any, Items]]
    """

    return (
        await asyncio_detailed(
            client=client,
            item_ids=item_ids,
            item_group_ids=item_group_ids,
        )
    ).parsed
