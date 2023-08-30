import random
import time

from locators.interactions_page_locators import SortablePageLocators, SelectablePageLocators, ResizablePageLocators, \
    DroppablePageLocators
from pages.base_page import BasePage


class SortablePage(BasePage):
    locators = SortablePageLocators()

    def get_sortable_items(self, elements):
        item_list = self.elements_are_visible(elements)
        return [item.text for item in item_list]

    def change_list_order(self):
        order_before = self.get_sortable_items(self.locators.LIST_ITEM)
        item_list = random.sample(self.elements_are_visible(self.locators.LIST_ITEM), k=2)
        item_what = item_list[0]
        item_where = item_list[1]
        self.action_drag_and_drop_to_element(item_what, item_where)
        order_after = self.get_sortable_items(self.locators.LIST_ITEM)
        print(order_before, order_after)
        return order_before, order_after

    def change_grid_order(self):
        order_before = self.element_is_visible(self.locators.TAB_GRID).click()
        item_list = random.sample(self.elements_are_visible(self.locators.GRID_ITEM), k=3)
        item_what = item_list[0]
        item_where = item_list[1]
        self.action_drag_and_drop_to_element(item_what, item_where)
        order_after = self.get_sortable_items(self.locators.GRID_ITEM)
        print(order_before, order_after)
        return order_before, order_after


class SelectablePage(BasePage):
    locators = SelectablePageLocators()

    def click_selectable_item(self, elements):
        item_list = self.elements_are_visible(elements)
        random.sample(item_list, k=1)[0].click()

    def select_list_item(self):
        self.click_selectable_item(self.locators.LIST_TEM)
        active_element = self.element_is_visible(self.locators.ACTIVE_LIST_ITEM)
        print(active_element.text)
        return active_element.text

    def select_grid_item(self):
        self.element_is_visible(self.locators.TAB_GRID).click()
        self.click_selectable_item(self.locators.GRID_ITEM)
        active_element = self.element_is_visible(self.locators.GRID_ACTIVE_ITEM)
        print(active_element.text)
        return active_element.text


class ResizablePage(BasePage):
    locators = ResizablePageLocators()

    def get_pixel_from_width_height(self, value):
        width = value.split(";")[0].split(':')[1].replace(' ', '')
        height = value.split(";")[1].split(':')[1].replace(' ', '')
        return width, height

    def get_max_min_size(self, element):
        size = self.element_is_present(element)
        size_value = size.get_attribute('style')
        return size_value

    def change_resizable_box(self):
        self.action_drag_and_drop_by_offset(self.element_is_present(self.locators.RESIZABLE_BOX_HANDLE), 400, 200)
        max_size = self.get_pixel_from_width_height(self.get_max_min_size(self.locators.RESIZABLE_BOX))

        self.action_drag_and_drop_by_offset(self.element_is_present(self.locators.RESIZABLE_BOX_HANDLE), -500, -300)
        min_size = self.get_pixel_from_width_height(self.get_max_min_size(self.locators.RESIZABLE_BOX))
        print(max_size, min_size)
        return max_size, min_size

    def change_resizable(self):
        self.action_drag_and_drop_by_offset(self.element_is_visible(self.locators.RESIZABLE_HANDLE),
                                            random.randint(1, 300), random.randint(1, 300))
        max_size = self.get_pixel_from_width_height(self.get_max_min_size(self.locators.RESIZABLE))

        self.action_drag_and_drop_by_offset(self.element_is_visible(self.locators.RESIZABLE_HANDLE),
                                            random.randint(-200, -1), random.randint(-200, -1))
        min_size = self.get_pixel_from_width_height(self.get_max_min_size(self.locators.RESIZABLE))
        print(max_size, min_size)
        return max_size, min_size


class DroppablePage(BasePage):
    locators = DroppablePageLocators()

    def simple_drop_into_box(self):
        drag_div = self.element_is_visible(self.locators.SIMPLE_DRAG_ME)
        drop_div = self.element_is_visible(self.locators.SIMPLE_DROP_HERE)
        self.action_drag_and_drop_to_element(drag_div, drop_div)
        return drop_div.text

    def accept_drop_drag(self):
        self.element_is_visible(self.locators.ACCEPT_TAB).click()
        acceptable_div = self.element_is_visible(self.locators.ACCEPTABLE)
        not_acceptable = self.element_is_visible(self.locators.NOT_ACCEPTABLE)
        drop_div = self.element_is_visible(self.locators.ACCEPT_DROP_HERE)
        self.action_drag_and_drop_to_element(not_acceptable, drop_div)
        not_accept_text = drop_div.text
        self.action_drag_and_drop_to_element(acceptable_div, drop_div)
        accept_text = drop_div.text
        return not_accept_text, accept_text

    def prevent_drop(self):
        self.element_is_visible(self.locators.PREVENT_TAB).click()
        drag_div = self.element_is_visible(self.locators.PREVENT_DRAG_ME)
        not_greedy_inner_box = self.element_is_visible(self.locators.NOT_GREEDY_BOX)
        greedy_inner_box = self.element_is_visible(self.locators.GREEDY_BOX)
        self.action_drag_and_drop_to_element(drag_div, not_greedy_inner_box)
        text_not_greedy_big = self.element_is_visible(self.locators.FIRST_BOX_TEXT).text
        text_not_greedy_small = not_greedy_inner_box.text
        self.action_drag_and_drop_to_element(drag_div, greedy_inner_box)
        text_greedy_big = self.element_is_visible(self.locators.SECOND_BOX_TEXT).text
        text_greedy_small = greedy_inner_box.text
        return text_not_greedy_big,text_not_greedy_small, text_greedy_big, text_greedy_small

    def not_will_revert_drag(self, type_drag):

        drags = {'will':
                      {'revert': self.locators.WILl_REVERT, },
                 'not_will':
                     {'revert': self.locators.NOT_REVERT, },
                 }
        self.element_is_visible(self.locators.REVER_TAB).click()
        revert = self.element_is_visible(drags[type_drag]['revert'])
        drop_div = self.element_is_visible(self.locators.REVERT_DROP_HERE)
        self.action_drag_and_drop_to_element(revert, drop_div)
        position_after_move = revert.get_attribute('style')
        time.sleep(2)
        position_after_revert = revert.get_attribute('style')
        print(position_after_move, position_after_revert)
        return position_after_move, position_after_revert
