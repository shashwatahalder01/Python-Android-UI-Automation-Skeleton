from pathlib import Path

# User file
userData = Path(__file__).parent / "userdata.xlsx"
emailUserNamesheetName = 'User_Data'
timeMessagesheetName = 'User_Data_2'


class Data(object):
    # Apk path

    gChat = Path(__file__).parent.parent / 'apk/GoogleChat.apk'
    Skype = Path(__file__).parent.parent / 'apk/Skype.apk'
    Viber = Path(__file__).parent.parent / 'apk/Viber.apk'
    Messages = Path(__file__).parent.parent / 'apk/Messages.xapk'

    # App package and App activity

    gChatAppPackage = 'com.google.android.apps.dynamite'
    gChatAppActivity = 'com.google.android.apps.dynamite.startup.StartUpActivity'
    skypeAppPackage = 'com.skype.raider'
    skypeAppActivity = 'com.skype4life.MainActivity'
    viberAppPackage = 'com.viber.voip'
    viberAppActivity = 'com.viber.voip.HomeActivity'
    messagesAppPackage = 'com.google.android.apps.messaging'
    messagesAppActivity = 'com.google.android.apps.messaging.ui.ConversationListActivity'
    whatsappAppPackage = 'com.whatsapp'
    whatsappAppActivity = 'com.whatsapp.HomeActivity'

    # Current App Package and Activity

    currentApkPath = gChat
    currentAppPackage = gChatAppPackage
    currentAppActivity = gChatAppActivity

    # Credentials

    # Element properties
    element_id_attribute = 'elementId'
    index_attribute = 'index'
    package_attribute = 'package'
    class_attribute = 'class'
    text_attribute = 'text'
    content_desc_attribute = 'content-desc'
    resource_id_attribute = 'resource-id'
    checkable_attribute = 'checkable'
    checked_attribute = 'checked'
    clickable_attribute = 'clickable'
    enabled_attribute = 'enabled'
    focusable_attribute = 'focusable'
    focused_attribute = 'focused'
    long_clickable_attribute = 'long-clickable'
    password_attribute = 'password'
    scrollable_attribute = 'scrollable'
    selected_attribute = 'selected'
    bounds_attribute = 'bounds'
    displayed_attribute = 'displayed'

