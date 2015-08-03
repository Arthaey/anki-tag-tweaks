# -*- coding: utf-8 -*-
# See github page to report issues or to contribute:
# https://github.com/Arthaey/anki-tag-tweaks
#
# Also available for Anki at https://ankiweb.net/shared/info/1384323610

from anki.hooks import wrap
from anki.lang import _
from anki.tags import TagManager
from aqt.browser import Browser
from aqt.utils import showInfo
from PyQt4.QtCore import Qt

FEATURES = {
    "collapseSearchesByDefault": True,
    "expandTagsByDefault": True,
    "refreshTagListAfterDeletingTag": True,
    "rightClickToRename": False, # TO BE IMPLEMENTED
    "rightClickToDelete": False, # TO BE IMPLEMENTED
}

def _collapseSearchesByDefault(self, root):
    match = root.findItems(_("My Searches"), Qt.MatchFixedString)
    if match:
        searches = match[0]
        root.collapseItem(searches)

def _expandTagsByDefault(self, root):
   root.expandAll()
    # It's a pain to fully expand each tag, so just re-collapse if needed.
   _collapseSearchesByDefault(self, root)

def _refreshTagListAfterDeletingTag(self, ids, tags, add=True):
    self.col.fixIntegrity()

def _rightClickToRename(self, root):
    showInfo("This feature has not been implemented yet.")

def _rightClickToDelete(self, root):
    showInfo("This feature has not been implemented yet.")


if FEATURES["refreshTagListAfterDeletingTag"]:
    TagManager.bulkAdd = wrap(TagManager.bulkAdd, _refreshTagListAfterDeletingTag, "after")

if FEATURES["collapseSearchesByDefault"]:
    Browser._favTree = wrap(Browser._favTree, _collapseSearchesByDefault, "after")

if FEATURES["rightClickToRename"]:
    Browser._userTagTree = wrap(Browser._userTagTree, _rightClickToRename, "after")

if FEATURES["rightClickToDelete"]:
    Browser._userTagTree = wrap(Browser._userTagTree, _rightClickToDelete, "after")

# This HAPPENS to work because "TagTweaks" is alphabetically after
# "HierarchicalTags" and os.listdir usually(?) returns the directory listing in
# alphabetical order.  However, the official Python docs say this order is NOT
# guaranteed.
#
# But I don't see how an addon can change or enforce the order in which addons
# are loaded, because it obivously won't run until AFTER it has been loaded, at
# which point it could be too late.
#
# So, the conclusion is to ensure this filename comes after HierarchicalTags's
# and to cross my fingers. :(
#
if FEATURES["expandTagsByDefault"]:
    Browser._userTagTree = wrap(Browser._userTagTree, _expandTagsByDefault, "after")
