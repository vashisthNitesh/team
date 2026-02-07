from cms.plugin_pool import plugin_pool
from django.test import TestCase


class PluginRegistrationTests(TestCase):
    def test_team_plugins_are_registered(self):
        self.assertIn('TeamMemberListGridCMSPlugin', plugin_pool.plugins)
        self.assertIn('TeamMemberListPluginCMSPlugin', plugin_pool.plugins)
        self.assertIn('TeamMemberDetailPluginCMSPlugin', plugin_pool.plugins)
