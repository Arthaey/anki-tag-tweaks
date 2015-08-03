# Description

An Anki add-on to slightly modify how the browse window handles tags. (Note: this
add-on assumes you also have the HierarchicalTags add-on installed.)

```python
FEATURES = {
    "collapseSearchesByDefault": True,
    "expandTagsByDefault": True,
    "refreshTagListAfterDeletingTag": True,
    "rightClickToRename": True,
    "rightClickToDelete": True,
}
```

# TODO

- use the configured separator for HierarchicalTags, not "::"
- right-click on tag to rename it
- right-click on tag to delete it
- UI for users to configure add-on without editing the code
