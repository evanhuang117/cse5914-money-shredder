from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient
from ...models.search_by_image_request import SearchByImageRequest
from ...models.search_paged_collection import SearchPagedCollection
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    json_body: SearchByImageRequest,
    aspect_filter: Union[Unset, None, str] = UNSET,
    category_ids: Union[Unset, None, str] = UNSET,
    charity_ids: Union[Unset, None, str] = UNSET,
    fieldgroups: Union[Unset, None, str] = UNSET,
    filter_: Union[Unset, None, str] = UNSET,
    limit: Union[Unset, None, str] = UNSET,
    offset: Union[Unset, None, str] = UNSET,
    sort: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/item_summary/search_by_image".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["aspect_filter"] = aspect_filter

    params["category_ids"] = category_ids

    params["charity_ids"] = charity_ids

    params["fieldgroups"] = fieldgroups

    params["filter"] = filter_

    params["limit"] = limit

    params["offset"] = offset

    params["sort"] = sort

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    json_json_body = json_body.to_dict()

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
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
    json_body: SearchByImageRequest,
    aspect_filter: Union[Unset, None, str] = UNSET,
    category_ids: Union[Unset, None, str] = UNSET,
    charity_ids: Union[Unset, None, str] = UNSET,
    fieldgroups: Union[Unset, None, str] = UNSET,
    filter_: Union[Unset, None, str] = UNSET,
    limit: Union[Unset, None, str] = UNSET,
    offset: Union[Unset, None, str] = UNSET,
    sort: Union[Unset, None, str] = UNSET,
) -> Response[Union[Any, SearchPagedCollection]]:
    """<img src=\"/cms/img/docs/experimental-icon.svg\" class=\"legend-icon experimental-icon\"
    alt=\"Experimental Release\" title=\"Experimental Release\">  This is an <a
    href=\"https://developer.ebay.com/api-docs/static/versioning.html#experimental \">Experimental</a>
    method. <p>This method searches for eBay items based on a image and retrieves summaries of the
    items. You pass in a Base64 image in the request payload and can refine the search by category, or
    eBay product ID (ePID), or a combination of these using URI parameters.  <br /><br />To get the
    Base64 image string, you can use sites such as <a href=\"https://codebeautify.org/image-to-
    base64-converter \" target=\"_blank\">https://codebeautify.org/image-to-base64-converter</a>.
    </p><p>This method also supports the following:  <ul> <li>Filtering by the value of one or multiple
    fields, such as listing format, item condition, price range, location, and more.  For the fields
    supported by this method, see the <a href=\"#uri.filter\">filter</a> parameter.</li><li>Filtering by
    item aspects using the <a href=\"#uri.aspect_filter\">aspect_filter</a> parameter. </li>  </ul></p>
    <p>For details and examples of these capabilities, see <a href=\"/api-docs/buy/static/api-
    browse.html\">Browse API</a> in the Buying Integration Guide.</p><h3><b>Pagination and sort
    controls</b></h3>  <p>There are pagination controls (<b>limit</b> and <b>offset</b> fields) and <b>
    sort</b> query parameters that control/sort the data that is returned. By default, the results are
    sorted by &quot;Best Match&quot;. For more information about  Best Match, see the eBay help page <a
    href=\"https://pages.ebay.com/help/sell/searchstanding.html \" target=\"_blank\">Best Match</a>.
    </p>    <h3><b> URLs for this method</b></h3><p><ul><li><b>Production URL:</b>
    <code>https://api.ebay.com/buy/browse/v1/item_summary/search_by_image?</code></li><li><b> Sandbox
    URL:  </b>Due to the data available, this method is not supported in the eBay Sandbox. To test your
    integration, use the Production URL.</li></ul></p><h3><b> Request headers</b></h3> This method uses
    the  <b>X-EBAY-C-ENDUSERCTX</b> request header to support revenue sharing for eBay Partner Networks
    and to improve the accuracy of shipping and delivery time estimations. For details see, <a
    href=\"/api-docs/buy/static/api-browse.html#Headers\">Request headers</a> in the Buying Integration
    Guide.   <h3><b>URL Encoding for Parameters</b></h3> <p>Query parameter values need to be URL
    encoded. For details, see <a href=\"/api-docs/static/rest-request-components.html#parameters\">URL
    encoding query parameter values</a>.  For readability, code examples in this document have not been
    URL encoded.</p>  <h3><b>Restrictions </b></h3> <p>This method can return a maximum of 10,000 items.
    For a list of supported sites and other restrictions, see <a href=\"/api-
    docs/buy/browse/overview.html#API\">API Restrictions</a>.</p> <span class=\"tablenote\"><b>eBay
    Partner Network: </b> In order to receive a commission for your sales, you must use the URL returned
    in the <code>itemAffiliateWebUrl</code> field to forward your buyer to the ebay.com site. </span>

    Args:
        aspect_filter (Union[Unset, None, str]):
        category_ids (Union[Unset, None, str]):
        charity_ids (Union[Unset, None, str]):
        fieldgroups (Union[Unset, None, str]):
        filter_ (Union[Unset, None, str]):
        limit (Union[Unset, None, str]):
        offset (Union[Unset, None, str]):
        sort (Union[Unset, None, str]):
        json_body (SearchByImageRequest): The type that defines the fields for the image
            information.

    Returns:
        Response[Union[Any, SearchPagedCollection]]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
        aspect_filter=aspect_filter,
        category_ids=category_ids,
        charity_ids=charity_ids,
        fieldgroups=fieldgroups,
        filter_=filter_,
        limit=limit,
        offset=offset,
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
    json_body: SearchByImageRequest,
    aspect_filter: Union[Unset, None, str] = UNSET,
    category_ids: Union[Unset, None, str] = UNSET,
    charity_ids: Union[Unset, None, str] = UNSET,
    fieldgroups: Union[Unset, None, str] = UNSET,
    filter_: Union[Unset, None, str] = UNSET,
    limit: Union[Unset, None, str] = UNSET,
    offset: Union[Unset, None, str] = UNSET,
    sort: Union[Unset, None, str] = UNSET,
) -> Optional[Union[Any, SearchPagedCollection]]:
    """<img src=\"/cms/img/docs/experimental-icon.svg\" class=\"legend-icon experimental-icon\"
    alt=\"Experimental Release\" title=\"Experimental Release\">  This is an <a
    href=\"https://developer.ebay.com/api-docs/static/versioning.html#experimental \">Experimental</a>
    method. <p>This method searches for eBay items based on a image and retrieves summaries of the
    items. You pass in a Base64 image in the request payload and can refine the search by category, or
    eBay product ID (ePID), or a combination of these using URI parameters.  <br /><br />To get the
    Base64 image string, you can use sites such as <a href=\"https://codebeautify.org/image-to-
    base64-converter \" target=\"_blank\">https://codebeautify.org/image-to-base64-converter</a>.
    </p><p>This method also supports the following:  <ul> <li>Filtering by the value of one or multiple
    fields, such as listing format, item condition, price range, location, and more.  For the fields
    supported by this method, see the <a href=\"#uri.filter\">filter</a> parameter.</li><li>Filtering by
    item aspects using the <a href=\"#uri.aspect_filter\">aspect_filter</a> parameter. </li>  </ul></p>
    <p>For details and examples of these capabilities, see <a href=\"/api-docs/buy/static/api-
    browse.html\">Browse API</a> in the Buying Integration Guide.</p><h3><b>Pagination and sort
    controls</b></h3>  <p>There are pagination controls (<b>limit</b> and <b>offset</b> fields) and <b>
    sort</b> query parameters that control/sort the data that is returned. By default, the results are
    sorted by &quot;Best Match&quot;. For more information about  Best Match, see the eBay help page <a
    href=\"https://pages.ebay.com/help/sell/searchstanding.html \" target=\"_blank\">Best Match</a>.
    </p>    <h3><b> URLs for this method</b></h3><p><ul><li><b>Production URL:</b>
    <code>https://api.ebay.com/buy/browse/v1/item_summary/search_by_image?</code></li><li><b> Sandbox
    URL:  </b>Due to the data available, this method is not supported in the eBay Sandbox. To test your
    integration, use the Production URL.</li></ul></p><h3><b> Request headers</b></h3> This method uses
    the  <b>X-EBAY-C-ENDUSERCTX</b> request header to support revenue sharing for eBay Partner Networks
    and to improve the accuracy of shipping and delivery time estimations. For details see, <a
    href=\"/api-docs/buy/static/api-browse.html#Headers\">Request headers</a> in the Buying Integration
    Guide.   <h3><b>URL Encoding for Parameters</b></h3> <p>Query parameter values need to be URL
    encoded. For details, see <a href=\"/api-docs/static/rest-request-components.html#parameters\">URL
    encoding query parameter values</a>.  For readability, code examples in this document have not been
    URL encoded.</p>  <h3><b>Restrictions </b></h3> <p>This method can return a maximum of 10,000 items.
    For a list of supported sites and other restrictions, see <a href=\"/api-
    docs/buy/browse/overview.html#API\">API Restrictions</a>.</p> <span class=\"tablenote\"><b>eBay
    Partner Network: </b> In order to receive a commission for your sales, you must use the URL returned
    in the <code>itemAffiliateWebUrl</code> field to forward your buyer to the ebay.com site. </span>

    Args:
        aspect_filter (Union[Unset, None, str]):
        category_ids (Union[Unset, None, str]):
        charity_ids (Union[Unset, None, str]):
        fieldgroups (Union[Unset, None, str]):
        filter_ (Union[Unset, None, str]):
        limit (Union[Unset, None, str]):
        offset (Union[Unset, None, str]):
        sort (Union[Unset, None, str]):
        json_body (SearchByImageRequest): The type that defines the fields for the image
            information.

    Returns:
        Response[Union[Any, SearchPagedCollection]]
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
        aspect_filter=aspect_filter,
        category_ids=category_ids,
        charity_ids=charity_ids,
        fieldgroups=fieldgroups,
        filter_=filter_,
        limit=limit,
        offset=offset,
        sort=sort,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    json_body: SearchByImageRequest,
    aspect_filter: Union[Unset, None, str] = UNSET,
    category_ids: Union[Unset, None, str] = UNSET,
    charity_ids: Union[Unset, None, str] = UNSET,
    fieldgroups: Union[Unset, None, str] = UNSET,
    filter_: Union[Unset, None, str] = UNSET,
    limit: Union[Unset, None, str] = UNSET,
    offset: Union[Unset, None, str] = UNSET,
    sort: Union[Unset, None, str] = UNSET,
) -> Response[Union[Any, SearchPagedCollection]]:
    """<img src=\"/cms/img/docs/experimental-icon.svg\" class=\"legend-icon experimental-icon\"
    alt=\"Experimental Release\" title=\"Experimental Release\">  This is an <a
    href=\"https://developer.ebay.com/api-docs/static/versioning.html#experimental \">Experimental</a>
    method. <p>This method searches for eBay items based on a image and retrieves summaries of the
    items. You pass in a Base64 image in the request payload and can refine the search by category, or
    eBay product ID (ePID), or a combination of these using URI parameters.  <br /><br />To get the
    Base64 image string, you can use sites such as <a href=\"https://codebeautify.org/image-to-
    base64-converter \" target=\"_blank\">https://codebeautify.org/image-to-base64-converter</a>.
    </p><p>This method also supports the following:  <ul> <li>Filtering by the value of one or multiple
    fields, such as listing format, item condition, price range, location, and more.  For the fields
    supported by this method, see the <a href=\"#uri.filter\">filter</a> parameter.</li><li>Filtering by
    item aspects using the <a href=\"#uri.aspect_filter\">aspect_filter</a> parameter. </li>  </ul></p>
    <p>For details and examples of these capabilities, see <a href=\"/api-docs/buy/static/api-
    browse.html\">Browse API</a> in the Buying Integration Guide.</p><h3><b>Pagination and sort
    controls</b></h3>  <p>There are pagination controls (<b>limit</b> and <b>offset</b> fields) and <b>
    sort</b> query parameters that control/sort the data that is returned. By default, the results are
    sorted by &quot;Best Match&quot;. For more information about  Best Match, see the eBay help page <a
    href=\"https://pages.ebay.com/help/sell/searchstanding.html \" target=\"_blank\">Best Match</a>.
    </p>    <h3><b> URLs for this method</b></h3><p><ul><li><b>Production URL:</b>
    <code>https://api.ebay.com/buy/browse/v1/item_summary/search_by_image?</code></li><li><b> Sandbox
    URL:  </b>Due to the data available, this method is not supported in the eBay Sandbox. To test your
    integration, use the Production URL.</li></ul></p><h3><b> Request headers</b></h3> This method uses
    the  <b>X-EBAY-C-ENDUSERCTX</b> request header to support revenue sharing for eBay Partner Networks
    and to improve the accuracy of shipping and delivery time estimations. For details see, <a
    href=\"/api-docs/buy/static/api-browse.html#Headers\">Request headers</a> in the Buying Integration
    Guide.   <h3><b>URL Encoding for Parameters</b></h3> <p>Query parameter values need to be URL
    encoded. For details, see <a href=\"/api-docs/static/rest-request-components.html#parameters\">URL
    encoding query parameter values</a>.  For readability, code examples in this document have not been
    URL encoded.</p>  <h3><b>Restrictions </b></h3> <p>This method can return a maximum of 10,000 items.
    For a list of supported sites and other restrictions, see <a href=\"/api-
    docs/buy/browse/overview.html#API\">API Restrictions</a>.</p> <span class=\"tablenote\"><b>eBay
    Partner Network: </b> In order to receive a commission for your sales, you must use the URL returned
    in the <code>itemAffiliateWebUrl</code> field to forward your buyer to the ebay.com site. </span>

    Args:
        aspect_filter (Union[Unset, None, str]):
        category_ids (Union[Unset, None, str]):
        charity_ids (Union[Unset, None, str]):
        fieldgroups (Union[Unset, None, str]):
        filter_ (Union[Unset, None, str]):
        limit (Union[Unset, None, str]):
        offset (Union[Unset, None, str]):
        sort (Union[Unset, None, str]):
        json_body (SearchByImageRequest): The type that defines the fields for the image
            information.

    Returns:
        Response[Union[Any, SearchPagedCollection]]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
        aspect_filter=aspect_filter,
        category_ids=category_ids,
        charity_ids=charity_ids,
        fieldgroups=fieldgroups,
        filter_=filter_,
        limit=limit,
        offset=offset,
        sort=sort,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    json_body: SearchByImageRequest,
    aspect_filter: Union[Unset, None, str] = UNSET,
    category_ids: Union[Unset, None, str] = UNSET,
    charity_ids: Union[Unset, None, str] = UNSET,
    fieldgroups: Union[Unset, None, str] = UNSET,
    filter_: Union[Unset, None, str] = UNSET,
    limit: Union[Unset, None, str] = UNSET,
    offset: Union[Unset, None, str] = UNSET,
    sort: Union[Unset, None, str] = UNSET,
) -> Optional[Union[Any, SearchPagedCollection]]:
    """<img src=\"/cms/img/docs/experimental-icon.svg\" class=\"legend-icon experimental-icon\"
    alt=\"Experimental Release\" title=\"Experimental Release\">  This is an <a
    href=\"https://developer.ebay.com/api-docs/static/versioning.html#experimental \">Experimental</a>
    method. <p>This method searches for eBay items based on a image and retrieves summaries of the
    items. You pass in a Base64 image in the request payload and can refine the search by category, or
    eBay product ID (ePID), or a combination of these using URI parameters.  <br /><br />To get the
    Base64 image string, you can use sites such as <a href=\"https://codebeautify.org/image-to-
    base64-converter \" target=\"_blank\">https://codebeautify.org/image-to-base64-converter</a>.
    </p><p>This method also supports the following:  <ul> <li>Filtering by the value of one or multiple
    fields, such as listing format, item condition, price range, location, and more.  For the fields
    supported by this method, see the <a href=\"#uri.filter\">filter</a> parameter.</li><li>Filtering by
    item aspects using the <a href=\"#uri.aspect_filter\">aspect_filter</a> parameter. </li>  </ul></p>
    <p>For details and examples of these capabilities, see <a href=\"/api-docs/buy/static/api-
    browse.html\">Browse API</a> in the Buying Integration Guide.</p><h3><b>Pagination and sort
    controls</b></h3>  <p>There are pagination controls (<b>limit</b> and <b>offset</b> fields) and <b>
    sort</b> query parameters that control/sort the data that is returned. By default, the results are
    sorted by &quot;Best Match&quot;. For more information about  Best Match, see the eBay help page <a
    href=\"https://pages.ebay.com/help/sell/searchstanding.html \" target=\"_blank\">Best Match</a>.
    </p>    <h3><b> URLs for this method</b></h3><p><ul><li><b>Production URL:</b>
    <code>https://api.ebay.com/buy/browse/v1/item_summary/search_by_image?</code></li><li><b> Sandbox
    URL:  </b>Due to the data available, this method is not supported in the eBay Sandbox. To test your
    integration, use the Production URL.</li></ul></p><h3><b> Request headers</b></h3> This method uses
    the  <b>X-EBAY-C-ENDUSERCTX</b> request header to support revenue sharing for eBay Partner Networks
    and to improve the accuracy of shipping and delivery time estimations. For details see, <a
    href=\"/api-docs/buy/static/api-browse.html#Headers\">Request headers</a> in the Buying Integration
    Guide.   <h3><b>URL Encoding for Parameters</b></h3> <p>Query parameter values need to be URL
    encoded. For details, see <a href=\"/api-docs/static/rest-request-components.html#parameters\">URL
    encoding query parameter values</a>.  For readability, code examples in this document have not been
    URL encoded.</p>  <h3><b>Restrictions </b></h3> <p>This method can return a maximum of 10,000 items.
    For a list of supported sites and other restrictions, see <a href=\"/api-
    docs/buy/browse/overview.html#API\">API Restrictions</a>.</p> <span class=\"tablenote\"><b>eBay
    Partner Network: </b> In order to receive a commission for your sales, you must use the URL returned
    in the <code>itemAffiliateWebUrl</code> field to forward your buyer to the ebay.com site. </span>

    Args:
        aspect_filter (Union[Unset, None, str]):
        category_ids (Union[Unset, None, str]):
        charity_ids (Union[Unset, None, str]):
        fieldgroups (Union[Unset, None, str]):
        filter_ (Union[Unset, None, str]):
        limit (Union[Unset, None, str]):
        offset (Union[Unset, None, str]):
        sort (Union[Unset, None, str]):
        json_body (SearchByImageRequest): The type that defines the fields for the image
            information.

    Returns:
        Response[Union[Any, SearchPagedCollection]]
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
            aspect_filter=aspect_filter,
            category_ids=category_ids,
            charity_ids=charity_ids,
            fieldgroups=fieldgroups,
            filter_=filter_,
            limit=limit,
            offset=offset,
            sort=sort,
        )
    ).parsed
