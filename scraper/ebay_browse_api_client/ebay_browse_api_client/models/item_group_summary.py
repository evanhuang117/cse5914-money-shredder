from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.image import Image
from ..types import UNSET, Unset

T = TypeVar("T", bound="ItemGroupSummary")


@attr.s(auto_attribs=True)
class ItemGroupSummary:
    """The type that defines the fields for the details of each item in an item group. An item group is  an item that has
    various aspect differences, such as color, size, storage capacity, etc. When an item group is created, one of the
    item variations, such as the red shirt size L, is chosen as the "parent". All the other items in the group are the
    children, such as the blue shirt size L, red shirt size M, etc. <br /><br /><span class="tablenote"><b> Note: </b>
    This container is returned only if the <b> item_id</b> in the request is an item group (parent ID of an item with
    variations).</span>

        Attributes:
            item_group_additional_images (Union[Unset, List[Image]]): An array of containers with the URLs for images that
                are in addition to the primary image of the item group.  The primary image is returned in the <b>
                itemGroupImage</b> field.
            item_group_href (Union[Unset, str]): The HATEOAS reference of the parent page of the item group. An item group
                is an item that has various aspect differences, such as color, size, storage capacity, etc.
            item_group_id (Union[Unset, str]): The unique identifier for the item group. An item group is an item that has
                various aspect differences, such as color, size, storage capacity, etc.
            item_group_image (Union[Unset, Image]): Type the defines the details of an image, such as size and image URL.
                Currently,  only <b> imageUrl</b> is  populated. The <b> height</b> and <b> width</b> were added for future use.
            item_group_title (Union[Unset, str]): The title of the item that appears on the item group page. An item group
                is an item that has various aspect differences, such as color, size, storage capacity, etc.
            item_group_type (Union[Unset, str]): An enumeration value that indicates the type of the item group. An item
                group is an item that has various aspect differences, such as color, size, storage capacity, etc. For
                implementation help, refer to <a href='https://developer.ebay.com/api-
                docs/buy/browse/types/gct:ItemGroupTypeEnum'>eBay API documentation</a>
    """

    item_group_additional_images: Union[Unset, List[Image]] = UNSET
    item_group_href: Union[Unset, str] = UNSET
    item_group_id: Union[Unset, str] = UNSET
    item_group_image: Union[Unset, Image] = UNSET
    item_group_title: Union[Unset, str] = UNSET
    item_group_type: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        item_group_additional_images: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.item_group_additional_images, Unset):
            item_group_additional_images = []
            for item_group_additional_images_item_data in self.item_group_additional_images:
                item_group_additional_images_item = item_group_additional_images_item_data.to_dict()

                item_group_additional_images.append(item_group_additional_images_item)

        item_group_href = self.item_group_href
        item_group_id = self.item_group_id
        item_group_image: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.item_group_image, Unset):
            item_group_image = self.item_group_image.to_dict()

        item_group_title = self.item_group_title
        item_group_type = self.item_group_type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if item_group_additional_images is not UNSET:
            field_dict["itemGroupAdditionalImages"] = item_group_additional_images
        if item_group_href is not UNSET:
            field_dict["itemGroupHref"] = item_group_href
        if item_group_id is not UNSET:
            field_dict["itemGroupId"] = item_group_id
        if item_group_image is not UNSET:
            field_dict["itemGroupImage"] = item_group_image
        if item_group_title is not UNSET:
            field_dict["itemGroupTitle"] = item_group_title
        if item_group_type is not UNSET:
            field_dict["itemGroupType"] = item_group_type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        item_group_additional_images = []
        _item_group_additional_images = d.pop("itemGroupAdditionalImages", UNSET)
        for item_group_additional_images_item_data in _item_group_additional_images or []:
            item_group_additional_images_item = Image.from_dict(item_group_additional_images_item_data)

            item_group_additional_images.append(item_group_additional_images_item)

        item_group_href = d.pop("itemGroupHref", UNSET)

        item_group_id = d.pop("itemGroupId", UNSET)

        _item_group_image = d.pop("itemGroupImage", UNSET)
        item_group_image: Union[Unset, Image]
        if isinstance(_item_group_image, Unset):
            item_group_image = UNSET
        else:
            item_group_image = Image.from_dict(_item_group_image)

        item_group_title = d.pop("itemGroupTitle", UNSET)

        item_group_type = d.pop("itemGroupType", UNSET)

        item_group_summary = cls(
            item_group_additional_images=item_group_additional_images,
            item_group_href=item_group_href,
            item_group_id=item_group_id,
            item_group_image=item_group_image,
            item_group_title=item_group_title,
            item_group_type=item_group_type,
        )

        item_group_summary.additional_properties = d
        return item_group_summary

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
