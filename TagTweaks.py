# See github page to report issues or to contribute:
# https://github.com/Arthaey/anki-tag-tweaks

from anki.hooks import wrap
from anki.lang import _
from aqt.browser import Browser
from PyQt4.QtCore import Qt

import pprint, sys # DELETE
pp = pprint.PrettyPrinter(indent = 2, stream=sys.stderr) # DELETE

FEATURES = {
    "collapseSearchesByDefault": True,
    "expandTagsByDefault": True,
    "rightClickToRename": True,
    "rightClickToDelete": True,
}

def _collapseSearchesByDefault(self, root):
    if FEATURES["collapseSearchesByDefault"]:
        searches = root.findItems(_("My Searches"), Qt.MatchFixedString)[0]
        root.collapseItem(searches)

def _expandTagsByDefault(self, root):
   if FEATURES["expandTagsByDefault"]:
       root.expandAll()
        # It's a pain to fully expand each tag, so just re-collapse if needed.
       _collapseSearchesByDefault(self, root)

#def _rightClickToRename(self, root):
#    if FEATURES["rightClickToRename"]:
#        # TO IMPLEMENT

#def _rightClickToDelete(self, root):
#    if FEATURES["rightClickToDelete"]:
#        # TO IMPLEMENT


Browser._favTree = wrap(Browser._favTree, _collapseSearchesByDefault, "after")

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
Browser._userTagTree = wrap(Browser._userTagTree, _expandTagsByDefault, "after")
