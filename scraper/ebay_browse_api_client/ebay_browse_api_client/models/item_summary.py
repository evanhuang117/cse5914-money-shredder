from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.category import Category
from ..models.compatibility_property import CompatibilityProperty
from ..models.converted_amount import ConvertedAmount
from ..models.image import Image
from ..models.item_location_impl import ItemLocationImpl
from ..models.marketing_price import MarketingPrice
from ..models.pickup_option_summary import PickupOptionSummary
from ..models.seller import Seller
from ..models.shipping_option_summary import ShippingOptionSummary
from ..models.target_location import TargetLocation
from ..types import UNSET, Unset

T = TypeVar("T", bound="ItemSummary")


@attr.s(auto_attribs=True)
class ItemSummary:
    """The type that defines the fields for the details of a specific item.

    Attributes:
        additional_images (Union[Unset, List[Image]]): An array of containers with the URLs for the images that are in
            addition to the primary image.  The primary image is returned in the <b> image.imageUrl</b> field.
        adult_only (Union[Unset, bool]): This indicates if the item is for adults only. For more information about
            adult-only items on eBay, see <a href="https://pages.ebay.com/help/policies/adult-only.html "
            target="_blank">Adult items policy</a> for sellers and <a href="https://www.ebay.com/help/terms-
            conditions/default/searching-adult-items?id=4661 " target="_blank">Adult-Only items on eBay</a> for buyers.
        available_coupons (Union[Unset, bool]): This boolean attribute indicates if coupons are available for the item.
        bid_count (Union[Unset, int]): This integer value indicates the total number of bids that have been placed for
            an auction item. This field is only returned for auction items.
        buying_options (Union[Unset, List[str]]): A comma separated list of all the purchase options available for the
            item. <br><br><b> Values Returned:</b><ul><li><b>FIXED_PRICE</b> - Indicates the buyer can purchase the item for
            a set price using the Buy It Now button. </li>  <li><b> AUCTION</b> - Indicates the buyer can place a bid for
            the item. After the first bid is placed, this becomes a live auction item and is the only buying option for this
            item.</li>  <li><b> BEST_OFFER</b> - Items where the buyer can send the seller a price they're willing to pay
            for the item. The seller can accept, reject, or send a counter offer. For details about Best Offer, see <a
            href="https://www.ebay.com/help/selling/listings/selling-buy-now/adding-best-offer-listing?id=4144 "
            target="_blank">Best Offer</a>.</li><li><b>CLASSIFIED_AD</b> - Indicates that the final sales transaction is to
            be completed outside of the eBay environment.</li></ul> Code so that your app gracefully handles any future
            changes to this list.
        categories (Union[Unset, List[Category]]): This array returns the name and ID of each category associated with
            the item, including top level, branch, and leaf categories.
        compatibility_match (Union[Unset, str]): This indicates how well the item matches the
            <b>compatibility_filter</b> product attributes.  <br><br><b> Valid Values: </b> EXACT or POSSIBLE <br /><br
            />Code so that your app gracefully handles any future changes to this list. For implementation help, refer to <a
            href='https://developer.ebay.com/api-docs/buy/browse/types/gct:CompatibilityMatchEnum'>eBay API
            documentation</a>
        compatibility_properties (Union[Unset, List[CompatibilityProperty]]): This container returns only the product
            attributes that are compatible with the item. These attributes were specified in the <b>compatibility_filter</b>
            in the request. This means that if you passed in 5 attributes and only 4 are compatible, only those 4 are
            returned. If none of the attributes are compatible, this container is not returned.
        condition (Union[Unset, str]): The text describing the condition of the item, such as New or Used. For a list of
            condition names, see <a href="https://developer.ebay.com/devzone/finding/callref/enums/conditionIdList.html "
            target="_blank">Item Condition IDs and Names</a>.  <br /><br />Code so that your app gracefully handles any
            future changes to this list.</span>
        condition_id (Union[Unset, str]): The identifier of the condition of the item. For example, 1000 is the
            identifier for NEW. For a list of condition names and IDs, see <a
            href="https://developer.ebay.com/devzone/finding/callref/enums/conditionIdList.html " target="_blank">Item
            Condition IDs and Names</a>. <br /><br />Code so that your app gracefully handles any future changes to this
            list.
        current_bid_price (Union[Unset, ConvertedAmount]): This type defines the monetary value of an amount. It can
            provide the amount in both the currency used on the eBay site where an item is being offered and the conversion
            of that value into another currency, if applicable.
        distance_from_pickup_location (Union[Unset, TargetLocation]): The type that defines the fields for the distance
            between the item location and the buyer's location.
        energy_efficiency_class (Union[Unset, str]): This indicates the <a
            href="https://en.wikipedia.org/wiki/European_Union_energy_label ">European energy efficiency</a> rating (EEK) of
            the item.  Energy efficiency ratings apply to products listed by commercial vendors in electronics categories
            only. <br /><br />Currently, this field is only applicable for the Germany site, and  is only returned if the
            seller specified the energy efficiency rating through item specifics at listing time. Rating values include
            <code>A+++</code>, <code>A++</code>, <code>A+</code>, <code>A</code>, <code>B</code>, <code>C</code>,
            <code>D</code>, <code>E</code>, <code>F</code>, and <code>G</code>.
        epid (Union[Unset, str]): An ePID is the eBay product identifier of a product from the eBay product catalog.
            This indicates the product in which the item belongs.
        image (Union[Unset, Image]): Type the defines the details of an image, such as size and image URL. Currently,
            only <b> imageUrl</b> is  populated. The <b> height</b> and <b> width</b> were added for future use.
        item_affiliate_web_url (Union[Unset, str]): The URL to the View Item page of the item, which includes the
            affiliate tracking ID. This field is only returned if the seller enables affiliate tracking for the item by
            including the <code><a href="/api-docs/buy/static/api-browse.html#Headers">X-EBAY-C-ENDUSERCTX</a></code>
            request header in the method.  <br /> <br /><span class="tablenote"><b>Note: </b> eBay Partner Network, in order
            to receive a commission for your sales, you must use this URL to forward your buyer to the ebay.com site.
            </span>
        item_creation_date (Union[Unset, str]): The date and time when the item listing was created.  This value is
            returned in UTC format (yyyy-MM-ddThh:mm:ss.sssZ), which you can convert into the local time of the buyer.
        item_end_date (Union[Unset, str]): The date and time up to which the item can be purchased.  This value is
            returned in UTC format (yyyy-MM-ddThh:mm:ss.sssZ), which you can convert into the local time of the buyer.<br
            /><br /><span class="tablenote"><b> Note: </b>This field is not returned for Good 'Til Cancelled (GTC)
            listings.</span>
        item_group_href (Union[Unset, str]): The HATEOAS reference of the parent page of the item group. An item group
            is an item that has various aspect differences, such as color, size, storage capacity, etc. <br /> <br /><span
            class="tablenote"> <b>  Note: </b>This field is returned only for item groups.</span>
        item_group_type (Union[Unset, str]): The indicates the item group type. An item group is an item that has
            various aspect differences, such as color, size, storage capacity, etc. <br /><br />Currently only the
            <code>SELLER_DEFINED_VARIATIONS</code> is supported and indicates this is an item group created by the seller.
            <br /> <br /><span class="tablenote"> <b> Note: </b>This field is returned only for item groups.</span><br /><br
            />Code so that your app gracefully handles any future changes to this list.
        item_href (Union[Unset, str]): The URI for the Browse API <a href="/api-
            docs/buy/browse/resources/item/methods/getItem">getItem</a> method, which can be used to retrieve more details
            about items in the search results.
        item_id (Union[Unset, str]): The unique RESTful identifier of the item.
        item_location (Union[Unset, ItemLocationImpl]): The type that defines the fields for the location of an item,
            such as information typically used for an address, including postal code, county, state/province, street
            address, city, and country (2-digit ISO code).
        item_web_url (Union[Unset, str]): The URL to the View Item page of the item.  This enables you to include a
            "Report Item on eBay" hyperlink that takes the buyer to the View Item page on eBay. From there they can report
            any issues regarding this item to eBay.
        leaf_category_ids (Union[Unset, List[str]]): The leaf category IDs of the item. When the item belongs to two
            leaf categories, the ID values are returned in the order primary, secondary.
        legacy_item_id (Union[Unset, str]): The unique identifier of the eBay listing that contains the item. This is
            the traditional/legacy ID that is often seen in the URL of the listing View Item page.
        listing_marketplace_id (Union[Unset, str]): The ID of the eBay marketplace where the item is listed. For
            implementation help, refer to <a href='https://developer.ebay.com/api-
            docs/buy/browse/types/ba:MarketplaceIdEnum'>eBay API documentation</a>
        marketing_price (Union[Unset, MarketingPrice]): The type that defines the fields that describe a seller
            discount.
        pickup_options (Union[Unset, List[PickupOptionSummary]]): This container returns the local pickup options
            available to the buyer. This container is only returned if the user is searching for local pickup items and set
            the local pickup filters in the method request.
        price (Union[Unset, ConvertedAmount]): This type defines the monetary value of an amount. It can provide the
            amount in both the currency used on the eBay site where an item is being offered and the conversion of that
            value into another currency, if applicable.
        price_display_condition (Union[Unset, str]): Indicates when in the buying flow the item's price can appear for
            minimum advertised price (MAP) items, which is the lowest price a retailer can advertise/show for this item. For
            implementation help, refer to <a href='https://developer.ebay.com/api-
            docs/buy/browse/types/gct:PriceDisplayConditionEnum'>eBay API documentation</a>
        priority_listing (Union[Unset, bool]): This field is returned as <code>true</code> if the listing is part of a
            Promoted Listing campaign. Promoted Listings are available to Above Standard and Top Rated sellers with recent
            sales activity.<br /><br /><span class="tablenote"><b>Note:</b> Priority Listing is returned only with a Best
            Match sort and will not be returned for other sort options.</span>
        qualified_programs (Union[Unset, List[str]]): An array of the qualified programs available for the item, such as
            EBAY_PLUS, AUTHENTICITY_GUARANTEE, and AUTHENTICITY_VERIFICATION.<br /><br />eBay Plus is a premium account
            option for buyers, which provides benefits such as fast free domestic shipping and free returns on selected
            items. Top-Rated eBay sellers must opt in to eBay Plus to be able to offer the program on qualifying listings.
            Sellers must commit to next-day delivery of those items.<br /><br /><span class="tablenote"><b>Note: </b> eBay
            Plus is available only to buyers in Germany, Austria, and Australia marketplaces.</span><br /><br />The eBay <a
            href="https://pages.ebay.com/authenticity-guarantee/ " target="_blank">Authenticity Guarantee</a> program
            enables third-party authenticators to perform authentication verification inspections on items such as watches
            and sneakers.
        seller (Union[Unset, Seller]): The type that defines the fields for basic information about the seller of the
            item returned by the <b> item_summary</b> resource.
        shipping_options (Union[Unset, List[ShippingOptionSummary]]): This container returns the shipping options
            available to ship the item.
        short_description (Union[Unset, str]): This text string is derived from the item condition and the item aspects
            (such as size, color, capacity, model, brand, etc.). Sometimes the title doesn't give enough information but the
            description is too big. Surfacing the <b>shortDescription</b> can often provide buyers with the additional
            information that could help them make a buying decision.  <br /><br />For example: <br /><br />    <code>   "<b>
            title</b>": "Petrel U42W FPV Drone RC Quadcopter w/HD Camera Live Video One Key Off / Landing", <br
            />"<b>shortDescription</b>": "1 U42W Quadcopter. Syma X5SW-V3 Wifi FPV RC Drone Quadcopter 2.4Ghz 6-Axis Gyro
            with Headless Mode. Syma X20 Pocket Drone 2.4Ghz Mini RC Quadcopter Headless Mode Altitude Hold. One Key Take
            Off / Landing function: allow beginner to easy to fly the drone without any skill.",</code>       <br /><br
            /><b>Restriction: </b> This field is returned by the <b> search</b> method only when <b> fieldgroups</b> =
            <code>EXTENDED</code>.
        thumbnail_images (Union[Unset, List[Image]]): An array of thumbnail images for the item.
        title (Union[Unset, str]): The seller-created title of the item. <br><br><b>Maximum Length: </b> 80 characters
        top_rated_buying_experience (Union[Unset, bool]): This indicates if the item is a top-rated plus item. There are
            three benefits of a top-rated plus item: a  minimum 30-day money-back return policy, shipping the item in 1
            business day with tracking provided, and the added comfort of knowing that this item is from an experienced
            seller with the highest buyer ratings. See the <a href="https://pages.ebay.com/topratedplus/index.html "
            target="_blank">Top Rated Plus Items </a> and <a href="https://pages.ebay.com/help/sell/top-rated.html "
            target="_blank">Becoming a Top Rated Seller and qualifying for Top Rated Plus</a> help topics for more
            information.
        tyre_label_image_url (Union[Unset, str]): The URL to the image that shows the information on the tyre label.
        unit_price (Union[Unset, ConvertedAmount]): This type defines the monetary value of an amount. It can provide
            the amount in both the currency used on the eBay site where an item is being offered and the conversion of that
            value into another currency, if applicable.
        unit_pricing_measure (Union[Unset, str]): The designation, such as size, weight, volume, count, etc., that was
            used to specify the quantity of the item. This helps buyers compare prices. <br /><br />For example, the
            following tells the buyer that the item is 7.99 per 100 grams. <br /><br /><code>"unitPricingMeasure":
            "100g",<br /> "unitPrice": {<br />&nbsp;&nbsp;"value": "7.99",<br />&nbsp;&nbsp;"currency": "GBP"</code>
        watch_count (Union[Unset, int]): The number of users that have added the item to their watch list.<br /><br
            /><span class="tablenote"> <strong>Note:</strong> This field is restricted to applications that have been
            granted permission to access this feature. You must submit an <a
            href="https://developer.ebay.com/my/support/tickets?tab=app-check ">App Check ticket</a> to request this access.
            In the App Check form, add a note to the <b>Application Title/Summary</b> and/or <b>Application Details</b>
            fields that you want access to Watch Count data in the Browse API.</span>
    """

    additional_images: Union[Unset, List[Image]] = UNSET
    adult_only: Union[Unset, bool] = UNSET
    available_coupons: Union[Unset, bool] = UNSET
    bid_count: Union[Unset, int] = UNSET
    buying_options: Union[Unset, List[str]] = UNSET
    categories: Union[Unset, List[Category]] = UNSET
    compatibility_match: Union[Unset, str] = UNSET
    compatibility_properties: Union[Unset, List[CompatibilityProperty]] = UNSET
    condition: Union[Unset, str] = UNSET
    condition_id: Union[Unset, str] = UNSET
    current_bid_price: Union[Unset, ConvertedAmount] = UNSET
    distance_from_pickup_location: Union[Unset, TargetLocation] = UNSET
    energy_efficiency_class: Union[Unset, str] = UNSET
    epid: Union[Unset, str] = UNSET
    image: Union[Unset, Image] = UNSET
    item_affiliate_web_url: Union[Unset, str] = UNSET
    item_creation_date: Union[Unset, str] = UNSET
    item_end_date: Union[Unset, str] = UNSET
    item_group_href: Union[Unset, str] = UNSET
    item_group_type: Union[Unset, str] = UNSET
    item_href: Union[Unset, str] = UNSET
    item_id: Union[Unset, str] = UNSET
    item_location: Union[Unset, ItemLocationImpl] = UNSET
    item_web_url: Union[Unset, str] = UNSET
    leaf_category_ids: Union[Unset, List[str]] = UNSET
    legacy_item_id: Union[Unset, str] = UNSET
    listing_marketplace_id: Union[Unset, str] = UNSET
    marketing_price: Union[Unset, MarketingPrice] = UNSET
    pickup_options: Union[Unset, List[PickupOptionSummary]] = UNSET
    price: Union[Unset, ConvertedAmount] = UNSET
    price_display_condition: Union[Unset, str] = UNSET
    priority_listing: Union[Unset, bool] = UNSET
    qualified_programs: Union[Unset, List[str]] = UNSET
    seller: Union[Unset, Seller] = UNSET
    shipping_options: Union[Unset, List[ShippingOptionSummary]] = UNSET
    short_description: Union[Unset, str] = UNSET
    thumbnail_images: Union[Unset, List[Image]] = UNSET
    title: Union[Unset, str] = UNSET
    top_rated_buying_experience: Union[Unset, bool] = UNSET
    tyre_label_image_url: Union[Unset, str] = UNSET
    unit_price: Union[Unset, ConvertedAmount] = UNSET
    unit_pricing_measure: Union[Unset, str] = UNSET
    watch_count: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        additional_images: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.additional_images, Unset):
            additional_images = []
            for additional_images_item_data in self.additional_images:
                additional_images_item = additional_images_item_data.to_dict()

                additional_images.append(additional_images_item)

        adult_only = self.adult_only
        available_coupons = self.available_coupons
        bid_count = self.bid_count
        buying_options: Union[Unset, List[str]] = UNSET
        if not isinstance(self.buying_options, Unset):
            buying_options = self.buying_options

        categories: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.categories, Unset):
            categories = []
            for categories_item_data in self.categories:
                categories_item = categories_item_data.to_dict()

                categories.append(categories_item)

        compatibility_match = self.compatibility_match
        compatibility_properties: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.compatibility_properties, Unset):
            compatibility_properties = []
            for compatibility_properties_item_data in self.compatibility_properties:
                compatibility_properties_item = compatibility_properties_item_data.to_dict()

                compatibility_properties.append(compatibility_properties_item)

        condition = self.condition
        condition_id = self.condition_id
        current_bid_price: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.current_bid_price, Unset):
            current_bid_price = self.current_bid_price.to_dict()

        distance_from_pickup_location: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.distance_from_pickup_location, Unset):
            distance_from_pickup_location = self.distance_from_pickup_location.to_dict()

        energy_efficiency_class = self.energy_efficiency_class
        epid = self.epid
        image: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.image, Unset):
            image = self.image.to_dict()

        item_affiliate_web_url = self.item_affiliate_web_url
        item_creation_date = self.item_creation_date
        item_end_date = self.item_end_date
        item_group_href = self.item_group_href
        item_group_type = self.item_group_type
        item_href = self.item_href
        item_id = self.item_id
        item_location: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.item_location, Unset):
            item_location = self.item_location.to_dict()

        item_web_url = self.item_web_url
        leaf_category_ids: Union[Unset, List[str]] = UNSET
        if not isinstance(self.leaf_category_ids, Unset):
            leaf_category_ids = self.leaf_category_ids

        legacy_item_id = self.legacy_item_id
        listing_marketplace_id = self.listing_marketplace_id
        marketing_price: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.marketing_price, Unset):
            marketing_price = self.marketing_price.to_dict()

        pickup_options: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.pickup_options, Unset):
            pickup_options = []
            for pickup_options_item_data in self.pickup_options:
                pickup_options_item = pickup_options_item_data.to_dict()

                pickup_options.append(pickup_options_item)

        price: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.price, Unset):
            price = self.price.to_dict()

        price_display_condition = self.price_display_condition
        priority_listing = self.priority_listing
        qualified_programs: Union[Unset, List[str]] = UNSET
        if not isinstance(self.qualified_programs, Unset):
            qualified_programs = self.qualified_programs

        seller: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.seller, Unset):
            seller = self.seller.to_dict()

        shipping_options: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.shipping_options, Unset):
            shipping_options = []
            for shipping_options_item_data in self.shipping_options:
                shipping_options_item = shipping_options_item_data.to_dict()

                shipping_options.append(shipping_options_item)

        short_description = self.short_description
        thumbnail_images: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.thumbnail_images, Unset):
            thumbnail_images = []
            for thumbnail_images_item_data in self.thumbnail_images:
                thumbnail_images_item = thumbnail_images_item_data.to_dict()

                thumbnail_images.append(thumbnail_images_item)

        title = self.title
        top_rated_buying_experience = self.top_rated_buying_experience
        tyre_label_image_url = self.tyre_label_image_url
        unit_price: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.unit_price, Unset):
            unit_price = self.unit_price.to_dict()

        unit_pricing_measure = self.unit_pricing_measure
        watch_count = self.watch_count

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if additional_images is not UNSET:
            field_dict["additionalImages"] = additional_images
        if adult_only is not UNSET:
            field_dict["adultOnly"] = adult_only
        if available_coupons is not UNSET:
            field_dict["availableCoupons"] = available_coupons
        if bid_count is not UNSET:
            field_dict["bidCount"] = bid_count
        if buying_options is not UNSET:
            field_dict["buyingOptions"] = buying_options
        if categories is not UNSET:
            field_dict["categories"] = categories
        if compatibility_match is not UNSET:
            field_dict["compatibilityMatch"] = compatibility_match
        if compatibility_properties is not UNSET:
            field_dict["compatibilityProperties"] = compatibility_properties
        if condition is not UNSET:
            field_dict["condition"] = condition
        if condition_id is not UNSET:
            field_dict["conditionId"] = condition_id
        if current_bid_price is not UNSET:
            field_dict["currentBidPrice"] = current_bid_price
        if distance_from_pickup_location is not UNSET:
            field_dict["distanceFromPickupLocation"] = distance_from_pickup_location
        if energy_efficiency_class is not UNSET:
            field_dict["energyEfficiencyClass"] = energy_efficiency_class
        if epid is not UNSET:
            field_dict["epid"] = epid
        if image is not UNSET:
            field_dict["image"] = image
        if item_affiliate_web_url is not UNSET:
            field_dict["itemAffiliateWebUrl"] = item_affiliate_web_url
        if item_creation_date is not UNSET:
            field_dict["itemCreationDate"] = item_creation_date
        if item_end_date is not UNSET:
            field_dict["itemEndDate"] = item_end_date
        if item_group_href is not UNSET:
            field_dict["itemGroupHref"] = item_group_href
        if item_group_type is not UNSET:
            field_dict["itemGroupType"] = item_group_type
        if item_href is not UNSET:
            field_dict["itemHref"] = item_href
        if item_id is not UNSET:
            field_dict["itemId"] = item_id
        if item_location is not UNSET:
            field_dict["itemLocation"] = item_location
        if item_web_url is not UNSET:
            field_dict["itemWebUrl"] = item_web_url
        if leaf_category_ids is not UNSET:
            field_dict["leafCategoryIds"] = leaf_category_ids
        if legacy_item_id is not UNSET:
            field_dict["legacyItemId"] = legacy_item_id
        if listing_marketplace_id is not UNSET:
            field_dict["listingMarketplaceId"] = listing_marketplace_id
        if marketing_price is not UNSET:
            field_dict["marketingPrice"] = marketing_price
        if pickup_options is not UNSET:
            field_dict["pickupOptions"] = pickup_options
        if price is not UNSET:
            field_dict["price"] = price
        if price_display_condition is not UNSET:
            field_dict["priceDisplayCondition"] = price_display_condition
        if priority_listing is not UNSET:
            field_dict["priorityListing"] = priority_listing
        if qualified_programs is not UNSET:
            field_dict["qualifiedPrograms"] = qualified_programs
        if seller is not UNSET:
            field_dict["seller"] = seller
        if shipping_options is not UNSET:
            field_dict["shippingOptions"] = shipping_options
        if short_description is not UNSET:
            field_dict["shortDescription"] = short_description
        if thumbnail_images is not UNSET:
            field_dict["thumbnailImages"] = thumbnail_images
        if title is not UNSET:
            field_dict["title"] = title
        if top_rated_buying_experience is not UNSET:
            field_dict["topRatedBuyingExperience"] = top_rated_buying_experience
        if tyre_label_image_url is not UNSET:
            field_dict["tyreLabelImageUrl"] = tyre_label_image_url
        if unit_price is not UNSET:
            field_dict["unitPrice"] = unit_price
        if unit_pricing_measure is not UNSET:
            field_dict["unitPricingMeasure"] = unit_pricing_measure
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

        adult_only = d.pop("adultOnly", UNSET)

        available_coupons = d.pop("availableCoupons", UNSET)

        bid_count = d.pop("bidCount", UNSET)

        buying_options = cast(List[str], d.pop("buyingOptions", UNSET))

        categories = []
        _categories = d.pop("categories", UNSET)
        for categories_item_data in _categories or []:
            categories_item = Category.from_dict(categories_item_data)

            categories.append(categories_item)

        compatibility_match = d.pop("compatibilityMatch", UNSET)

        compatibility_properties = []
        _compatibility_properties = d.pop("compatibilityProperties", UNSET)
        for compatibility_properties_item_data in _compatibility_properties or []:
            compatibility_properties_item = CompatibilityProperty.from_dict(compatibility_properties_item_data)

            compatibility_properties.append(compatibility_properties_item)

        condition = d.pop("condition", UNSET)

        condition_id = d.pop("conditionId", UNSET)

        _current_bid_price = d.pop("currentBidPrice", UNSET)
        current_bid_price: Union[Unset, ConvertedAmount]
        if isinstance(_current_bid_price, Unset):
            current_bid_price = UNSET
        else:
            current_bid_price = ConvertedAmount.from_dict(_current_bid_price)

        _distance_from_pickup_location = d.pop("distanceFromPickupLocation", UNSET)
        distance_from_pickup_location: Union[Unset, TargetLocation]
        if isinstance(_distance_from_pickup_location, Unset):
            distance_from_pickup_location = UNSET
        else:
            distance_from_pickup_location = TargetLocation.from_dict(_distance_from_pickup_location)

        energy_efficiency_class = d.pop("energyEfficiencyClass", UNSET)

        epid = d.pop("epid", UNSET)

        _image = d.pop("image", UNSET)
        image: Union[Unset, Image]
        if isinstance(_image, Unset):
            image = UNSET
        else:
            image = Image.from_dict(_image)

        item_affiliate_web_url = d.pop("itemAffiliateWebUrl", UNSET)

        item_creation_date = d.pop("itemCreationDate", UNSET)

        item_end_date = d.pop("itemEndDate", UNSET)

        item_group_href = d.pop("itemGroupHref", UNSET)

        item_group_type = d.pop("itemGroupType", UNSET)

        item_href = d.pop("itemHref", UNSET)

        item_id = d.pop("itemId", UNSET)

        _item_location = d.pop("itemLocation", UNSET)
        item_location: Union[Unset, ItemLocationImpl]
        if isinstance(_item_location, Unset):
            item_location = UNSET
        else:
            item_location = ItemLocationImpl.from_dict(_item_location)

        item_web_url = d.pop("itemWebUrl", UNSET)

        leaf_category_ids = cast(List[str], d.pop("leafCategoryIds", UNSET))

        legacy_item_id = d.pop("legacyItemId", UNSET)

        listing_marketplace_id = d.pop("listingMarketplaceId", UNSET)

        _marketing_price = d.pop("marketingPrice", UNSET)
        marketing_price: Union[Unset, MarketingPrice]
        if isinstance(_marketing_price, Unset):
            marketing_price = UNSET
        else:
            marketing_price = MarketingPrice.from_dict(_marketing_price)

        pickup_options = []
        _pickup_options = d.pop("pickupOptions", UNSET)
        for pickup_options_item_data in _pickup_options or []:
            pickup_options_item = PickupOptionSummary.from_dict(pickup_options_item_data)

            pickup_options.append(pickup_options_item)

        _price = d.pop("price", UNSET)
        price: Union[Unset, ConvertedAmount]
        if isinstance(_price, Unset):
            price = UNSET
        else:
            price = ConvertedAmount.from_dict(_price)

        price_display_condition = d.pop("priceDisplayCondition", UNSET)

        priority_listing = d.pop("priorityListing", UNSET)

        qualified_programs = cast(List[str], d.pop("qualifiedPrograms", UNSET))

        _seller = d.pop("seller", UNSET)
        seller: Union[Unset, Seller]
        if isinstance(_seller, Unset):
            seller = UNSET
        else:
            seller = Seller.from_dict(_seller)

        shipping_options = []
        _shipping_options = d.pop("shippingOptions", UNSET)
        for shipping_options_item_data in _shipping_options or []:
            shipping_options_item = ShippingOptionSummary.from_dict(shipping_options_item_data)

            shipping_options.append(shipping_options_item)

        short_description = d.pop("shortDescription", UNSET)

        thumbnail_images = []
        _thumbnail_images = d.pop("thumbnailImages", UNSET)
        for thumbnail_images_item_data in _thumbnail_images or []:
            thumbnail_images_item = Image.from_dict(thumbnail_images_item_data)

            thumbnail_images.append(thumbnail_images_item)

        title = d.pop("title", UNSET)

        top_rated_buying_experience = d.pop("topRatedBuyingExperience", UNSET)

        tyre_label_image_url = d.pop("tyreLabelImageUrl", UNSET)

        _unit_price = d.pop("unitPrice", UNSET)
        unit_price: Union[Unset, ConvertedAmount]
        if isinstance(_unit_price, Unset):
            unit_price = UNSET
        else:
            unit_price = ConvertedAmount.from_dict(_unit_price)

        unit_pricing_measure = d.pop("unitPricingMeasure", UNSET)

        watch_count = d.pop("watchCount", UNSET)

        item_summary = cls(
            additional_images=additional_images,
            adult_only=adult_only,
            available_coupons=available_coupons,
            bid_count=bid_count,
            buying_options=buying_options,
            categories=categories,
            compatibility_match=compatibility_match,
            compatibility_properties=compatibility_properties,
            condition=condition,
            condition_id=condition_id,
            current_bid_price=current_bid_price,
            distance_from_pickup_location=distance_from_pickup_location,
            energy_efficiency_class=energy_efficiency_class,
            epid=epid,
            image=image,
            item_affiliate_web_url=item_affiliate_web_url,
            item_creation_date=item_creation_date,
            item_end_date=item_end_date,
            item_group_href=item_group_href,
            item_group_type=item_group_type,
            item_href=item_href,
            item_id=item_id,
            item_location=item_location,
            item_web_url=item_web_url,
            leaf_category_ids=leaf_category_ids,
            legacy_item_id=legacy_item_id,
            listing_marketplace_id=listing_marketplace_id,
            marketing_price=marketing_price,
            pickup_options=pickup_options,
            price=price,
            price_display_condition=price_display_condition,
            priority_listing=priority_listing,
            qualified_programs=qualified_programs,
            seller=seller,
            shipping_options=shipping_options,
            short_description=short_description,
            thumbnail_images=thumbnail_images,
            title=title,
            top_rated_buying_experience=top_rated_buying_experience,
            tyre_label_image_url=tyre_label_image_url,
            unit_price=unit_price,
            unit_pricing_measure=unit_pricing_measure,
            watch_count=watch_count,
        )

        item_summary.additional_properties = d
        return item_summary

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
