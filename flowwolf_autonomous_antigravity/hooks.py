app_name = "flowwolf_autonomous_antigravity"
app_title = "Flowwolf Autonomous Antigravity"
app_publisher = "A Frappe app for Flowwolf Autonomous Antigravity"
app_description = "flowwolf_autonomous_antigravity"
app_email = "your.email@example.com"
app_license = "mit"

# Apps
# ------------------

# required_apps = []

# Each item in the list will be shown as an app in the apps page
# add_to_apps_screen = [
# 	{
# 		"name": "flowwolf_autonomous_antigravity",
# 		"logo": "/assets/flowwolf_autonomous_antigravity/logo.png",
# 		"title": "Flowwolf Autonomous Antigravity",
# 		"route": "/flowwolf_autonomous_antigravity",
# 		"has_permission": "flowwolf_autonomous_antigravity.api.permission.has_app_permission"
# 	}
# ]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/flowwolf_autonomous_antigravity/css/flowwolf_autonomous_antigravity.css"
# app_include_js = "/assets/flowwolf_autonomous_antigravity/js/flowwolf_autonomous_antigravity.js"

# include js, css files in header of web template
# web_include_css = "/assets/flowwolf_autonomous_antigravity/css/flowwolf_autonomous_antigravity.css"
# web_include_js = "/assets/flowwolf_autonomous_antigravity/js/flowwolf_autonomous_antigravity.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "flowwolf_autonomous_antigravity/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "flowwolf_autonomous_antigravity/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "flowwolf_autonomous_antigravity.utils.jinja_methods",
# 	"filters": "flowwolf_autonomous_antigravity.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "flowwolf_autonomous_antigravity.install.before_install"
# after_install = "flowwolf_autonomous_antigravity.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "flowwolf_autonomous_antigravity.uninstall.before_uninstall"
# after_uninstall = "flowwolf_autonomous_antigravity.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "flowwolf_autonomous_antigravity.utils.before_app_install"
# after_app_install = "flowwolf_autonomous_antigravity.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "flowwolf_autonomous_antigravity.utils.before_app_uninstall"
# after_app_uninstall = "flowwolf_autonomous_antigravity.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "flowwolf_autonomous_antigravity.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"flowwolf_autonomous_antigravity.tasks.all"
# 	],
# 	"daily": [
# 		"flowwolf_autonomous_antigravity.tasks.daily"
# 	],
# 	"hourly": [
# 		"flowwolf_autonomous_antigravity.tasks.hourly"
# 	],
# 	"weekly": [
# 		"flowwolf_autonomous_antigravity.tasks.weekly"
# 	],
# 	"monthly": [
# 		"flowwolf_autonomous_antigravity.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "flowwolf_autonomous_antigravity.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "flowwolf_autonomous_antigravity.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "flowwolf_autonomous_antigravity.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["flowwolf_autonomous_antigravity.utils.before_request"]
# after_request = ["flowwolf_autonomous_antigravity.utils.after_request"]

# Job Events
# ----------
# before_job = ["flowwolf_autonomous_antigravity.utils.before_job"]
# after_job = ["flowwolf_autonomous_antigravity.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"flowwolf_autonomous_antigravity.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }

# Translation
# ------------
# List of apps whose translatable strings should be excluded from this app's translations.
# ignore_translatable_strings_from = []

