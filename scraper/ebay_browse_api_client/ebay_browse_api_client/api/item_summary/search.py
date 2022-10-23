from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient
from ...models.search_paged_collection import SearchPagedCollection
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    aspect_filter: Union[Unset, None, str] = UNSET,
    auto_correct: Union[Unset, None, str] = UNSET,
    category_ids: Union[Unset, None, str] = UNSET,
    charity_ids: Union[Unset, None, str] = UNSET,
    compatibility_filter: Union[Unset, None, str] = UNSET,
    epid: Union[Unset, None, str] = UNSET,
    fieldgroups: Union[Unset, None, str] = UNSET,
    filter_: Union[Unset, None, str] = UNSET,
    gtin: Union[Unset, None, str] = UNSET,
    limit: Union[Unset, None, str] = UNSET,
    offset: Union[Unset, None, str] = UNSET,
    q: Union[Unset, None, str] = UNSET,
    sort: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/item_summary/search".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["aspect_filter"] = aspect_filter

    params["auto_correct"] = auto_correct

    params["category_ids"] = category_ids

    params["charity_ids"] = charity_ids

    params["compatibility_filter"] = compatibility_filter

    params["epid"] = epid

    params["fieldgroups"] = fieldgroups

    params["filter"] = filter_

    params["gtin"] = gtin

    params["limit"] = limit

    params["offset"] = offset

    params["q"] = q

    params["sort"] = sort

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, SearchPagedCollection]]:
    if response.status_code == 200:
        response_200 = SearchPagedCollection.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400
    if response.status_code == 409:
        response_409 = cast(Any, None)
        return response_409
    if response.status_code == 500:
        response_500 = cast(Any, None)
        return response_500
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Any, SearchPagedCollection]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    aspect_filter: Union[Unset, None, str] = UNSET,
    auto_correct: Union[Unset, None, str] = UNSET,
    category_ids: Union[Unset, None, str] = UNSET,
    charity_ids: Union[Unset, None, str] = UNSET,
    compatibility_filter: Union[Unset, None, str] = UNSET,
    epid: Union[Unset, None, str] = UNSET,
    fieldgroups: Union[Unset, None, str] = UNSET,
    filter_: Union[Unset, None, str] = UNSET,
    gtin: Union[Unset, None, str] = UNSET,
    limit: Union[Unset, None, str] = UNSET,
    offset: Union[Unset, None, str] = UNSET,
    q: Union[Unset, None, str] = UNSET,
    sort: Union[Unset, None, str] = UNSET,
) -> Response[Union[Any, SearchPagedCollection]]:
    """<p>This method searches for eBay items by various query parameters and retrieves summaries of the
    items. You can search by keyword, category, eBay product ID (ePID), or GTIN, charity ID, or a
    combination of these.</p><span class=\"tablenote\"><p><b>Note:</b> Only listings where FIXED_PRICE
    (Buy It Now) is a buying option are returned by default. To retrieve listings that do not have
    FIXED_PRICE as a buying option, the buyingOptions filter can be used to retrieve those
    listings.</p><p>Note that an auction listing enabled with the 'Buy it Now' feature will initially
    show AUCTION and FIXED_PRICE as buying options, but if/when that auction listing receives a
    qualifying bid, only AUCTION would remain as a buying option. If this happens, the buyingOptions
    filter would need to be used to retrieve that auction listing.</p></span><p>This method also
    supports the following:<ul><li>Filtering by the value of one or multiple fields, such as listing
    format, item condition, price range, location, and more. For the fields supported by this method,
    see the <a href=\"#uri.filter\">filter</a> parameter.</li><li>Retrieving the refinements (metadata)
    of an item , such as item aspects (color, brand), condition, category, etc. using the <a
    href=\"#uri.fieldgroups\">fieldgroups</a> parameter.</li><li>Filtering by item aspects and other
    refinements using the <a href=\"#uri.aspect_filter\">aspect_filter</a> parameter. </li>
    <li>Filtering for items that are compatible with a specific product, using the <a
    href=\"#uri.compatibility_filter\">compatibility_filter</a> parameter.</li><li>Creating aspects
    histograms, which enables shoppers to drill down in each refinement narrowing the search
    results.</li></ul></p><p>For details and examples of these capabilities, see <a href=\"/api-
    docs/buy/static/api-browse.html\">Browse API</a> in the Buying Integration Guide.</p><h3><b>
    Pagination and sort controls</b></h3><p>There are pagination controls (<b>limit</b> and
    <b>offset</b> fields) and <b> sort</b> query parameters that control/sort the data that is returned.
    By default, the results are sorted by &quot;Best Match&quot;. For more information about Best Match,
    see the eBay help page <a href=\"https://pages.ebay.com/help/sell/searchstanding.html \"
    target=\"_blank\">Best Match</a>.</p><h3><b>URLs for this method</b></h3><p><ul><li><b>Production
    URL:</b><code>https://api.ebay.com/buy/browse/v1/item_summary/search?</code></li><li><b>Sandbox URL:
    </b><code>https://api.sandbox.ebay.com/buy/browse/v1/item_summary/search?</code></li></ul></p><h3><b
    > Request headers</b></h3> This method uses the <b>X-EBAY-C-ENDUSERCTX</b> request header to support
    revenue sharing for eBay Partner Networks and to improve the accuracy of shipping and delivery time
    estimations. For details see, <a href=\"/api-docs/buy/static/api-browse.html#Headers\">Request
    headers</a> in the Buying Integration Guide.<h3><b>Restrictions </b></h3> <p>This method can return
    a maximum of 10,000 items. For a list of supported sites and other restrictions, see <a href=\"/api-
    docs/buy/browse/overview.html#API\">API Restrictions</a>.</p><span class=\"tablenote\"><b>eBay
    Partner Network:</b> In order to receive a commission for your sales, you must use the URL returned
    in the <code>itemAffiliateWebUrl</code> field to forward your buyer to the ebay.com site.</span>

    Args:
        aspect_filter (Union[Unset, None, str]):
        auto_correct (Union[Unset, None, str]):
        category_ids (Union[Unset, None, str]):
        charity_ids (Union[Unset, None, str]):
        compatibility_filter (Union[Unset, None, str]):
        epid (Union[Unset, None, str]):
        fieldgroups (Union[Unset, None, str]):
        filter_ (Union[Unset, None, str]):
        gtin (Union[Unset, None, str]):
        limit (Union[Unset, None, str]):
        offset (Union[Unset, None, str]):
        q (Union[Unset, None, str]):
        sort (Union[Unset, None, str]):

    Returns:
        Response[Union[Any, SearchPagedCollection]]
    """

    kwargs = _get_kwargs(
        client=client,
        aspect_filter=aspect_filter,
        auto_correct=auto_correct,
        category_ids=category_ids,
        charity_ids=charity_ids,
        compatibility_filter=compatibility_filter,
        epid=epid,
        fieldgroups=fieldgroups,
        filter_=filter_,
        gtin=gtin,
        limit=limit,
        offset=offset,
        q=q,
        sort=sort,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: AuthenticatedClient,
    aspect_filter: Union[Unset, None, str] = UNSET,
    auto_correct: Union[Unset, None, str] = UNSET,
    category_ids: Union[Unset, None, str] = UNSET,
    charity_ids: Union[Unset, None, str] = UNSET,
    compatibility_filter: Union[Unset, None, str] = UNSET,
    epid: Union[Unset, None, str] = UNSET,
    fieldgroups: Union[Unset, None, str] = UNSET,
    filter_: Union[Unset, None, str] = UNSET,
    gtin: Union[Unset, None, str] = UNSET,
    limit: Union[Unset, None, str] = UNSET,
    offset: Union[Unset, None, str] = UNSET,
    q: Union[Unset, None, str] = UNSET,
    sort: Union[Unset, None, str] = UNSET,
) -> Optional[Union[Any, SearchPagedCollection]]:
    """<p>This method searches for eBay items by various query parameters and retrieves summaries of the
    items. You can search by keyword, category, eBay product ID (ePID), or GTIN, charity ID, or a
    combination of these.</p><span class=\"tablenote\"><p><b>Note:</b> Only listings where FIXED_PRICE
    (Buy It Now) is a buying option are returned by default. To retrieve listings that do not have
    FIXED_PRICE as a buying option, the buyingOptions filter can be used to retrieve those
    listings.</p><p>Note that an auction listing enabled with the 'Buy it Now' feature will initially
    show AUCTION and FIXED_PRICE as buying options, but if/when that auction listing receives a
    qualifying bid, only AUCTION would remain as a buying option. If this happens, the buyingOptions
    filter would need to be used to retrieve that auction listing.</p></span><p>This method also
    supports the following:<ul><li>Filtering by the value of one or multiple fields, such as listing
    format, item condition, price range, location, and more. For the fields supported by this method,
    see the <a href=\"#uri.filter\">filter</a> parameter.</li><li>Retrieving the refinements (metadata)
    of an item , such as item aspects (color, brand), condition, category, etc. using the <a
    href=\"#uri.fieldgroups\">fieldgroups</a> parameter.</li><li>Filtering by item aspects and other
    refinements using the <a href=\"#uri.aspect_filter\">aspect_filter</a> parameter. </li>
    <li>Filtering for items that are compatible with a specific product, using the <a
    href=\"#uri.compatibility_filter\">compatibility_filter</a> parameter.</li><li>Creating aspects
    histograms, which enables shoppers to drill down in each refinement narrowing the search
    results.</li></ul></p><p>For details and examples of these capabilities, see <a href=\"/api-
    docs/buy/static/api-browse.html\">Browse API</a> in the Buying Integration Guide.</p><h3><b>
    Pagination and sort controls</b></h3><p>There are pagination controls (<b>limit</b> and
    <b>offset</b> fields) and <b> sort</b> query parameters that control/sort the data that is returned.
    By default, the results are sorted by &quot;Best Match&quot;. For more information about Best Match,
    see the eBay help page <a href=\"https://pages.ebay.com/help/sell/searchstanding.html \"
    target=\"_blank\">Best Match</a>.</p><h3><b>URLs for this method</b></h3><p><ul><li><b>Production
    URL:</b><code>https://api.ebay.com/buy/browse/v1/item_summary/search?</code></li><li><b>Sandbox URL:
    </b><code>https://api.sandbox.ebay.com/buy/browse/v1/item_summary/search?</code></li></ul></p><h3><b
    > Request headers</b></h3> This method uses the <b>X-EBAY-C-ENDUSERCTX</b> request header to support
    revenue sharing for eBay Partner Networks and to improve the accuracy of shipping and delivery time
    estimations. For details see, <a href=\"/api-docs/buy/static/api-browse.html#Headers\">Request
    headers</a> in the Buying Integration Guide.<h3><b>Restrictions </b></h3> <p>This method can return
    a maximum of 10,000 items. For a list of supported sites and other restrictions, see <a href=\"/api-
    docs/buy/browse/overview.html#API\">API Restrictions</a>.</p><span class=\"tablenote\"><b>eBay
    Partner Network:</b> In order to receive a commission for your sales, you must use the URL returned
    in the <code>itemAffiliateWebUrl</code> field to forward your buyer to the ebay.com site.</span>

    Args:
        aspect_filter (Union[Unset, None, str]):
        auto_correct (Union[Unset, None, str]):
        category_ids (Union[Unset, None, str]):
        charity_ids (Union[Unset, None, str]):
        compatibility_filter (Union[Unset, None, str]):
        epid (Union[Unset, None, str]):
        fieldgroups (Union[Unset, None, str]):
        filter_ (Union[Unset, None, str]):
        gtin (Union[Unset, None, str]):
        limit (Union[Unset, None, str]):
        offset (Union[Unset, None, str]):
        q (Union[Unset, None, str]):
        sort (Union[Unset, None, str]):

    Returns:
        Response[Union[Any, SearchPagedCollection]]
    """

    return sync_detailed(
        client=client,
        aspect_filter=aspect_filter,
        auto_correct=auto_correct,
        category_ids=category_ids,
        charity_ids=charity_ids,
        compatibility_filter=compatibility_filter,
        epid=epid,
        fieldgroups=fieldgroups,
        filter_=filter_,
        gtin=gtin,
        limit=limit,
        offset=offset,
        q=q,
        sort=sort,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    aspect_filter: Union[Unset, None, str] = UNSET,
    auto_correct: Union[Unset, None, str] = UNSET,
    category_ids: Union[Unset, None, str] = UNSET,
    charity_ids: Union[Unset, None, str] = UNSET,
    compatibility_filter: Union[Unset, None, str] = UNSET,
    epid: Union[Unset, None, str] = UNSET,
    fieldgroups: Union[Unset, None, str] = UNSET,
    filter_: Union[Unset, None, str] = UNSET,
    gtin: Union[Unset, None, str] = UNSET,
    limit: Union[Unset, None, str] = UNSET,
    offset: Union[Unset, None, str] = UNSET,
    q: Union[Unset, None, str] = UNSET,
    sort: Union[Unset, None, str] = UNSET,
) -> Response[Union[Any, SearchPagedCollection]]:
    """<p>This method searches for eBay items by various query parameters and retrieves summaries of the
    items. You can search by keyword, category, eBay product ID (ePID), or GTIN, charity ID, or a
    combination of these.</p><span class=\"tablenote\"><p><b>Note:</b> Only listings where FIXED_PRICE
    (Buy It Now) is a buying option are returned by default. To retrieve listings that do not have
    FIXED_PRICE as a buying option, the buyingOptions filter can be used to retrieve those
    listings.</p><p>Note that an auction listing enabled with the 'Buy it Now' feature will initially
    show AUCTION and FIXED_PRICE as buying options, but if/when that auction listing receives a
    qualifying bid, only AUCTION would remain as a buying option. If this happens, the buyingOptions
    filter would need to be used to retrieve that auction listing.</p></span><p>This method also
    supports the following:<ul><li>Filtering by the value of one or multiple fields, such as listing
    format, item condition, price range, location, and more. For the fields supported by this method,
    see the <a href=\"#uri.filter\">filter</a> parameter.</li><li>Retrieving the refinements (metadata)
    of an item , such as item aspects (color, brand), condition, category, etc. using the <a
    href=\"#uri.fieldgroups\">fieldgroups</a> parameter.</li><li>Filtering by item aspects and other
    refinements using the <a href=\"#uri.aspect_filter\">aspect_filter</a> parameter. </li>
    <li>Filtering for items that are compatible with a specific product, using the <a
    href=\"#uri.compatibility_filter\">compatibility_filter</a> parameter.</li><li>Creating aspects
    histograms, which enables shoppers to drill down in each refinement narrowing the search
    results.</li></ul></p><p>For details and examples of these capabilities, see <a href=\"/api-
    docs/buy/static/api-browse.html\">Browse API</a> in the Buying Integration Guide.</p><h3><b>
    Pagination and sort controls</b></h3><p>There are pagination controls (<b>limit</b> and
    <b>offset</b> fields) and <b> sort</b> query parameters that control/sort the data that is returned.
    By default, the results are sorted by &quot;Best Match&quot;. For more information about Best Match,
    see the eBay help page <a href=\"https://pages.ebay.com/help/sell/searchstanding.html \"
    target=\"_blank\">Best Match</a>.</p><h3><b>URLs for this method</b></h3><p><ul><li><b>Production
    URL:</b><code>https://api.ebay.com/buy/browse/v1/item_summary/search?</code></li><li><b>Sandbox URL:
    </b><code>https://api.sandbox.ebay.com/buy/browse/v1/item_summary/search?</code></li></ul></p><h3><b
    > Request headers</b></h3> This method uses the <b>X-EBAY-C-ENDUSERCTX</b> request header to support
    revenue sharing for eBay Partner Networks and to improve the accuracy of shipping and delivery time
    estimations. For details see, <a href=\"/api-docs/buy/static/api-browse.html#Headers\">Request
    headers</a> in the Buying Integration Guide.<h3><b>Restrictions </b></h3> <p>This method can return
    a maximum of 10,000 items. For a list of supported sites and other restrictions, see <a href=\"/api-
    docs/buy/browse/overview.html#API\">API Restrictions</a>.</p><span class=\"tablenote\"><b>eBay
    Partner Network:</b> In order to receive a commission for your sales, you must use the URL returned
    in the <code>itemAffiliateWebUrl</code> field to forward your buyer to the ebay.com site.</span>

    Args:
        aspect_filter (Union[Unset, None, str]):
        auto_correct (Union[Unset, None, str]):
        category_ids (Union[Unset, None, str]):
        charity_ids (Union[Unset, None, str]):
        compatibility_filter (Union[Unset, None, str]):
        epid (Union[Unset, None, str]):
        fieldgroups (Union[Unset, None, str]):
        filter_ (Union[Unset, None, str]):
        gtin (Union[Unset, None, str]):
        limit (Union[Unset, None, str]):
        offset (Union[Unset, None, str]):
        q (Union[Unset, None, str]):
        sort (Union[Unset, None, str]):

    Returns:
        Response[Union[Any, SearchPagedCollection]]
    """

    kwargs = _get_kwargs(
        client=client,
        aspect_filter=aspect_filter,
        auto_correct=auto_correct,
        category_ids=category_ids,
        charity_ids=charity_ids,
        compatibility_filter=compatibility_filter,
        epid=epid,
        fieldgroups=fieldgroups,
        filter_=filter_,
        gtin=gtin,
        limit=limit,
        offset=offset,
        q=q,
        sort=sort,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    aspect_filter: Union[Unset, None, str] = UNSET,
    auto_correct: Union[Unset, None, str] = UNSET,
    category_ids: Union[Unset, None, str] = UNSET,
    charity_ids: Union[Unset, None, str] = UNSET,
    compatibility_filter: Union[Unset, None, str] = UNSET,
    epid: Union[Unset, None, str] = UNSET,
    fieldgroups: Union[Unset, None, str] = UNSET,
    filter_: Union[Unset, None, str] = UNSET,
    gtin: Union[Unset, None, str] = UNSET,
    limit: Union[Unset, None, str] = UNSET,
    offset: Union[Unset, None, str] = UNSET,
    q: Union[Unset, None, str] = UNSET,
    sort: Union[Unset, None, str] = UNSET,
) -> Optional[Union[Any, SearchPagedCollection]]:
    """<p>This method searches for eBay items by various query parameters and retrieves summaries of the
    items. You can search by keyword, category, eBay product ID (ePID), or GTIN, charity ID, or a
    combination of these.</p><span class=\"tablenote\"><p><b>Note:</b> Only listings where FIXED_PRICE
    (Buy It Now) is a buying option are returned by default. To retrieve listings that do not have
    FIXED_PRICE as a buying option, the buyingOptions filter can be used to retrieve those
    listings.</p><p>Note that an auction listing enabled with the 'Buy it Now' feature will initially
    show AUCTION and FIXED_PRICE as buying options, but if/when that auction listing receives a
    qualifying bid, only AUCTION would remain as a buying option. If this happens, the buyingOptions
    filter would need to be used to retrieve that auction listing.</p></span><p>This method also
    supports the following:<ul><li>Filtering by the value of one or multiple fields, such as listing
    format, item condition, price range, location, and more. For the fields supported by this method,
    see the <a href=\"#uri.filter\">filter</a> parameter.</li><li>Retrieving the refinements (metadata)
    of an item , such as item aspects (color, brand), condition, category, etc. using the <a
    href=\"#uri.fieldgroups\">fieldgroups</a> parameter.</li><li>Filtering by item aspects and other
    refinements using the <a href=\"#uri.aspect_filter\">aspect_filter</a> parameter. </li>
    <li>Filtering for items that are compatible with a specific product, using the <a
    href=\"#uri.compatibility_filter\">compatibility_filter</a> parameter.</li><li>Creating aspects
    histograms, which enables shoppers to drill down in each refinement narrowing the search
    results.</li></ul></p><p>For details and examples of these capabilities, see <a href=\"/api-
    docs/buy/static/api-browse.html\">Browse API</a> in the Buying Integration Guide.</p><h3><b>
    Pagination and sort controls</b></h3><p>There are pagination controls (<b>limit</b> and
    <b>offset</b> fields) and <b> sort</b> query parameters that control/sort the data that is returned.
    By default, the results are sorted by &quot;Best Match&quot;. For more information about Best Match,
    see the eBay help page <a href=\"https://pages.ebay.com/help/sell/searchstanding.html \"
    target=\"_blank\">Best Match</a>.</p><h3><b>URLs for this method</b></h3><p><ul><li><b>Production
    URL:</b><code>https://api.ebay.com/buy/browse/v1/item_summary/search?</code></li><li><b>Sandbox URL:
    </b><code>https://api.sandbox.ebay.com/buy/browse/v1/item_summary/search?</code></li></ul></p><h3><b
    > Request headers</b></h3> This method uses the <b>X-EBAY-C-ENDUSERCTX</b> request header to support
    revenue sharing for eBay Partner Networks and to improve the accuracy of shipping and delivery time
    estimations. For details see, <a href=\"/api-docs/buy/static/api-browse.html#Headers\">Request
    headers</a> in the Buying Integration Guide.<h3><b>Restrictions </b></h3> <p>This method can return
    a maximum of 10,000 items. For a list of supported sites and other restrictions, see <a href=\"/api-
    docs/buy/browse/overview.html#API\">API Restrictions</a>.</p><span class=\"tablenote\"><b>eBay
    Partner Network:</b> In order to receive a commission for your sales, you must use the URL returned
    in the <code>itemAffiliateWebUrl</code> field to forward your buyer to the ebay.com site.</span>

    Args:
        aspect_filter (Union[Unset, None, str]):
        auto_correct (Union[Unset, None, str]):
        category_ids (Union[Unset, None, str]):
        charity_ids (Union[Unset, None, str]):
        compatibility_filter (Union[Unset, None, str]):
        epid (Union[Unset, None, str]):
        fieldgroups (Union[Unset, None, str]):
        filter_ (Union[Unset, None, str]):
        gtin (Union[Unset, None, str]):
        limit (Union[Unset, None, str]):
        offset (Union[Unset, None, str]):
        q (Union[Unset, None, str]):
        sort (Union[Unset, None, str]):

    Returns:
        Response[Union[Any, SearchPagedCollection]]
    """

    return (
        await asyncio_detailed(
            client=client,
            aspect_filter=aspect_filter,
            auto_correct=auto_correct,
            category_ids=category_ids,
            charity_ids=charity_ids,
            compatibility_filter=compatibility_filter,
            epid=epid,
            fieldgroups=fieldgroups,
            filter_=filter_,
            gtin=gtin,
            limit=limit,
            offset=offset,
            q=q,
            sort=sort,
        )
    ).parsed
