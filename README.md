# max-component
[![hacs_badge](https://img.shields.io/badge/HACS-Default-orange.svg)](https://github.com/custom-components/hacs)
## Introduction
This is a custom component for Home Assistant, that is used for controlling your MAX! devices.

## Installation

### Step 1: Download files

#### Option 1: Via HACS

Make sure you have HACS installed. If you don't, run `curl -sfSL https://hacs.xyz/install | bash -` in HA.  
Choose Integrations under HACS. Then hit the plus button, search for "scheduler", choose it, and hit install in HACS.

#### Option 2: Manual
Clone this repository or download the source code as a zip file and add/merge the `custom_components/` folder with its contents in your configuration directory.


### Step 2: Restart HA
In order for the newly added integration to be loaded, HA needs to be restarted.

### Step 3: Add integration
In HA, go to Configuration > Integrations.
In the bottom right corner, click on the big button with a '+'.

If the component is properly installed, you should be able to find the 'Scheduler integration' in the list.

Select it, and the scheduler integration is ready for use.

### Step 4: Add the scheduler-card

## Max! entities


### States


### Services

