# MkDocs B&R Automation Studio Help Index File Generator

This is a plugin fo the MkDocs tool to automatically generate the format of files/folder structures needed for use in the B&R Automation Studio Help installation tools.

The plugin works by building the xml contents file from the navigation dictionary defined in MkDocs. The expectation is that there will be a navigation items defined in the mkdocs.yml. There is an expected format needed to support the format needed for the AS Help.

## Enabling
The plugin is enabled by adding the `- br-as-help-index-gen` to the mkdocs.yml file. This plugin is only tested to work with the mkdocs "brtheme"

## Configuration
### `HelpID`
ID of the help component. Used as the "ID" by the AS update program.
### `ComponentName`
Name of the component. No spaces can be used here. 
### `Version`
Version number to place on the index contents file.
### `ParentGuid`
This is the GUID of the parent of which the root page of the documentation will live under.
### `TargetPath`
This is the expected export directory that the documentation will live under in the AS Help. For example if the documentation being build was called "UserSample" and the expected location in the AS Help was have this live under the Technology Solutions section you would use the following parameter definition. `TargetPath: technologysolutions\ts_usersample` Where "technologysolutions" is the predefined path existing in the AS Help install and ts_usersample is the custom name of the folder we'd like the documentation to live under.

!!! Note:
    The AS Help installation system requires that the path be all lower case with no spaces. 

### `OutputPath`
The output path of the documentation relative to the mkdocs.yml file. The output structure of the documentation will be `OutputPath/Help/Help-en/targetpath/`

## Navigation Configuration
By default, MkDocs does not support sections to have index pages. It is therefore supported by using a specific format for in definition of the nav yaml. Pages themselves can be defined in the same format as normal MkDocs. The first page listed underneath the Section Name will be the page that is displayed when that section is selected in the help. In the example below, the `Section Name: 'index.md'` will be the source page for it's Section Name parent.

``` yaml
nav:
    - Section Name:
        - Section Name: 'index.md'
        - Page Name: 'SectionName/PageName.md'
        - Other Page: `SectionName/SourceFile.md
```

**This plug requires the nav section to be present in your mkdocs.yml file. Without it - the plugin will not run**