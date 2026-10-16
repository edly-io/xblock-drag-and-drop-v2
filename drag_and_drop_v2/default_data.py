""" Default data for Drag and Drop v2 XBlock """
from urllib.parse import quote

from .utils import _

TARGET_IMG_DESCRIPTION = _(
    "Three drop zones stacked from top to bottom: The Top Zone, The Middle Zone and The Bottom Zone."
)

# The default background is one Studio's editor would generate ("Generate image automatically"): one column of
# three 350 x 120 zones, 20px apart. The data-* attributes are what the editor reads back to fill in its inputs.
AUTOZONE_COLS = 1
AUTOZONE_ROWS = 3
AUTOZONE_WIDTH = 350
AUTOZONE_HEIGHT = 120
AUTOZONE_PADDING = 20


def _autozone_rect(row):
    """ The (x, y, width, height) of the zone in the given row of the default layout. """
    return (
        AUTOZONE_PADDING,
        AUTOZONE_PADDING + row * (AUTOZONE_HEIGHT + AUTOZONE_PADDING),
        AUTOZONE_WIDTH,
        AUTOZONE_HEIGHT,
    )


def _autozone_background():
    """ The data URI of the default generated background, as the editor's autozone template draws it. """
    width = AUTOZONE_WIDTH * AUTOZONE_COLS + AUTOZONE_PADDING * (AUTOZONE_COLS + 1)
    height = AUTOZONE_HEIGHT * AUTOZONE_ROWS + AUTOZONE_PADDING * (AUTOZONE_ROWS + 1)
    rects = "".join(
        f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="#f7f7f7" rx="10" ry="10" '
        f'stroke="#d6d6d6" stroke-width="2" stroke-dasharray="3,3" />'
        for x, y, w, h in (_autozone_rect(row) for row in range(AUTOZONE_ROWS))
    )
    svg = (
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" data-producer="dndv2" '
        f'data-cols="{AUTOZONE_COLS}" data-rows="{AUTOZONE_ROWS}" '
        f'data-zone_width="{AUTOZONE_WIDTH}" data-zone_height="{AUTOZONE_HEIGHT}">'
        f'<rect x="0" y="0" width="100%" height="100%" fill="#fff" />{rects}</svg>'
    )
    return "data:image/svg+xml," + quote(svg, safe="")


def _autozone(row, uid, title, description):
    """ A zone of the default layout. """
    x, y, width, height = _autozone_rect(row)
    return {
        "uid": uid,
        "title": title,
        "description": description,
        "x": x,
        "y": y,
        "width": width,
        "height": height,
        "align": "center",
    }


TOP_ZONE_ID = "top"
MIDDLE_ZONE_ID = "middle"
BOTTOM_ZONE_ID = "bottom"

TOP_ZONE_TITLE = _("The Top Zone")
MIDDLE_ZONE_TITLE = _("The Middle Zone")
BOTTOM_ZONE_TITLE = _("The Bottom Zone")

TOP_ZONE_DESCRIPTION = _("Use this zone for items that go at the top.")
MIDDLE_ZONE_DESCRIPTION = _("Use this zone for items that go in the middle.")
BOTTOM_ZONE_DESCRIPTION = _("Use this zone for items that go at the bottom.")

ITEM_CORRECT_FEEDBACK_TOP = _("Correct! This one belongs to The Top Zone.")
ITEM_CORRECT_FEEDBACK_MIDDLE = _("Correct! This one belongs to The Middle Zone.")
ITEM_CORRECT_FEEDBACK_BOTTOM = _("Correct! This one belongs to The Bottom Zone.")
ITEM_INCORRECT_FEEDBACK = _("No, this item does not belong here. Try again.")
ITEM_NO_ZONE_FEEDBACK = _("You silly, there are no zones for this one.")
ITEM_ANY_ZONE_FEEDBACK = _("Of course it goes here! It goes anywhere!")

ITEM_TOP_ZONE_NAME = _("Goes to the top")
ITEM_MIDDLE_ZONE_NAME = _("Goes to the middle")
ITEM_BOTTOM_ZONE_NAME = _("Goes to the bottom")
ITEM_ANY_ZONE_NAME = _("Goes anywhere")
ITEM_NO_ZONE_NAME = _("I don't belong anywhere")

START_FEEDBACK = _("Drag the items onto the image above.")
FINISH_FEEDBACK = _("Good work! You have completed this drag and drop problem.")

DEFAULT_DATA = {
    "targetImg": _autozone_background(),
    "targetImgDescription": TARGET_IMG_DESCRIPTION,
    # The generated background is blank, so the zone titles are what tells learners the zones apart.
    "displayLabels": True,
    "zones": [
        _autozone(0, TOP_ZONE_ID, TOP_ZONE_TITLE, TOP_ZONE_DESCRIPTION),
        _autozone(1, MIDDLE_ZONE_ID, MIDDLE_ZONE_TITLE, MIDDLE_ZONE_DESCRIPTION),
        _autozone(2, BOTTOM_ZONE_ID, BOTTOM_ZONE_TITLE, BOTTOM_ZONE_DESCRIPTION),
    ],
    "items": [
        {
            "displayName": ITEM_TOP_ZONE_NAME,
            "feedback": {
                "incorrect": ITEM_INCORRECT_FEEDBACK,
                "correct": ITEM_CORRECT_FEEDBACK_TOP
            },
            "zones": [
                TOP_ZONE_ID
            ],
            "imageURL": "",
            "id": 0,
        },
        {
            "displayName": ITEM_MIDDLE_ZONE_NAME,
            "feedback": {
                "incorrect": ITEM_INCORRECT_FEEDBACK,
                "correct": ITEM_CORRECT_FEEDBACK_MIDDLE
            },
            "zones": [
                MIDDLE_ZONE_ID
            ],
            "imageURL": "",
            "id": 1,
        },
        {
            "displayName": ITEM_BOTTOM_ZONE_NAME,
            "feedback": {
                "incorrect": ITEM_INCORRECT_FEEDBACK,
                "correct": ITEM_CORRECT_FEEDBACK_BOTTOM
            },
            "zones": [
                BOTTOM_ZONE_ID
            ],
            "imageURL": "",
            "id": 2,
        },
        {
            "displayName": ITEM_ANY_ZONE_NAME,
            "feedback": {
                "incorrect": "",
                "correct": ITEM_ANY_ZONE_FEEDBACK
            },
            "zones": [
                TOP_ZONE_ID,
                BOTTOM_ZONE_ID,
                MIDDLE_ZONE_ID
            ],
            "imageURL": "",
            "id": 3
        },
        {
            "displayName": ITEM_NO_ZONE_NAME,
            "feedback": {
                "incorrect": ITEM_NO_ZONE_FEEDBACK,
                "correct": ""
            },
            "zones": [],
            "imageURL": "",
            "id": 4,
        },
    ],
    "feedback": {
        "start": START_FEEDBACK,
        "finish": FINISH_FEEDBACK,
    },
}
