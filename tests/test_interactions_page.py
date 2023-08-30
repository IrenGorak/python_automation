from pages.interactions_page import SortablePage, SelectablePage, ResizablePage, DroppablePage


class TestInteractions:
    class TestSortablePage:
        def test_list_grid_sortable(self, driver):
            sortable_page = SortablePage(driver, "https://demoqa.com/sortable")
            sortable_page.open()
            list_before, list_after = sortable_page.change_list_order()
            grid_before, grid_after = sortable_page.change_grid_order()
            assert list_before != list_after, "The order do not change"
            assert grid_before != grid_after, "The order do not change"

    class TestSelectable:
        def test_list_grid_selectable(self, driver):
            selectable_page = SelectablePage(driver, "https://demoqa.com/selectable")
            selectable_page.open()
            item_list = selectable_page.select_list_item()
            grid_list = selectable_page.select_grid_item()
            assert len(item_list) > 0, "The element is not click or selected"
            assert len(grid_list) > 0, "The element is not click or selected"

    class TestResizable:
        def test_change_size(self, driver):
            resizable_page = ResizablePage(driver, "https://demoqa.com/resizable")
            resizable_page.open()
            max_box, min_box = resizable_page.change_resizable_box()
            max_res, min_res = resizable_page.change_resizable()
            assert ('500px', '300px') == max_box, "Max size not equal to '500px', '300px'"
            assert ('150px', '150px') == min_box, "Min size not equal '150px', '150px'"
            assert max_res != min_res, "resizable has not been change"

    class TestDroppablePage:
        def test_simple_drop_in_box(self, driver):
            droppable_page = DroppablePage(driver, "https://demoqa.com/droppable")
            droppable_page.open()
            text = droppable_page.simple_drop_into_box()
            assert text == "Dropped!", "the element is not dropped"

        def test_accept_tab_drop(self, driver):
            droppable_page = DroppablePage(driver, "https://demoqa.com/droppable")
            droppable_page.open()
            not_accept, accept = droppable_page.accept_drop_drag()
            assert not_accept == "Drop here", "the element is dropped with change text"
            assert accept == "Dropped!", "the text is ot change after the drop element"

        def test_prevent_tab(self, driver):
            droppable_page = DroppablePage(driver, "https://demoqa.com/droppable")
            droppable_page.open()
            not_greedy_big, not_greedy_small, greedy_big, greedy_small = droppable_page.prevent_drop()
            assert not_greedy_big == "Dropped!", "the element text has not change"
            assert not_greedy_small == "Dropped!", "the element text has not change"
            assert greedy_big == "Outer droppable", "the element text has change"
            assert greedy_small == "Dropped!", "the element text has not change"

        def test_revert_drop(self, driver):
            droppable_page = DroppablePage(driver, "https://demoqa.com/droppable")
            droppable_page.open()
            will_move_after, will_after_revert = droppable_page.not_will_revert_drag('will')
            not_will_after_move, not_will_after_revert = droppable_page.not_will_revert_drag('not_will')
            assert will_move_after != will_after_revert, "the element has not reverted"
            assert not_will_after_move == not_will_after_revert, "the element has reverted"
