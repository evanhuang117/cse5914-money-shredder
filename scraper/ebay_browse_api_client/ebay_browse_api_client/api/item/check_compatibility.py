from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient
from ...models.compatibility_payload import CompatibilityPayload
from ...models.compatibility_response import CompatibilityResponse
from ...types import Response


def _get_kwargs(
    item_id: str,
    *,
    client: AuthenticatedClient,
    json_body: CompatibilityPayload,
    x_ebay_c_marketplace_id: str,
) -> Dict[str, Any]:
    url = "{}/item/{item_id}/check_compatibility".format(client.base_url, item_id=item_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    headers["X-EBAY-C-MARKETPLACE-ID"] = x_ebay_c_marketplace_id

    json_json_body = json_body.to_dict()

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, CompatibilityResponse]]:
    if response.status_code == 200:
        response_200 = CompatibilityResponse.from_dict(response.json())

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


def _build_response(*, response: httpx.Response) -> Response[Union[Any, CompatibilityResponse]]:
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
    json_body: CompatibilityPayload,
    x_ebay_c_marketplace_id: str,
) -> Response[Union[Any, CompatibilityResponse]]:
    """This method checks if a product is compatible with the specified item. You can use this method to
    check the compatibility of cars, trucks, and motorcycles with a specific part listed on eBay. <br
    /><br />For example, to check the compatibility of a part, you pass in the item ID of the part as a
    URI parameter and specify all the attributes used to define a specific car in the <b>
    compatibilityProperties</b> container. If the call is successful, the response will be <b>
    COMPATIBLE</b>, <b> NOT_COMPATIBLE</b>, or <b> UNDETERMINED</b>. See <a href=\"/api-docs/buy/browse/
    resources/item/methods/checkCompatibility#response.compatibilityStatus\">compatibilityStatus</a> for
    details.   <br /><br /> <span class=\"tablenote\"><b> Note: </b> The only products supported are
    cars, trucks, and motorcycles. </span><p>  To find the attributes and values for a specific
    marketplace, you can use the compatibility methods in the <a href=\"/api-
    docs/commerce/taxonomy/resources/methods\">Taxonomy API</a>. You can use this data to create menus
    to help buyers specify the product, such as their car.</p> <p> For more details and a list of the
    required attributes for the US marketplace that describe motor vehicles, see <a href=\"/api-
    docs/buy/static/api-browse.html#Check\">Check compatibility</a> in the Buy Integration
    Guide</a>.</p>   <p>For an example, see the <a href=\"/api-
    docs/buy/browse/resources/item/methods/checkCompatibility#h2-samples\">Samples</a> section. </p>
    <h3>URLs for this method</h3>  <p><b> Production URL: </b>
    <code>https://api.ebay.com/buy/browse/v1/item/{item_id}/check_compatibility</code> </p>
    <p><span class=\"tablenote\"><b> Note: </b> This method is supported only on Production. </span></p>
    <h3><b> Restrictions </b></h3> <p>For a list of supported sites and other restrictions, see <a
    href=\"/api-docs/buy/browse/overview.html#API\">API Restrictions</a>.</p>

    Args:
        item_id (str):
        x_ebay_c_marketplace_id (str):
        json_body (CompatibilityPayload): An array of attribute name/value pairs used to define a
            specific product. For example: If you wanted to specify a specific car, one of the
            name/value pairs would be <br /><code>"name" : "Year", <br />"value" : "2019"</code>  <p>
            For a list of the attributes required for cars and trucks and motorcycles see <a
            href="/api-docs/buy/static/api-browse.html#Check">Check compatibility</a> in the Buy
            Integration Guide.</p>

    Returns:
        Response[Union[Any, CompatibilityResponse]]
    """

    kwargs = _get_kwargs(
        item_id=item_id,
        client=client,
        json_body=json_body,
        x_ebay_c_marketplace_id=x_ebay_c_marketplace_id,
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
    json_body: CompatibilityPayload,
    x_ebay_c_marketplace_id: str,
) -> Optional[Union[Any, CompatibilityResponse]]:
    """This method checks if a product is compatible with the specified item. You can use this method to
    check the compatibility of cars, trucks, and motorcycles with a specific part listed on eBay. <br
    /><br />For example, to check the compatibility of a part, you pass in the item ID of the part as a
    URI parameter and specify all the attributes used to define a specific car in the <b>
    compatibilityProperties</b> container. If the call is successful, the response will be <b>
    COMPATIBLE</b>, <b> NOT_COMPATIBLE</b>, or <b> UNDETERMINED</b>. See <a href=\"/api-docs/buy/browse/
    resources/item/methods/checkCompatibility#response.compatibilityStatus\">compatibilityStatus</a> for
    details.   <br /><br /> <span class=\"tablenote\"><b> Note: </b> The only products supported are
    cars, trucks, and motorcycles. </span><p>  To find the attributes and values for a specific
    marketplace, you can use the compatibility methods in the <a href=\"/api-
    docs/commerce/taxonomy/resources/methods\">Taxonomy API</a>. You can use this data to create menus
    to help buyers specify the product, such as their car.</p> <p> For more details and a list of the
    required attributes for the US marketplace that describe motor vehicles, see <a href=\"/api-
    docs/buy/static/api-browse.html#Check\">Check compatibility</a> in the Buy Integration
    Guide</a>.</p>   <p>For an example, see the <a href=\"/api-
    docs/buy/browse/resources/item/methods/checkCompatibility#h2-samples\">Samples</a> section. </p>
    <h3>URLs for this method</h3>  <p><b> Production URL: </b>
    <code>https://api.ebay.com/buy/browse/v1/item/{item_id}/check_compatibility</code> </p>
    <p><span class=\"tablenote\"><b> Note: </b> This method is supported only on Production. </span></p>
    <h3><b> Restrictions </b></h3> <p>For a list of supported sites and other restrictions, see <a
    href=\"/api-docs/buy/browse/overview.html#API\">API Restrictions</a>.</p>

    Args:
        item_id (str):
        x_ebay_c_marketplace_id (str):
        json_body (CompatibilityPayload): An array of attribute name/value pairs used to define a
            specific product. For example: If you wanted to specify a specific car, one of the
            name/value pairs would be <br /><code>"name" : "Year", <br />"value" : "2019"</code>  <p>
            For a list of the attributes required for cars and trucks and motorcycles see <a
            href="/api-docs/buy/static/api-browse.html#Check">Check compatibility</a> in the Buy
            Integration Guide.</p>

    Returns:
        Response[Union[Any, CompatibilityResponse]]
    """

    return sync_detailed(
        item_id=item_id,
        client=client,
        json_body=json_body,
        x_ebay_c_marketplace_id=x_ebay_c_marketplace_id,
    ).parsed


async def asyncio_detailed(
    item_id: str,
    *,
    client: AuthenticatedClient,
    json_body: CompatibilityPayload,
    x_ebay_c_marketplace_id: str,
) -> Response[Union[Any, CompatibilityResponse]]:
    """This method checks if a product is compatible with the specified item. You can use this method to
    check the compatibility of cars, trucks, and motorcycles with a specific part listed on eBay. <br
    /><br />For example, to check the compatibility of a part, you pass in the item ID of the part as a
    URI parameter and specify all the attributes used to define a specific car in the <b>
    compatibilityProperties</b> container. If the call is successful, the response will be <b>
    COMPATIBLE</b>, <b> NOT_COMPATIBLE</b>, or <b> UNDETERMINED</b>. See <a href=\"/api-docs/buy/browse/
    resources/item/methods/checkCompatibility#response.compatibilityStatus\">compatibilityStatus</a> for
    details.   <br /><br /> <span class=\"tablenote\"><b> Note: </b> The only products supported are
    cars, trucks, and motorcycles. </span><p>  To find the attributes and values for a specific
    marketplace, you can use the compatibility methods in the <a href=\"/api-
    docs/commerce/taxonomy/resources/methods\">Taxonomy API</a>. You can use this data to create menus
    to help buyers specify the product, such as their car.</p> <p> For more details and a list of the
    required attributes for the US marketplace that describe motor vehicles, see <a href=\"/api-
    docs/buy/static/api-browse.html#Check\">Check compatibility</a> in the Buy Integration
    Guide</a>.</p>   <p>For an example, see the <a href=\"/api-
    docs/buy/browse/resources/item/methods/checkCompatibility#h2-samples\">Samples</a> section. </p>
    <h3>URLs for this method</h3>  <p><b> Production URL: </b>
    <code>https://api.ebay.com/buy/browse/v1/item/{item_id}/check_compatibility</code> </p>
    <p><span class=\"tablenote\"><b> Note: </b> This method is supported only on Production. </span></p>
    <h3><b> Restrictions </b></h3> <p>For a list of supported sites and other restrictions, see <a
    href=\"/api-docs/buy/browse/overview.html#API\">API Restrictions</a>.</p>

    Args:
        item_id (str):
        x_ebay_c_marketplace_id (str):
        json_body (CompatibilityPayload): An array of attribute name/value pairs used to define a
            specific product. For example: If you wanted to specify a specific car, one of the
            name/value pairs would be <br /><code>"name" : "Year", <br />"value" : "2019"</code>  <p>
            For a list of the attributes required for cars and trucks and motorcycles see <a
            href="/api-docs/buy/static/api-browse.html#Check">Check compatibility</a> in the Buy
            Integration Guide.</p>

    Returns:
        Response[Union[Any, CompatibilityResponse]]
    """

    kwargs = _get_kwargs(
        item_id=item_id,
        client=client,
        json_body=json_body,
        x_ebay_c_marketplace_id=x_ebay_c_marketplace_id,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    item_id: str,
    *,
    client: AuthenticatedClient,
    json_body: CompatibilityPayload,
    x_ebay_c_marketplace_id: str,
) -> Optional[Union[Any, CompatibilityResponse]]:
    """This method checks if a product is compatible with the specified item. You can use this method to
    check the compatibility of cars, trucks, and motorcycles with a specific part listed on eBay. <br
    /><br />For example, to check the compatibility of a part, you pass in the item ID of the part as a
    URI parameter and specify all the attributes used to define a specific car in the <b>
    compatibilityProperties</b> container. If the call is successful, the response will be <b>
    COMPATIBLE</b>, <b> NOT_COMPATIBLE</b>, or <b> UNDETERMINED</b>. See <a href=\"/api-docs/buy/browse/
    resources/item/methods/checkCompatibility#response.compatibilityStatus\">compatibilityStatus</a> for
    details.   <br /><br /> <span class=\"tablenote\"><b> Note: </b> The only products supported are
    cars, trucks, and motorcycles. </span><p>  To find the attributes and values for a specific
    marketplace, you can use the compatibility methods in the <a href=\"/api-
    docs/commerce/taxonomy/resources/methods\">Taxonomy API</a>. You can use this data to create menus
    to help buyers specify the product, such as their car.</p> <p> For more details and a list of the
    required attributes for the US marketplace that describe motor vehicles, see <a href=\"/api-
    docs/buy/static/api-browse.html#Check\">Check compatibility</a> in the Buy Integration
    Guide</a>.</p>   <p>For an example, see the <a href=\"/api-
    docs/buy/browse/resources/item/methods/checkCompatibility#h2-samples\">Samples</a> section. </p>
    <h3>URLs for this method</h3>  <p><b> Production URL: </b>
    <code>https://api.ebay.com/buy/browse/v1/item/{item_id}/check_compatibility</code> </p>
    <p><span class=\"tablenote\"><b> Note: </b> This method is supported only on Production. </span></p>
    <h3><b> Restrictions </b></h3> <p>For a list of supported sites and other restrictions, see <a
    href=\"/api-docs/buy/browse/overview.html#API\">API Restrictions</a>.</p>

    Args:
        item_id (str):
        x_ebay_c_marketplace_id (str):
        json_body (CompatibilityPayload): An array of attribute name/value pairs used to define a
            specific product. For example: If you wanted to specify a specific car, one of the
            name/value pairs would be <br /><code>"name" : "Year", <br />"value" : "2019"</code>  <p>
            For a list of the attributes required for cars and trucks and motorcycles see <a
            href="/api-docs/buy/static/api-browse.html#Check">Check compatibility</a> in the Buy
            Integration Guide.</p>

    Returns:
        Response[Union[Any, CompatibilityResponse]]
    """

    return (
        await asyncio_detailed(
            item_id=item_id,
            client=client,
            json_body=json_body,
            x_ebay_c_marketplace_id=x_ebay_c_marketplace_id,
        )
    ).parsed
