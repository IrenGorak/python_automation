from selenium.webdriver.common.by import By


class SortablePageLocators:
    TAB_LIST = (By.CSS_SELECTOR, "a[idd='demo-tab-list']")
    LIST_ITEM = (By.CSS_SELECTOR, "div[id='demo-tabpane-list']  div [class='list-group-item list-group-item-action']")
    TAB_GRID = (By.CSS_SELECTOR, "a[id='demo-tab-grid']")
    GRID_ITEM = (By.CSS_SELECTOR, "div[id='demo-tabpane-grid']  div [class='list-group-item list-group-item-action']")


class SelectablePageLocators:
    TAB_LIST = (By.CSS_SELECTOR, "a[id='demo-tab-list']")
    LIST_TEM = (By.CSS_SELECTOR, "li[class='mt-2 list-group-item list-group-item-action']")
    ACTIVE_LIST_ITEM = (By.CSS_SELECTOR, "li[class='mt-2 list-group-item active list-group-item-action']")
    TAB_GRID = (By.CSS_SELECTOR, "a[id='demo-tab-grid']")
    GRID_ITEM = (By.CSS_SELECTOR, "li[class='list-group-item list-group-item-action']")
    GRID_ACTIVE_ITEM = (By.CSS_SELECTOR, "li[class='list-group-item active list-group-item-action']")


class ResizablePageLocators:
    RESIZABLE_BOX = (By.CSS_SELECTOR, "div[id='resizableBoxWithRestriction']")
    RESIZABLE_BOX_HANDLE = (By.CSS_SELECTOR, "div[class='constraint-area'] "
                                             "span[class='react-resizable-handle react-resizable-handle-se']")
    RESIZABLE = (By.CSS_SELECTOR, "div[id='resizable']")
    RESIZABLE_HANDLE = (By.CSS_SELECTOR, "div[id='resizable'] "
                                         "span[class='react-resizable-handle react-resizable-handle-se']")


class DroppablePageLocators:
    SIMPLE_TAB = (By.CSS_SELECTOR, "a[id='droppableExample-tab-simple']")
    SIMPLE_DRAG_ME = (By.CSS_SELECTOR, "div[id='draggable']")
    SIMPLE_DROP_HERE = (By.CSS_SELECTOR, "#simpleDropContainer #droppable")

    ACCEPT_TAB = (By.CSS_SELECTOR, "a[id='droppableExample-tab-accept']")
    ACCEPTABLE = (By.CSS_SELECTOR, "div[id='acceptable']")
    NOT_ACCEPTABLE = (By.CSS_SELECTOR, "div[id='notAcceptable']")
    ACCEPT_DROP_HERE = (By.CSS_SELECTOR, "#acceptDropContainer #droppable")

    PREVENT_TAB = (By.CSS_SELECTOR, "a[id='droppableExample-tab-preventPropogation']")
    PREVENT_DRAG_ME = (By.CSS_SELECTOR, "#ppDropContainer #dragBox")
    FIRST_BOX_TEXT = (By.CSS_SELECTOR, "div[id='notGreedyDropBox'] p:nth-child(1)")
    NOT_GREEDY_BOX = (By.CSS_SELECTOR, 'div[id="notGreedyInnerDropBox"]')
    GREEDY_BOX = (By.CSS_SELECTOR, "div[id='greedyDropBoxInner']")
    SECOND_BOX_TEXT = (By.CSS_SELECTOR, "div[id='greedyDropBox'] p:nth-child(1)")

    REVER_TAB = (By.CSS_SELECTOR, "a[id='droppableExample-tab-revertable']")
    REVER_DRAG_ME = (By.CSS_SELECTOR, "div[id='draggable']")
    WILl_REVERT = (By.CSS_SELECTOR, "div[id='revertable']")
    NOT_REVERT = (By.CSS_SELECTOR, "div[id='notRevertable']")
    REVERT_DROP_HERE = (By.CSS_SELECTOR, "#revertableDropContainer #droppable")


class DragabblePageLocators:
    SIMPLE_DRAG = (By.CSS_SELECTOR, "#draggableExample-tabpane-simple #dragBox")

    AXIS_TAB = (By.CSS_SELECTOR, "a[id='draggableExample-tab-axisRestriction']")
    AXIS_X = (By.CSS_SELECTOR, "div[id='restrictedX']")
    AXIS_Y = (By.CSS_SELECTOR, "div[id='restrictedY']")

