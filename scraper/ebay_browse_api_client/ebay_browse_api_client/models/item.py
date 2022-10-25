from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.addon_service import AddonService
from ..models.address import Address
from ..models.authenticity_guarantee_program import AuthenticityGuaranteeProgram
from ..models.authenticity_verification_program import AuthenticityVerificationProgram
from ..models.available_coupon import AvailableCoupon
from ..models.converted_amount import ConvertedAmount
from ..models.error import Error
from ..models.estimated_availability import EstimatedAvailability
from ..models.image import Image
from ..models.item_group_summary import ItemGroupSummary
from ..models.item_return_terms import ItemReturnTerms
from ..models.marketing_price import MarketingPrice
from ..models.payment_method import PaymentMethod
from ..models.product import Product
from ..models.review_rating import ReviewRating
from ..models.seller_custom_policy import SellerCustomPolicy
from ..models.seller_detail import SellerDetail
from ..models.ship_to_locations import ShipToLocations
from ..models.shipping_option import ShippingOption
from ..models.taxes import Taxes
from ..models.typed_name_value import TypedNameValue
from ..types import UNSET, Unset

T = TypeVar("T", bound="Item")


@attr.s(auto_attribs=True)
class Item:
    """The details of an item that can be purchased.

    Attributes:
        additional_images (Union[Unset, List[Image]]): An array of containers with the URLs for the images that are in
            addition to the primary image.  The primary image is returned in the <b> image.imageUrl</b> field.
        addon_services (Union[Unset, List[AddonService]]): A list of add-on services that may be selected for the item
            or that may apply automatically.
        adult_only (Union[Unset, bool]): This indicates if the item is for  adults only. For more information about
            adult-only items on eBay, see <a href="https://pages.ebay.com/help/policies/adult-only.html "
            target="_blank">Adult items policy</a> for sellers and <a href="https://www.ebay.com/help/terms-
            conditions/default/searching-adult-items?id=4661" target="_blank">Adult-Only items on eBay</a> for buyers.
        age_group (Union[Unset, str]): (Primary Item Aspect) The age group for which the product is recommended. For
            example, newborn, infant, toddler, kids, adult, etc. All the item aspects, including this aspect, are returned
            in the <b> localizedAspects</b> container.
        authenticity_guarantee (Union[Unset, AuthenticityGuaranteeProgram]): A type that identifies whether the item is
            qualified for the Authenticity Guarantee program.
        authenticity_verification (Union[Unset, AuthenticityVerificationProgram]): A type that identifies whether the
            item is from a verified seller.
        available_coupons (Union[Unset, List[AvailableCoupon]]): A list of available coupons for the item.
        bid_count (Union[Unset, int]): This integer value indicates the total number of bids that have been placed
            against an auction item. This field is returned only for auction items.
        brand (Union[Unset, str]): (Primary Item Aspect) The name brand of the item, such as Nike, Apple, etc.  All the
            item aspects, including this aspect, are returned in the <b> localizedAspects</b> container.
        buying_options (Union[Unset, List[str]]): A comma separated list of all the purchase options available for the
            item. The values returned are:<ul><li><code>FIXED_PRICE</code> - Indicates the buyer can purchase the item for a
            set price using the Buy It Now button.</li><li><code>AUCTION</code> - Indicates the buyer can place a bid for
            the item. After the first bid is placed, this becomes a live auction item and is the only buying option for this
            item.</li><li><code>BEST_OFFER</code> - Indicates the buyer can send the seller a price they're willing to pay
            for the item. The seller can accept, reject, or send a counter offer. For more information on how this works,
            see <a href="https://www.ebay.com/help/buying/buy-now/making-best-offer?id=4019 ">Making a Best
            Offer</a>.</li><li><code>CLASSIFIED_AD</code> - Indicates that the final sales transaction is to be completed
            outside of the eBay environment.</li></ul>Code so that your app gracefully handles any future changes to this
            list.
        category_id (Union[Unset, str]): The ID of the leaf category for this item. A leaf category is the lowest level
            in that category and has no children.
        category_id_path (Union[Unset, str]): The IDs of every category in the item path, separated by pipe characters,
            starting with the top level parent category.<br /><br />For example, if an item belongs to the top level
            category Home and Garden (category ID 11700), followed by Home Improvement (159907), Heating, Cooling and Air
            (69197), and Thermostats (115947), the field would return the value: <code>11700|159907|69197|115947</code>.
        category_path (Union[Unset, str]): Text that shows the category hierarchy of the item. For example:
            Computers/Tablets &amp; Networking, Laptops &amp; Netbooks, PC Laptops &amp; Netbooks
        color (Union[Unset, str]): (Primary Item Aspect) Text describing the color of the item.  All the item aspects,
            including this aspect, are returned in the <b> localizedAspects</b> container.
        condition (Union[Unset, str]): A short text description for the condition of the item, such as New or Used. For
            a list of condition names, see <a
            href="https://developer.ebay.com/devzone/finding/callref/enums/conditionIdList.html " target="_blank">Item
            Condition IDs and Names</a>.  <br /><br />Code so that your app gracefully handles any future changes to this
            list.
        condition_description (Union[Unset, str]): A full text description for the condition of the item. This field
            elaborates on the value specified in the <b>condition</b> field and provides full details for the condition of
            the item.
        condition_id (Union[Unset, str]): The identifier of the condition of the item. For example, 1000 is the
            identifier for NEW. For a list of condition names and IDs, see <a
            href="https://developer.ebay.com/devzone/finding/callref/enums/conditionIdList.html " target="_blank">Item
            Condition IDs and Names</a>. <br /><br />Code so that your app gracefully handles any future changes to this
            list.
        current_bid_price (Union[Unset, ConvertedAmount]): This type defines the monetary value of an amount. It can
            provide the amount in both the currency used on the eBay site where an item is being offered and the conversion
            of that value into another currency, if applicable.
        description (Union[Unset, str]): The full description of the item that was created by the seller. This can be
            plain text or rich content and can be very large.
        eco_participation_fee (Union[Unset, ConvertedAmount]): This type defines the monetary value of an amount. It can
            provide the amount in both the currency used on the eBay site where an item is being offered and the conversion
            of that value into another currency, if applicable.
        eligible_for_inline_checkout (Union[Unset, bool]): This field indicates if the item can be purchased using the
            Buy <a href="/api-docs/buy/order/resources/methods">Order API</a>. <ul> <li>If the value of this field is
            <code>true</code>, this indicates that the item can be purchased using the <b> Order API</b>. </li>  <li>If the
            value of this field is <code>false</code>, this indicates that the item cannot be purchased using the <b> Order
            API</b> and must be purchased on the eBay site.</li> </ul>
        enabled_for_guest_checkout (Union[Unset, bool]): This indicates if the item can be purchased using Guest
            Checkout in the <a href="/api-docs/buy/order/resources/methods">Order API</a>. You can use this flag to exclude
            items from your inventory that are not eligible for Guest Checkout, such as gift cards.
        energy_efficiency_class (Union[Unset, str]): This indicates the <a
            href="https://en.wikipedia.org/wiki/European_Union_energy_label ">European energy efficiency</a> rating (EEK) of
            the item. This field is returned only if the seller specified the energy efficiency rating. <br /><br />The
            rating is a set of energy efficiency classes from A to G, where 'A' is the most energy efficient and 'G' is the
            least efficient. This rating helps buyers choose between various models. <br /><br />When the manufacturer's
            specifications for this item are available, the link to this information is returned in the <b>
            productFicheWebUrl</b> field.
        epid (Union[Unset, str]): An EPID is the eBay product identifier of a product from the eBay product catalog.
            This indicates the product in which the item belongs.
        estimated_availabilities (Union[Unset, List[EstimatedAvailability]]): The estimated number of this item that are
            available for purchase. Because the quantity of an item can change several times within a second, it is
            impossible to return the exact quantity. So instead of returning quantity, the estimated availability of the
            item is returned.
        gender (Union[Unset, str]): (Primary Item Aspect) The gender for the item. This is used for items that could
            vary by gender, such as clothing. For example: male, female, or unisex. All the item aspects, including this
            aspect, are returned in the <b> localizedAspects</b> container.
        gtin (Union[Unset, str]): The unique Global Trade Item number of the item as defined by <a
            href="https://www.gtin.info " target="_blank">https://www.gtin.info</a>. This can be a UPC (Universal Product
            Code), EAN (European Article Number), or an ISBN (International Standard Book Number) value.
        image (Union[Unset, Image]): Type the defines the details of an image, such as size and image URL. Currently,
            only <b> imageUrl</b> is  populated. The <b> height</b> and <b> width</b> were added for future use.
        inferred_epid (Union[Unset, str]): The ePID (eBay Product ID of a product from the eBay product catalog) for the
            item, which has been programmatically determined by eBay using the item's title, aspects, and other data. <br
            /><br />If the seller provided an ePID for the item, the seller's value is returned in the <b> epid</b> field.
            <br /><br /><span class="tablenote"><b> Note: </b> This field is returned only for authorized Partners.</span>
        item_affiliate_web_url (Union[Unset, str]): The URL of the View Item page of the item, which includes the
            affiliate tracking ID. This field is only returned if the eBay partner enables affiliate tracking for the item
            by including the  <a href="/api-docs/buy/static/api-browse.html#Headers"><code>X-EBAY-C-ENDUSERCTX</code></a>
            request header in the method.  <br /> <br /><span class="tablenote"><b>Note: </b> eBay Partner Network, in order
            to be commissioned for your sales, you must use this URL to forward your buyer to the ebay.com site. </span>
        item_creation_date (Union[Unset, str]): A timestamp that indicates the date and time an item listing was
            created.<br /><br />This value is returned in UTC format (yyyy-MM-ddThh:mm:ss.sssZ), which can be converted into
            the local time of the buyer.
        item_end_date (Union[Unset, str]): This timestamp indicates the date and time up to which the item can be
            purchased.  This value is returned in UTC format (yyyy-MM-ddThh:mm:ss.sssZ), which you can convert into the
            local time of the buyer.<br /><br /><span class="tablenote"><b> Note: </b>This field is only returned for
            auction listings.</span>
        item_id (Union[Unset, str]): The unique RESTful identifier of the item.
        item_location (Union[Unset, Address]): The type that defines the fields for an address.
        item_web_url (Union[Unset, str]): The URL of the View Item page of the item. This enables you to include a
            "Report Item on eBay" link that takes the buyer to the View Item page on eBay. From there they can report any
            issues regarding this item to eBay.
        legacy_item_id (Union[Unset, str]): The unique identifier of the eBay listing that contains the item. This is
            the traditional/legacy ID that is often seen in the URL of the listing View Item page.
        listing_marketplace_id (Union[Unset, str]): The ID of the eBay marketplace where the item is listed. For
            implementation help, refer to <a href='https://developer.ebay.com/api-
            docs/buy/browse/types/ba:MarketplaceIdEnum'>eBay API documentation</a>
        localized_aspects (Union[Unset, List[TypedNameValue]]): An array of containers that show the complete list of
            the aspect name/value pairs that describe the variation of the item.
        lot_size (Union[Unset, int]): The number of items in a lot. In other words, a lot size is the number of items
            that are being sold together.  <br /><br />A lot is a set of two or more items included in a single listing that
            must be purchased together in a single order line item. All the items in the lot are the same but there can be
            multiple items in a single lot,  such as the package of batteries shown in the example below.   <br /><br
            /><table border="1"> <tr> <tr>  <th>Item</th>  <th>Lot Definition</th> <th>Lot Size</th></tr>  <tr>  <td>A
            package of 24 AA batteries</td>  <td>A box of 10 packages</td>  <td>10  </td> </tr>  <tr>  <td>A P235/75-15
            Goodyear tire </td>  <td>4 tires  </td>  <td>4  </td> </tr> <tr> <td>Fashion Jewelry Rings  </td> <td>Package of
            100 assorted rings  </td> <td>100 </td> </tr></table>  <br /><br /><span class="tablenote"><b>Note: </b>  Lots
            are not supported in all categories.  </span>
        marketing_price (Union[Unset, MarketingPrice]): The type that defines the fields that describe a seller
            discount.
        material (Union[Unset, str]): (Primary Item Aspect) Text describing what the item is made of. For example, silk.
            All the item aspects, including this aspect, are returned in the <b> localizedAspects</b> container.
        minimum_price_to_bid (Union[Unset, ConvertedAmount]): This type defines the monetary value of an amount. It can
            provide the amount in both the currency used on the eBay site where an item is being offered and the conversion
            of that value into another currency, if applicable.
        mpn (Union[Unset, str]): The manufacturer's part number, which is a unique number that identifies a specific
            product. To identify the product, this is always used along with brand.
        pattern (Union[Unset, str]): (Primary Item Aspect) Text describing the pattern used on the item. For example,
            paisley. All the item aspects, including this aspect, are returned in the <b> localizedAspects</b> container.
        payment_methods (Union[Unset, List[PaymentMethod]]): The payment methods for the item, including the payment
            method types, brands, and instructions for the buyer.
        price (Union[Unset, ConvertedAmount]): This type defines the monetary value of an amount. It can provide the
            amount in both the currency used on the eBay site where an item is being offered and the conversion of that
            value into another currency, if applicable.
        price_display_condition (Union[Unset, str]): Indicates when in the buying flow the item's price can appear for
            minimum advertised price (MAP) items, which is the lowest price a retailer can advertise/show for this item. For
            implementation help, refer to <a href='https://developer.ebay.com/api-
            docs/buy/browse/types/gct:PriceDisplayConditionEnum'>eBay API documentation</a>
        primary_item_group (Union[Unset, ItemGroupSummary]): The type that defines the fields for the details of each
            item in an item group. An item group is  an item that has various aspect differences, such as color, size,
            storage capacity, etc. When an item group is created, one of the item variations, such as the red shirt size L,
            is chosen as the "parent". All the other items in the group are the children, such as the blue shirt size L, red
            shirt size M, etc. <br /><br /><span class="tablenote"><b> Note: </b> This container is returned only if the <b>
            item_id</b> in the request is an item group (parent ID of an item with variations).</span>
        primary_product_review_rating (Union[Unset, ReviewRating]): The type that defines the fields for the rating of a
            product review.
        priority_listing (Union[Unset, bool]): This field is returned as <code>true</code> if the listing is part of a
            Promoted Listing campaign. Promoted Listings are available to Above Standard and Top Rated sellers with recent
            sales activity.<br /><br />For more information, see <a href="https://pages.ebay.com/seller-center/listing-and-
            marketing/promoted-listings.html " target="_blank">Promoted Listings</a>.
        product (Union[Unset, Product]): The type that defines the fields for the product information of the item.
        product_fiche_web_url (Union[Unset, str]): The URL of a page containing the manufacturer's specification of this
            item, which helps buyers make a purchasing decision. This information is available only for items that include
            the European energy efficiency rating (EEK) but is not available for <em> all</em> items with an EEK rating and
            is returned only if this information is available. The EEK rating of the item is returned in the <b>
            energyEfficiencyClass</b> field.
        qualified_programs (Union[Unset, List[str]]): An array of the qualified programs available for the item, or for
            the item group when returned for the <b>getItemsByItemGroup</b> method, such as EBAY_PLUS,
            AUTHENTICITY_GUARANTEE, and AUTHENTICITY_VERIFICATION.<br /><br /><span class="tablenote"><b>Note: </b>The
            <code>AUTHENTICITY_GUARANTEE</code> value being returned by the <b>getItemsByItemGroup</b> method indicates that
            at least one item in the item group supports this program, but doesn't guarantee that the program is available
            to all items in the item group. To verify if the Authenticity Program is indeed available for the item that you
            are interested in, grab the <b>items.itemId</b> value for that item and use the <b>getItem</b> method. This
            method will return specific details on that particular item, including whether or not the Authenticity Guarantee
            Program is available for the item. Look for the <b>qualifiedPrograms</b> array and <b>authenticityGuarantee</b>
            container in the <b>getItem</b> response for this information.</span><br /><br />eBay Plus is a premium account
            option for buyers, which provides benefits such as fast free domestic shipping and free returns on selected
            items. Top-Rated eBay sellers must opt in to eBay Plus to be able to offer the program on qualifying listings.
            Sellers must commit to next-day delivery of those items.<br /><br /><span class="tablenote"><b>Note: </b> eBay
            Plus is available only to buyers in Germany, Austria, and Australia marketplaces.</span><br /><br />The eBay <a
            href="https://pages.ebay.com/authenticity-guarantee/ " target="_blank">Authenticity Guarantee</a> program
            enables third-party authenticators to perform authentication verification inspections on items such as watches
            and sneakers.
        quantity_limit_per_buyer (Union[Unset, int]): The maximum number for a specific item that one buyer can
            purchase.
        reserve_price_met (Union[Unset, bool]): This indicates if the reserve price of the item has been met. A reserve
            price is set by the seller and is the minimum amount the seller is willing to sell the item for. <p>If the
            highest bid is not equal to or higher than the reserve price when the auction ends, the listing ends and the
            item is not sold.</p> <p><b> Note: </b>This is returned only for auctions that have a reserve price.</p>
        return_terms (Union[Unset, ItemReturnTerms]): The type that defines the fields for the seller's return policy.
        seller (Union[Unset, SellerDetail]): The type that defines the fields for basic and detailed information about
            the seller of the item returned by the <b> item</b> resource.
        seller_custom_policies (Union[Unset, List[SellerCustomPolicy]]): A list of the custom policies that are applied
            to a listing.
        seller_item_revision (Union[Unset, str]): An identifier generated/incremented when a seller revises the item.
            There are two types of item revisions: <ul><li>Seller changes, such as changing the title</li>  <li>eBay system
            changes, such as changing the quantity when an item is purchased</li></ul> This ID is changed <em> only</em>
            when the seller makes a change to the item. This means you cannot use this value to determine if the quantity
            has changed.
        shipping_options (Union[Unset, List[ShippingOption]]): An array of shipping options containers that have the
            details about cost, carrier, etc. of one shipping option.
        ship_to_locations (Union[Unset, ShipToLocations]): The type that defines the fields that include and exclude
            geographic regions affecting where the item can be shipped. The seller defines these regions when listing the
            item.
        short_description (Union[Unset, str]): This text string is derived from the item condition and the item aspects
            (such as size, color, capacity, model, brand, etc.).
        size (Union[Unset, str]): (Primary Item Aspect) The size of the item. For example, '7' for a size 7 shoe. All
            the item aspects, including this aspect, are returned in the <b> localizedAspects</b> container.
        size_system (Union[Unset, str]): (Primary Item Aspect) The sizing system of the country.  All the item aspects,
            including this aspect, are returned in the <b> localizedAspects</b> container. <br /><br /><b> Valid Values:
            </b> <br />AU (Australia),  <br />BR (Brazil), <br />CN (China),  <br />DE (Germany),  <br />EU (European
            Union),  <br /> FR (France), <br /> IT (Italy),  <br />JP (Japan), <br />MX (Mexico),  <br />US (USA), <br /> UK
            (United Kingdom) <br /><br />Code so that your app gracefully handles any future changes to this list.
        size_type (Union[Unset, str]): (Primary Item Aspect) Text describing a size group in which the item would be
            included, such as regular, petite, plus, big-and-tall or maternity. All the item aspects, including this aspect,
            are returned in the <b> localizedAspects</b> container.
        subtitle (Union[Unset, str]): A subtitle is optional and allows the seller to provide more information about the
            product, possibly including keywords that may assist with search results.
        taxes (Union[Unset, List[Taxes]]): The container for the tax information for the item.
        title (Union[Unset, str]): The seller-created title of the item. <br><br><b> Maximum Length: </b> 80 characters
        top_rated_buying_experience (Union[Unset, bool]): This indicates if the item a top-rated plus item. There are
            three benefits of a top-rated plus item: a  minimum 30-day money-back return policy, shipping the items in 1
            business day with tracking provided, and the added comfort of knowing this item is from experienced sellers with
            the highest buyer ratings. See the <a href="https://pages.ebay.com/topratedplus/index.html " target="_blank">Top
            Rated Plus Items </a> and <a href="https://pages.ebay.com/help/sell/top-rated.html " target="_blank">Becoming a
            Top Rated Seller and qualifying for Top Rated Plus</a> help topics for more information.
        tyre_label_image_url (Union[Unset, str]): The URL to the image that shows the information on the tyre label.
        unique_bidder_count (Union[Unset, int]): This integer value indicates the number of different eBay users who
            have placed one or more bids on an auction item. This field is only applicable to auction items.
        unit_price (Union[Unset, ConvertedAmount]): This type defines the monetary value of an amount. It can provide
            the amount in both the currency used on the eBay site where an item is being offered and the conversion of that
            value into another currency, if applicable.
        unit_pricing_measure (Union[Unset, str]): The designation, such as size, weight, volume, count, etc., that was
            used to specify the quantity of the item.  This helps buyers compare prices. <br /><br />For example, the
            following tells the buyer that the item is 7.99 per 100 grams. <br /><br /><code>"unitPricingMeasure":
            "100g",<br /> "unitPrice": {<br />&nbsp;&nbsp;"value": "7.99",<br />&nbsp;&nbsp;"currency": "GBP"</code>
        warnings (Union[Unset, List[Error]]): An array of warning messages. These types of errors do not prevent the
            method from executing but should be checked.
        watch_count (Union[Unset, int]): The number of users that have added the item to their watch list.<br /><br
            /><span class="tablenote"> <strong>Note:</strong> This field is restricted to applications that have been
            granted permission to access this feature. You must submit an <a
            href="https://developer.ebay.com/my/support/tickets?tab=app-check ">App Check ticket</a> to request this access.
            In the App Check form, add a note to the <b>Application Title/Summary</b> and/or <b>Application Details</b>
            fields that you want access to Watch Count data in the Browse API.</span>
    """

    additional_images: Union[Unset, List[Image]] = UNSET
    addon_services: Union[Unset, List[AddonService]] = UNSET
    adult_only: Union[Unset, bool] = UNSET
    age_group: Union[Unset, str] = UNSET
    authenticity_guarantee: Union[Unset, AuthenticityGuaranteeProgram] = UNSET
    authenticity_verification: Union[Unset, AuthenticityVerificationProgram] = UNSET
    available_coupons: Union[Unset, List[AvailableCoupon]] = UNSET
    bid_count: Union[Unset, int] = UNSET
    brand: Union[Unset, str] = UNSET
    buying_options: Union[Unset, List[str]] = UNSET
    category_id: Union[Unset, str] = UNSET
    category_id_path: Union[Unset, str] = UNSET
    category_path: Union[Unset, str] = UNSET
    color: Union[Unset, str] = UNSET
    condition: Union[Unset, str] = UNSET
    condition_description: Union[Unset, str] = UNSET
    condition_id: Union[Unset, str] = UNSET
    current_bid_price: Union[Unset, ConvertedAmount] = UNSET
    description: Union[Unset, str] = UNSET
    eco_participation_fee: Union[Unset, ConvertedAmount] = UNSET
    eligible_for_inline_checkout: Union[Unset, bool] = UNSET
    enabled_for_guest_checkout: Union[Unset, bool] = UNSET
    energy_efficiency_class: Union[Unset, str] = UNSET
    epid: Union[Unset, str] = UNSET
    estimated_availabilities: Union[Unset, List[EstimatedAvailability]] = UNSET
    gender: Union[Unset, str] = UNSET
    gtin: Union[Unset, str] = UNSET
    image: Union[Unset, Image] = UNSET
    inferred_epid: Union[Unset, str] = UNSET
    item_affiliate_web_url: Union[Unset, str] = UNSET
    item_creation_date: Union[Unset, str] = UNSET
    item_end_date: Union[Unset, str] = UNSET
    item_id: Union[Unset, str] = UNSET
    item_location: Union[Unset, Address] = UNSET
    item_web_url: Union[Unset, str] = UNSET
    legacy_item_id: Union[Unset, str] = UNSET
    listing_marketplace_id: Union[Unset, str] = UNSET
    localized_aspects: Union[Unset, List[TypedNameValue]] = UNSET
    lot_size: Union[Unset, int] = UNSET
    marketing_price: Union[Unset, MarketingPrice] = UNSET
    material: Union[Unset, str] = UNSET
    minimum_price_to_bid: Union[Unset, ConvertedAmount] = UNSET
    mpn: Union[Unset, str] = UNSET
    pattern: Union[Unset, str] = UNSET
    payment_methods: Union[Unset, List[PaymentMethod]] = UNSET
    price: Union[Unset, ConvertedAmount] = UNSET
    price_display_condition: Union[Unset, str] = UNSET
    primary_item_group: Union[Unset, ItemGroupSummary] = UNSET
    primary_product_review_rating: Union[Unset, ReviewRating] = UNSET
    priority_listing: Union[Unset, bool] = UNSET
    product: Union[Unset, Product] = UNSET
    product_fiche_web_url: Union[Unset, str] = UNSET
    qualified_programs: Union[Unset, List[str]] = UNSET
    quantity_limit_per_buyer: Union[Unset, int] = UNSET
    reserve_price_met: Union[Unset, bool] = UNSET
    return_terms: Union[Unset, ItemReturnTerms] = UNSET
    seller: Union[Unset, SellerDetail] = UNSET
    seller_custom_policies: Union[Unset, List[SellerCustomPolicy]] = UNSET
    seller_item_revision: Union[Unset, str] = UNSET
    shipping_options: Union[Unset, List[ShippingOption]] = UNSET
    ship_to_locations: Union[Unset, ShipToLocations] = UNSET
    short_description: Union[Unset, str] = UNSET
    size: Union[Unset, str] = UNSET
    size_system: Union[Unset, str] = UNSET
    size_type: Union[Unset, str] = UNSET
    subtitle: Union[Unset, str] = UNSET
    taxes: Union[Unset, List[Taxes]] = UNSET
    title: Union[Unset, str] = UNSET
    top_rated_buying_experience: Union[Unset, bool] = UNSET
    tyre_label_image_url: Union[Unset, str] = UNSET
    unique_bidder_count: Union[Unset, int] = UNSET
    unit_price: Union[Unset, ConvertedAmount] = UNSET
    unit_pricing_measure: Union[Unset, str] = UNSET
    warnings: Union[Unset, List[Error]] = UNSET
    watch_count: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        additional_images: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.additional_images, Unset):
            additional_images = []
            for additional_images_item_data in self.additional_images:
                additional_images_item = additional_images_item_data.to_dict()

                additional_images.append(additional_images_item)

        addon_services: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.addon_services, Unset):
            addon_services = []
            for addon_services_item_data in self.addon_services:
                addon_services_item = addon_services_item_data.to_dict()

                addon_services.append(addon_services_item)

        adult_only = self.adult_only
        age_group = self.age_group
        authenticity_guarantee: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.authenticity_guarantee, Unset):
            authenticity_guarantee = self.authenticity_guarantee.to_dict()

        authenticity_verification: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.authenticity_verification, Unset):
            authenticity_verification = self.authenticity_verification.to_dict()

        available_coupons: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.available_coupons, Unset):
            available_coupons = []
            for available_coupons_item_data in self.available_coupons:
                available_coupons_item = available_coupons_item_data.to_dict()

                available_coupons.append(available_coupons_item)

        bid_count = self.bid_count
        brand = self.brand
        buying_options: Union[Unset, List[str]] = UNSET
        if not isinstance(self.buying_options, Unset):
            buying_options = self.buying_options

        category_id = self.category_id
        category_id_path = self.category_id_path
        category_path = self.category_path
        color = self.color
        condition = self.condition
        condition_description = self.condition_description
        condition_id = self.condition_id
        current_bid_price: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.current_bid_price, Unset):
            current_bid_price = self.current_bid_price.to_dict()

        description = self.description
        eco_participation_fee: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.eco_participation_fee, Unset):
            eco_participation_fee = self.eco_participation_fee.to_dict()

        eligible_for_inline_checkout = self.eligible_for_inline_checkout
        enabled_for_guest_checkout = self.enabled_for_guest_checkout
        energy_efficiency_class = self.energy_efficiency_class
        epid = self.epid
        estimated_availabilities: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.estimated_availabilities, Unset):
            estimated_availabilities = []
            for estimated_availabilities_item_data in self.estimated_availabilities:
                estimated_availabilities_item = estimated_availabilities_item_data.to_dict()

                estimated_availabilities.append(estimated_availabilities_item)

        gender = self.gender
        gtin = self.gtin
        image: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.image, Unset):
            image = self.image.to_dict()

        inferred_epid = self.inferred_epid
        item_affiliate_web_url = self.item_affiliate_web_url
        item_creation_date = self.item_creation_date
        item_end_date = self.item_end_date
        item_id = self.item_id
        item_location: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.item_location, Unset):
            item_location = self.item_location.to_dict()

        item_web_url = self.item_web_url
        legacy_item_id = self.legacy_item_id
        listing_marketplace_id = self.listing_marketplace_id
        localized_aspects: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.localized_aspects, Unset):
            localized_aspects = []
            for localized_aspects_item_data in self.localized_aspects:
                localized_aspects_item = localized_aspects_item_data.to_dict()

                localized_aspects.append(localized_aspects_item)

        lot_size = self.lot_size
        marketing_price: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.marketing_price, Unset):
            marketing_price = self.marketing_price.to_dict()

        material = self.material
        minimum_price_to_bid: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.minimum_price_to_bid, Unset):
            minimum_price_to_bid = self.minimum_price_to_bid.to_dict()

        mpn = self.mpn
        pattern = self.pattern
        payment_methods: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.payment_methods, Unset):
            payment_methods = []
            for payment_methods_item_data in self.payment_methods:
                payment_methods_item = payment_methods_item_data.to_dict()

                payment_methods.append(payment_methods_item)

        price: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.price, Unset):
            price = self.price.to_dict()

        price_display_condition = self.price_display_condition
        primary_item_group: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.primary_item_group, Unset):
            primary_item_group = self.primary_item_group.to_dict()

        primary_product_review_rating: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.primary_product_review_rating, Unset):
            primary_product_review_rating = self.primary_product_review_rating.to_dict()

        priority_listing = self.priority_listing
        product: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.product, Unset):
            product = self.product.to_dict()

        product_fiche_web_url = self.product_fiche_web_url
        qualified_programs: Union[Unset, List[str]] = UNSET
        if not isinstance(self.qualified_programs, Unset):
            qualified_programs = self.qualified_programs

        quantity_limit_per_buyer = self.quantity_limit_per_buyer
        reserve_price_met = self.reserve_price_met
        return_terms: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.return_terms, Unset):
            return_terms = self.return_terms.to_dict()

        seller: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.seller, Unset):
            seller = self.seller.to_dict()

        seller_custom_policies: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.seller_custom_policies, Unset):
            seller_custom_policies = []
            for seller_custom_policies_item_data in self.seller_custom_policies:
                seller_custom_policies_item = seller_custom_policies_item_data.to_dict()

                seller_custom_policies.append(seller_custom_policies_item)

        seller_item_revision = self.seller_item_revision
        shipping_options: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.shipping_options, Unset):
            shipping_options = []
            for shipping_options_item_data in self.shipping_options:
                shipping_options_item = shipping_options_item_data.to_dict()

                shipping_options.append(shipping_options_item)

        ship_to_locations: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ship_to_locations, Unset):
            ship_to_locations = self.ship_to_locations.to_dict()

        short_description = self.short_description
        size = self.size
        size_system = self.size_system
        size_type = self.size_type
        subtitle = self.subtitle
        taxes: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.taxes, Unset):
            taxes = []
            for taxes_item_data in self.taxes:
                taxes_item = taxes_item_data.to_dict()

                taxes.append(taxes_item)

        title = self.title
        top_rated_buying_experience = self.top_rated_buying_experience
        tyre_label_image_url = self.tyre_label_image_url
        unique_bidder_count = self.unique_bidder_count
        unit_price: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.unit_price, Unset):
            unit_price = self.unit_price.to_dict()

        unit_pricing_measure = self.unit_pricing_measure
        warnings: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.warnings, Unset):
            warnings = []
            for warnings_item_data in self.warnings:
                warnings_item = warnings_item_data.to_dict()

                warnings.append(warnings_item)

        watch_count = self.watch_count

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if additional_images is not UNSET:
            field_dict["additionalImages"] = additional_images
        if addon_services is not UNSET:
            field_dict["addonServices"] = addon_services
        if adult_only is not UNSET:
            field_dict["adultOnly"] = adult_only
        if age_group is not UNSET:
            field_dict["ageGroup"] = age_group
        if authenticity_guarantee is not UNSET:
            field_dict["authenticityGuarantee"] = authenticity_guarantee
        if authenticity_verification is not UNSET:
            field_dict["authenticityVerification"] = authenticity_verification
        if available_coupons is not UNSET:
            field_dict["availableCoupons"] = available_coupons
        if bid_count is not UNSET:
            field_dict["bidCount"] = bid_count
        if brand is not UNSET:
            field_dict["brand"] = brand
        if buying_options is not UNSET:
            field_dict["buyingOptions"] = buying_options
        if category_id is not UNSET:
            field_dict["categoryId"] = category_id
        if category_id_path is not UNSET:
            field_dict["categoryIdPath"] = category_id_path
        if category_path is not UNSET:
            field_dict["categoryPath"] = category_path
        if color is not UNSET:
            field_dict["color"] = color
        if condition is not UNSET:
            field_dict["condition"] = condition
        if condition_description is not UNSET:
            field_dict["conditionDescription"] = condition_description
        if condition_id is not UNSET:
            field_dict["conditionId"] = condition_id
        if current_bid_price is not UNSET:
            field_dict["currentBidPrice"] = current_bid_price
        if description is not UNSET:
            field_dict["description"] = description
        if eco_participation_fee is not UNSET:
            field_dict["ecoParticipationFee"] = eco_participation_fee
        if eligible_for_inline_checkout is not UNSET:
            field_dict["eligibleForInlineCheckout"] = eligible_for_inline_checkout
        if enabled_for_guest_checkout is not UNSET:
            field_dict["enabledForGuestCheckout"] = enabled_for_guest_checkout
        if energy_efficiency_class is not UNSET:
            field_dict["energyEfficiencyClass"] = energy_efficiency_class
        if epid is not UNSET:
            field_dict["epid"] = epid
        if estimated_availabilities is not UNSET:
            field_dict["estimatedAvailabilities"] = estimated_availabilities
        if gender is not UNSET:
            field_dict["gender"] = gender
        if gtin is not UNSET:
            field_dict["gtin"] = gtin
        if image is not UNSET:
            field_dict["image"] = image
        if inferred_epid is not UNSET:
            field_dict["inferredEpid"] = inferred_epid
        if item_affiliate_web_url is not UNSET:
            field_dict["itemAffiliateWebUrl"] = item_affiliate_web_url
        if item_creation_date is not UNSET:
            field_dict["itemCreationDate"] = item_creation_date
        if item_end_date is not UNSET:
            field_dict["itemEndDate"] = item_end_date
        if item_id is not UNSET:
            field_dict["itemId"] = item_id
        if item_location is not UNSET:
            field_dict["itemLocation"] = item_location
        if item_web_url is not UNSET:
            field_dict["itemWebUrl"] = item_web_url
        if legacy_item_id is not UNSET:
            field_dict["legacyItemId"] = legacy_item_id
        if listing_marketplace_id is not UNSET:
            field_dict["listingMarketplaceId"] = listing_marketplace_id
        if localized_aspects is not UNSET:
            field_dict["localizedAspects"] = localized_aspects
        if lot_size is not UNSET:
            field_dict["lotSize"] = lot_size
        if marketing_price is not UNSET:
            field_dict["marketingPrice"] = marketing_price
        if material is not UNSET:
            field_dict["material"] = material
        if minimum_price_to_bid is not UNSET:
            field_dict["minimumPriceToBid"] = minimum_price_to_bid
        if mpn is not UNSET:
            field_dict["mpn"] = mpn
        if pattern is not UNSET:
            field_dict["pattern"] = pattern
        if payment_methods is not UNSET:
            field_dict["paymentMethods"] = payment_methods
        if price is not UNSET:
            field_dict["price"] = price
        if price_display_condition is not UNSET:
            field_dict["priceDisplayCondition"] = price_display_condition
        if primary_item_group is not UNSET:
            field_dict["primaryItemGroup"] = primary_item_group
        if primary_product_review_rating is not UNSET:
            field_dict["primaryProductReviewRating"] = primary_product_review_rating
        if priority_listing is not UNSET:
            field_dict["priorityListing"] = priority_listing
        if product is not UNSET:
            field_dict["product"] = product
        if product_fiche_web_url is not UNSET:
            field_dict["productFicheWebUrl"] = product_fiche_web_url
        if qualified_programs is not UNSET:
            field_dict["qualifiedPrograms"] = qualified_programs
        if quantity_limit_per_buyer is not UNSET:
            field_dict["quantityLimitPerBuyer"] = quantity_limit_per_buyer
        if reserve_price_met is not UNSET:
            field_dict["reservePriceMet"] = reserve_price_met
        if return_terms is not UNSET:
            field_dict["returnTerms"] = return_terms
        if seller is not UNSET:
            field_dict["seller"] = seller
        if seller_custom_policies is not UNSET:
            field_dict["sellerCustomPolicies"] = seller_custom_policies
        if seller_item_revision is not UNSET:
            field_dict["sellerItemRevision"] = seller_item_revision
        if shipping_options is not UNSET:
            field_dict["shippingOptions"] = shipping_options
        if ship_to_locations is not UNSET:
            field_dict["shipToLocations"] = ship_to_locations
        if short_description is not UNSET:
            field_dict["shortDescription"] = short_description
        if size is not UNSET:
            field_dict["size"] = size
        if size_system is not UNSET:
            field_dict["sizeSystem"] = size_system
        if size_type is not UNSET:
            field_dict["sizeType"] = size_type
        if subtitle is not UNSET:
            field_dict["subtitle"] = subtitle
        if taxes is not UNSET:
            field_dict["taxes"] = taxes
        if title is not UNSET:
            field_dict["title"] = title
        if top_rated_buying_experience is not UNSET:
            field_dict["topRatedBuyingExperience"] = top_rated_buying_experience
        if tyre_label_image_url is not UNSET:
            field_dict["tyreLabelImageUrl"] = tyre_label_image_url
        if unique_bidder_count is not UNSET:
            field_dict["uniqueBidderCount"] = unique_bidder_count
        if unit_price is not UNSET:
            field_dict["unitPrice"] = unit_price
        if unit_pricing_measure is not UNSET:
            field_dict["unitPricingMeasure"] = unit_pricing_measure
        if warnings is not UNSET:
            field_dict["warnings"] = warnings
        if watch_count is not UNSET:
            field_dict["watchCount"] = watch_count

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        additional_images = []
        _additional_images = d.pop("additionalImages", UNSET)
        for additional_images_item_data in _additional_images or []:
            additional_images_item = Image.from_dict(additional_images_item_data)

            additional_images.append(additional_images_item)

        addon_services = []
        _addon_services = d.pop("addonServices", UNSET)
        for addon_services_item_data in _addon_services or []:
            addon_services_item = AddonService.from_dict(addon_services_item_data)

            addon_services.append(addon_services_item)

        adult_only = d.pop("adultOnly", UNSET)

        age_group = d.pop("ageGroup", UNSET)

        _authenticity_guarantee = d.pop("authenticityGuarantee", UNSET)
        authenticity_guarantee: Union[Unset, AuthenticityGuaranteeProgram]
        if isinstance(_authenticity_guarantee, Unset):
            authenticity_guarantee = UNSET
        else:
            authenticity_guarantee = AuthenticityGuaranteeProgram.from_dict(_authenticity_guarantee)

        _authenticity_verification = d.pop("authenticityVerification", UNSET)
        authenticity_verification: Union[Unset, AuthenticityVerificationProgram]
        if isinstance(_authenticity_verification, Unset):
            authenticity_verification = UNSET
        else:
            authenticity_verification = AuthenticityVerificationProgram.from_dict(_authenticity_verification)

        available_coupons = []
        _available_coupons = d.pop("availableCoupons", UNSET)
        for available_coupons_item_data in _available_coupons or []:
            available_coupons_item = AvailableCoupon.from_dict(available_coupons_item_data)

            available_coupons.append(available_coupons_item)

        bid_count = d.pop("bidCount", UNSET)

        brand = d.pop("brand", UNSET)

        buying_options = cast(List[str], d.pop("buyingOptions", UNSET))

        category_id = d.pop("categoryId", UNSET)

        category_id_path = d.pop("categoryIdPath", UNSET)

        category_path = d.pop("categoryPath", UNSET)

        color = d.pop("color", UNSET)

        condition = d.pop("condition", UNSET)

        condition_description = d.pop("conditionDescription", UNSET)

        condition_id = d.pop("conditionId", UNSET)

        _current_bid_price = d.pop("currentBidPrice", UNSET)
        current_bid_price: Union[Unset, ConvertedAmount]
        if isinstance(_current_bid_price, Unset):
            current_bid_price = UNSET
        else:
            current_bid_price = ConvertedAmount.from_dict(_current_bid_price)

        description = d.pop("description", UNSET)

        _eco_participation_fee = d.pop("ecoParticipationFee", UNSET)
        eco_participation_fee: Union[Unset, ConvertedAmount]
        if isinstance(_eco_participation_fee, Unset):
            eco_participation_fee = UNSET
        else:
            eco_participation_fee = ConvertedAmount.from_dict(_eco_participation_fee)

        eligible_for_inline_checkout = d.pop("eligibleForInlineCheckout", UNSET)

        enabled_for_guest_checkout = d.pop("enabledForGuestCheckout", UNSET)

        energy_efficiency_class = d.pop("energyEfficiencyClass", UNSET)

        epid = d.pop("epid", UNSET)

        estimated_availabilities = []
        _estimated_availabilities = d.pop("estimatedAvailabilities", UNSET)
        for estimated_availabilities_item_data in _estimated_availabilities or []:
            estimated_availabilities_item = EstimatedAvailability.from_dict(estimated_availabilities_item_data)

            estimated_availabilities.append(estimated_availabilities_item)

        gender = d.pop("gender", UNSET)

        gtin = d.pop("gtin", UNSET)

        _image = d.pop("image", UNSET)
        image: Union[Unset, Image]
        if isinstance(_image, Unset):
            image = UNSET
        else:
            image = Image.from_dict(_image)

        inferred_epid = d.pop("inferredEpid", UNSET)

        item_affiliate_web_url = d.pop("itemAffiliateWebUrl", UNSET)

        item_creation_date = d.pop("itemCreationDate", UNSET)

        item_end_date = d.pop("itemEndDate", UNSET)

        item_id = d.pop("itemId", UNSET)

        _item_location = d.pop("itemLocation", UNSET)
        item_location: Union[Unset, Address]
        if isinstance(_item_location, Unset):
            item_location = UNSET
        else:
            item_location = Address.from_dict(_item_location)

        item_web_url = d.pop("itemWebUrl", UNSET)

        legacy_item_id = d.pop("legacyItemId", UNSET)

        listing_marketplace_id = d.pop("listingMarketplaceId", UNSET)

        localized_aspects = []
        _localized_aspects = d.pop("localizedAspects", UNSET)
        for localized_aspects_item_data in _localized_aspects or []:
            localized_aspects_item = TypedNameValue.from_dict(localized_aspects_item_data)

            localized_aspects.append(localized_aspects_item)

        lot_size = d.pop("lotSize", UNSET)

        _marketing_price = d.pop("marketingPrice", UNSET)
        marketing_price: Union[Unset, MarketingPrice]
        if isinstance(_marketing_price, Unset):
            marketing_price = UNSET
        else:
            marketing_price = MarketingPrice.from_dict(_marketing_price)

        material = d.pop("material", UNSET)

        _minimum_price_to_bid = d.pop("minimumPriceToBid", UNSET)
        minimum_price_to_bid: Union[Unset, ConvertedAmount]
        if isinstance(_minimum_price_to_bid, Unset):
            minimum_price_to_bid = UNSET
        else:
            minimum_price_to_bid = ConvertedAmount.from_dict(_minimum_price_to_bid)

        mpn = d.pop("mpn", UNSET)

        pattern = d.pop("pattern", UNSET)

        payment_methods = []
        _payment_methods = d.pop("paymentMethods", UNSET)
        for payment_methods_item_data in _payment_methods or []:
            payment_methods_item = PaymentMethod.from_dict(payment_methods_item_data)

            payment_methods.append(payment_methods_item)

        _price = d.pop("price", UNSET)
        price: Union[Unset, ConvertedAmount]
        if isinstance(_price, Unset):
            price = UNSET
        else:
            price = ConvertedAmount.from_dict(_price)

        price_display_condition = d.pop("priceDisplayCondition", UNSET)

        _primary_item_group = d.pop("primaryItemGroup", UNSET)
        primary_item_group: Union[Unset, ItemGroupSummary]
        if isinstance(_primary_item_group, Unset):
            primary_item_group = UNSET
        else:
            primary_item_group = ItemGroupSummary.from_dict(_primary_item_group)

        _primary_product_review_rating = d.pop("primaryProductReviewRating", UNSET)
        primary_product_review_rating: Union[Unset, ReviewRating]
        if isinstance(_primary_product_review_rating, Unset):
            primary_product_review_rating = UNSET
        else:
            primary_product_review_rating = ReviewRating.from_dict(_primary_product_review_rating)

        priority_listing = d.pop("priorityListing", UNSET)

        _product = d.pop("product", UNSET)
        product: Union[Unset, Product]
        if isinstance(_product, Unset):
            product = UNSET
        else:
            product = Product.from_dict(_product)

        product_fiche_web_url = d.pop("productFicheWebUrl", UNSET)

        qualified_programs = cast(List[str], d.pop("qualifiedPrograms", UNSET))

        quantity_limit_per_buyer = d.pop("quantityLimitPerBuyer", UNSET)

        reserve_price_met = d.pop("reservePriceMet", UNSET)

        _return_terms = d.pop("returnTerms", UNSET)
        return_terms: Union[Unset, ItemReturnTerms]
        if isinstance(_return_terms, Unset):
            return_terms = UNSET
        else:
            return_terms = ItemReturnTerms.from_dict(_return_terms)

        _seller = d.pop("seller", UNSET)
        seller: Union[Unset, SellerDetail]
        if isinstance(_seller, Unset):
            seller = UNSET
        else:
            seller = SellerDetail.from_dict(_seller)

        seller_custom_policies = []
        _seller_custom_policies = d.pop("sellerCustomPolicies", UNSET)
        for seller_custom_policies_item_data in _seller_custom_policies or []:
            seller_custom_policies_item = SellerCustomPolicy.from_dict(seller_custom_policies_item_data)

            seller_custom_policies.append(seller_custom_policies_item)

        seller_item_revision = d.pop("sellerItemRevision", UNSET)

        shipping_options = []
        _shipping_options = d.pop("shippingOptions", UNSET)
        for shipping_options_item_data in _shipping_options or []:
            shipping_options_item = ShippingOption.from_dict(shipping_options_item_data)

            shipping_options.append(shipping_options_item)

        _ship_to_locations = d.pop("shipToLocations", UNSET)
        ship_to_locations: Union[Unset, ShipToLocations]
        if isinstance(_ship_to_locations, Unset):
            ship_to_locations = UNSET
        else:
            ship_to_locations = ShipToLocations.from_dict(_ship_to_locations)

        short_description = d.pop("shortDescription", UNSET)

        size = d.pop("size", UNSET)

        size_system = d.pop("sizeSystem", UNSET)

        size_type = d.pop("sizeType", UNSET)

        subtitle = d.pop("subtitle", UNSET)

        taxes = []
        _taxes = d.pop("taxes", UNSET)
        for taxes_item_data in _taxes or []:
            taxes_item = Taxes.from_dict(taxes_item_data)

            taxes.append(taxes_item)

        title = d.pop("title", UNSET)

        top_rated_buying_experience = d.pop("topRatedBuyingExperience", UNSET)

        tyre_label_image_url = d.pop("tyreLabelImageUrl", UNSET)

        unique_bidder_count = d.pop("uniqueBidderCount", UNSET)

        _unit_price = d.pop("unitPrice", UNSET)
        unit_price: Union[Unset, ConvertedAmount]
        if isinstance(_unit_price, Unset):
            unit_price = UNSET
        else:
            unit_price = ConvertedAmount.from_dict(_unit_price)

        unit_pricing_measure = d.pop("unitPricingMeasure", UNSET)

        warnings = []
        _warnings = d.pop("warnings", UNSET)
        for warnings_item_data in _warnings or []:
            warnings_item = Error.from_dict(warnings_item_data)

            warnings.append(warnings_item)

        watch_count = d.pop("watchCount", UNSET)

        item = cls(
            additional_images=additional_images,
            addon_services=addon_services,
            adult_only=adult_only,
            age_group=age_group,
            authenticity_guarantee=authenticity_guarantee,
            authenticity_verification=authenticity_verification,
            available_coupons=available_coupons,
            bid_count=bid_count,
            brand=brand,
            buying_options=buying_options,
            category_id=category_id,
            category_id_path=category_id_path,
            category_path=category_path,
            color=color,
            condition=condition,
            condition_description=condition_description,
            condition_id=condition_id,
            current_bid_price=current_bid_price,
            description=description,
            eco_participation_fee=eco_participation_fee,
            eligible_for_inline_checkout=eligible_for_inline_checkout,
            enabled_for_guest_checkout=enabled_for_guest_checkout,
            energy_efficiency_class=energy_efficiency_class,
            epid=epid,
            estimated_availabilities=estimated_availabilities,
            gender=gender,
            gtin=gtin,
            image=image,
            inferred_epid=inferred_epid,
            item_affiliate_web_url=item_affiliate_web_url,
            item_creation_date=item_creation_date,
            item_end_date=item_end_date,
            item_id=item_id,
            item_location=item_location,
            item_web_url=item_web_url,
            legacy_item_id=legacy_item_id,
            listing_marketplace_id=listing_marketplace_id,
            localized_aspects=localized_aspects,
            lot_size=lot_size,
            marketing_price=marketing_price,
            material=material,
            minimum_price_to_bid=minimum_price_to_bid,
            mpn=mpn,
            pattern=pattern,
            payment_methods=payment_methods,
            price=price,
            price_display_condition=price_display_condition,
            primary_item_group=primary_item_group,
            primary_product_review_rating=primary_product_review_rating,
            priority_listing=priority_listing,
            product=product,
            product_fiche_web_url=product_fiche_web_url,
            qualified_programs=qualified_programs,
            quantity_limit_per_buyer=quantity_limit_per_buyer,
            reserve_price_met=reserve_price_met,
            return_terms=return_terms,
            seller=seller,
            seller_custom_policies=seller_custom_policies,
            seller_item_revision=seller_item_revision,
            shipping_options=shipping_options,
            ship_to_locations=ship_to_locations,
            short_description=short_description,
            size=size,
            size_system=size_system,
            size_type=size_type,
            subtitle=subtitle,
            taxes=taxes,
            title=title,
            top_rated_buying_experience=top_rated_buying_experience,
            tyre_label_image_url=tyre_label_image_url,
            unique_bidder_count=unique_bidder_count,
            unit_price=unit_price,
            unit_pricing_measure=unit_pricing_measure,
            warnings=warnings,
            watch_count=watch_count,
        )

        item.additional_properties = d
        return item

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
