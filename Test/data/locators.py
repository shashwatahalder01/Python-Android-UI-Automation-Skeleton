# gChat

class StartupPageLocator(object):
    changeProfile = '//android.widget.FrameLayout/android.widget.ImageView[2]'
    shQups = '//android.view.ViewGroup[@content-desc="Use shahwata halder sh.qups@gmail.com"]'

    ok = '//android.widget.Button[@resource-id="android:id/button1"]'
    navigation = '//android.widget.ImageButton[@content-desc="Navigation menu"]'
    searchbutton = '//android.widget.TextView[@resource-id="com.google.android.apps.dynamite:id/open_search_bar_text_view"]'
    searchText = '//android.widget.EditText[@resource-id="com.google.android.apps.dynamite:id/search_term"]'
    selectPerson = '//android.widget.LinearLayout[@resource-id="com.google.android.apps.dynamite:id/user_name_and_indicators"]'

    chatPersons = '/android.widget.TextView[@resource-id="com.google.android.apps.dynamite:id/open_search_bar_text_view"]//android.widget.LinearLayout'
    chatMessage = '//android.widget.EditText[@resource-id="com.google.android.apps.dynamite:id/compose_edit_text"]'
    postMessage = '//android.widget.ImageButton[@resource-id="com.google.android.apps.dynamite:id/post_message_button"]'
    backFromChat = '//android.widget.ImageButton[@content-desc="Navigate Up"]'
    seenMessage = '//android.widget.ImageView[@resource-id="com.google.android.apps.dynamite:id/read_receipt_right_avatar_a"]'

    newChat = '//android.widget.Button[@resource-id="com.google.android.apps.dynamite:id/fab_stub"]'
    chat = '//android.widget.FrameLayout[@resource-id="com.google.android.apps.dynamite:id/navigation_bar_item_icon_container"]'
    rooms = '//android.widget.FrameLayout[@resource-id="com.google.android.apps.dynamite:id/navigation_bar_item_icon_container"]'


class IntroPageLocator(object):
    letsGo = '//android.widget.Button[@content-desc="Let\'s go"]'
    signInOrCreate = '//android.widget.Button[@content-desc="Sign in or create"]'
    signInOption = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup'
