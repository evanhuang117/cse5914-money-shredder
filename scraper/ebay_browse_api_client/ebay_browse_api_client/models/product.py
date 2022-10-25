from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.additional_product_identity import AdditionalProductIdentity
from ..models.aspect_group import AspectGroup
from ..models.image import Image
from ..types import UNSET, Unset

T = TypeVar("T", bound="Product")


@attr.s(auto_attribs=True)
class Product:
    """The type that defines the fields for the product information of the item.

    Attributes:
        additional_images (Union[Unset, List[Image]]): An array of containers with the URLs for the product images that
            are in addition to the primary image.
        additional_product_identities (Union[Unset, List[AdditionalProductIdentity]]): An array of product identifiers
            associated with the item. This container is returned if the seller has associated the eBay Product Identifier
            (ePID) with the item and in the request <b> fieldgroups</b> is set to <code>PRODUCT</code>.
        aspect_groups (Union[Unset, List[AspectGroup]]): An array of containers for the product aspects. Each group
            contains the aspect group name and the aspect name/value pairs.
        brand (Union[Unset, str]): The brand associated with product. To identify the product, this is always used along
            with MPN (manufacturer part number).
        description (Union[Unset, str]): The rich description of an eBay product, which might contain HTML.
        gtins (Union[Unset, List[str]]): An array of all the possible GTINs values associated with the product. A GTIN
            is a unique Global Trade Item number of the item as defined by <a href="https://www.gtin.info "
            target="_blank">https://www.gtin.info</a>. This can be a UPC (Universal Product Code), EAN (European Article
            Number), or an ISBN (International Standard Book Number) value.
        image (Union[Unset, Image]): Type the defines the details of an image, such as size and image URL. Currently,
            only <b> imageUrl</b> is  populated. The <b> height</b> and <b> width</b> were added for future use.
        mpns (Union[Unset, List[str]]): An array of all possible MPN values associated with the product. A MPNs is
            manufacturer part number of the product. To identify the product, this is always used along with brand.
        title (Union[Unset, str]): The title of the product.
    """

    additional_images: Union[Unset, List[Image]] = UNSET
    additional_product_identities: Union[Unset, List[AdditionalProductIdentity]] = UNSET
    aspect_groups: Union[Unset, List[AspectGroup]] = UNSET
    brand: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    gtins: Union[Unset, List[str]] = UNSET
    image: Union[Unset, Image] = UNSET
    mpns: Union[Unset, List[str]] = UNSET
    title: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        additional_images: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.additional_images, Unset):
            additional_images = []
            for additional_images_item_data in self.additional_images:
                additional_images_item = additional_images_item_data.to_dict()

                additional_images.append(additional_images_item)

        additional_product_identities: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.additional_product_identities, Unset):
            additional_product_identities = []
            for additional_product_identities_item_data in self.additional_product_identities:
                additional_product_identities_item = additional_product_identities_item_data.to_dict()

                additional_product_identities.append(additional_product_identities_item)

        aspect_groups: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.aspect_groups, Unset):
            aspect_groups = []
            for aspect_groups_item_data in self.aspect_groups:
                aspect_groups_item = aspect_groups_item_data.to_dict()

                aspect_groups.append(aspect_groups_item)

        brand = self.brand
        description = self.description
        gtins: Union[Unset, List[str]] = UNSET
        if not isinstance(self.gtins, Unset):
            gtins = self.gtins

        image: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.image, Unset):
            image = self.image.to_dict()

        mpns: Union[Unset, List[str]] = UNSET
        if not isinstance(self.mpns, Unset):
            mpns = self.mpns

        title = self.title

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if additional_images is not UNSET:
            field_dict["additionalImages"] = additional_images
        if additional_product_identities is not UNSET:
            field_dict["additionalProductIdentities"] = additional_product_identities
        if aspect_groups is not UNSET:
            field_dict["aspectGroups"] = aspect_groups
        if brand is not UNSET:
            field_dict["brand"] = brand
        if description is not UNSET:
            field_dict["description"] = description
        if gtins is not UNSET:
            field_dict["gtins"] = gtins
        if image is not UNSET:
            field_dict["image"] = image
        if mpns is not UNSET:
            field_dict["mpns"] = mpns
        if title is not UNSET:
            field_dict["title"] = title

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        additional_images = []
        _additional_images = d.pop("additionalImages", UNSET)
        for additional_images_item_data in _additional_images or []:
            additional_images_item = Image.from_dict(additional_images_item_data)

            additional_images.append(additional_images_item)

        additional_product_identities = []
        _additional_product_identities = d.pop("additionalProductIdentities", UNSET)
        for additional_product_identities_item_data in _additional_product_identities or []:
            additional_product_identities_item = AdditionalProductIdentity.from_dict(
                additional_product_identities_item_data
            )

            additional_product_identities.append(additional_product_identities_item)

        aspect_groups = []
        _aspect_groups = d.pop("aspectGroups", UNSET)
        for aspect_groups_item_data in _aspect_groups or []:
            aspect_groups_item = AspectGroup.from_dict(aspect_groups_item_data)

            aspect_groups.append(aspect_groups_item)

        brand = d.pop("brand", UNSET)

        description = d.pop("description", UNSET)

        gtins = cast(List[str], d.pop("gtins", UNSET))

        _image = d.pop("image", UNSET)
        image: Union[Unset, Image]
        if isinstance(_image, Unset):
            image = UNSET
        else:
            image = Image.from_dict(_image)

        mpns = cast(List[str], d.pop("mpns", UNSET))

        title = d.pop("title", UNSET)

        product = cls(
            additional_images=additional_images,
            additional_product_identities=additional_product_identities,
            aspect_groups=aspect_groups,
            brand=brand,
            description=description,
            gtins=gtins,
            image=image,
            mpns=mpns,
            title=title,
        )

        product.additional_properties = d
        return product

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
