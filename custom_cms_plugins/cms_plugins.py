from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import gettext_lazy as _

from . import models


MODULE_LABEL = _('Industrial B2B')


@plugin_pool.register_plugin
class LayoutSectionPlugin(CMSPluginBase):
    model = models.LayoutSection
    name = _('Layout Section (Container)')
    module = MODULE_LABEL
    render_template = 'custom_cms_plugins/layout_section.html'
    allow_children = True
    child_classes = [
        'HeroSliderPlugin',
        'FeaturedProductsGridPlugin',
        'CategoryTeaserGridPlugin',
        'IndustriesTeaserPlugin',
        'BrandsPartnersGridPlugin',
        'QuickContactFormPlugin',
        'BrandsOverviewGridPlugin',
        'BrandHeroPlugin',
        'SubCategoriesGridPlugin',
        'CategoryHeaderPlugin',
        'ProductListingGridPlugin',
        'IndustryHeroPlugin',
        'SolutionsAccordionPlugin',
        'KeyProductsGridPlugin',
        'CaseStudiesGridPlugin',
        'ManufacturersGridPlugin',
        'ContactHeroPlugin',
        'ContactFormFullPlugin',
        'ContactInfoBlockPlugin',
        'GoogleMapEmbedPlugin',
    ]
    cache = False
    icon = 'fa fa-layer-group'


@plugin_pool.register_plugin
class HeroSliderPlugin(CMSPluginBase):
    model = models.HeroSlider
    name = _('Hero Slider (Full-width)')
    module = MODULE_LABEL
    render_template = 'custom_cms_plugins/hero_slider.html'
    allow_children = True
    child_classes = ['HeroSlidePlugin']
    cache = False
    icon = 'fa fa-images'


@plugin_pool.register_plugin
class HeroSlidePlugin(CMSPluginBase):
    model = models.HeroSlide
    name = _('Hero Slide')
    module = MODULE_LABEL
    render_template = 'custom_cms_plugins/hero_slide.html'
    require_parent = True
    parent_classes = ['HeroSliderPlugin']
    cache = False
    icon = 'fa fa-image'


@plugin_pool.register_plugin
class FeaturedProductsGridPlugin(CMSPluginBase):
    model = models.FeaturedProductsGrid
    name = _('Featured Products Grid')
    module = MODULE_LABEL
    render_template = 'custom_cms_plugins/featured_products_grid.html'
    allow_children = True
    child_classes = ['ProductCardPlugin']
    cache = False
    icon = 'fa fa-box'


@plugin_pool.register_plugin
class ProductCardPlugin(CMSPluginBase):
    model = models.ProductCard
    name = _('Product Card')
    module = MODULE_LABEL
    render_template = 'custom_cms_plugins/product_card.html'
    require_parent = True
    parent_classes = ['FeaturedProductsGridPlugin', 'KeyProductsGridPlugin']
    cache = False
    icon = 'fa fa-microchip'


@plugin_pool.register_plugin
class CategoryTeaserGridPlugin(CMSPluginBase):
    model = models.CategoryTeaserGrid
    name = _('Category Teaser Grid')
    module = MODULE_LABEL
    render_template = 'custom_cms_plugins/category_teaser_grid.html'
    allow_children = True
    child_classes = ['CategoryCardPlugin']
    cache = False
    icon = 'fa fa-th-large'


@plugin_pool.register_plugin
class CategoryCardPlugin(CMSPluginBase):
    model = models.CategoryCard
    name = _('Category Card')
    module = MODULE_LABEL
    render_template = 'custom_cms_plugins/category_card.html'
    require_parent = True
    parent_classes = ['CategoryTeaserGridPlugin']
    cache = False
    icon = 'fa fa-tags'


@plugin_pool.register_plugin
class IndustriesTeaserPlugin(CMSPluginBase):
    model = models.IndustriesTeaser
    name = _('Industries Teaser')
    module = MODULE_LABEL
    render_template = 'custom_cms_plugins/industries_teaser.html'
    allow_children = True
    child_classes = ['IndustryCardPlugin']
    cache = False
    icon = 'fa fa-industry'


@plugin_pool.register_plugin
class IndustryCardPlugin(CMSPluginBase):
    model = models.IndustryCard
    name = _('Industry Card')
    module = MODULE_LABEL
    render_template = 'custom_cms_plugins/industry_card.html'
    require_parent = True
    parent_classes = ['IndustriesTeaserPlugin']
    cache = False
    icon = 'fa fa-flask'


@plugin_pool.register_plugin
class BrandsPartnersGridPlugin(CMSPluginBase):
    model = models.BrandsPartnersGrid
    name = _('Brands & Partners Grid')
    module = MODULE_LABEL
    render_template = 'custom_cms_plugins/brands_partners_grid.html'
    allow_children = True
    child_classes = ['BrandLogoCardPlugin']
    cache = False
    icon = 'fa fa-handshake'


@plugin_pool.register_plugin
class BrandLogoCardPlugin(CMSPluginBase):
    model = models.BrandLogoCard
    name = _('Brand Logo Card')
    module = MODULE_LABEL
    render_template = 'custom_cms_plugins/brand_logo_card.html'
    require_parent = True
    parent_classes = ['BrandsPartnersGridPlugin', 'BrandsOverviewGridPlugin']
    cache = False
    icon = 'fa fa-building'


@plugin_pool.register_plugin
class QuickContactFormPlugin(CMSPluginBase):
    model = models.QuickContactForm
    name = _('Quick Contact Form')
    module = MODULE_LABEL
    render_template = 'custom_cms_plugins/quick_contact_form.html'
    cache = False
    icon = 'fa fa-paper-plane'


@plugin_pool.register_plugin
class BrandsOverviewGridPlugin(CMSPluginBase):
    model = models.BrandsOverviewGrid
    name = _('Brands Overview Grid')
    module = MODULE_LABEL
    render_template = 'custom_cms_plugins/brands_overview_grid.html'
    allow_children = True
    child_classes = ['BrandOverviewCardPlugin']
    cache = False
    icon = 'fa fa-briefcase'


@plugin_pool.register_plugin
class BrandOverviewCardPlugin(CMSPluginBase):
    model = models.BrandOverviewCard
    name = _('Brand Overview Card')
    module = MODULE_LABEL
    render_template = 'custom_cms_plugins/brand_overview_card.html'
    require_parent = True
    parent_classes = ['BrandsOverviewGridPlugin']
    cache = False
    icon = 'fa fa-award'


@plugin_pool.register_plugin
class BrandHeroPlugin(CMSPluginBase):
    model = models.BrandHero
    name = _('Brand Hero Banner')
    module = MODULE_LABEL
    render_template = 'custom_cms_plugins/brand_hero.html'
    cache = False
    icon = 'fa fa-flag'


@plugin_pool.register_plugin
class SubCategoriesGridPlugin(CMSPluginBase):
    model = models.SubCategoriesGrid
    name = _('Sub-categories Grid')
    module = MODULE_LABEL
    render_template = 'custom_cms_plugins/subcategories_grid.html'
    allow_children = True
    child_classes = ['SubCategoryCardPlugin']
    cache = False
    icon = 'fa fa-sitemap'


@plugin_pool.register_plugin
class SubCategoryCardPlugin(CMSPluginBase):
    model = models.SubCategoryCard
    name = _('Sub-category Card')
    module = MODULE_LABEL
    render_template = 'custom_cms_plugins/subcategory_card.html'
    require_parent = True
    parent_classes = ['SubCategoriesGridPlugin']
    cache = False
    icon = 'fa fa-list'


@plugin_pool.register_plugin
class CategoryHeaderPlugin(CMSPluginBase):
    model = models.CategoryHeader
    name = _('Category Header')
    module = MODULE_LABEL
    render_template = 'custom_cms_plugins/category_header.html'
    cache = False
    icon = 'fa fa-stream'


@plugin_pool.register_plugin
class ProductListingGridPlugin(CMSPluginBase):
    model = models.ProductListingGrid
    name = _('Product Listing Grid')
    module = MODULE_LABEL
    render_template = 'custom_cms_plugins/product_listing_grid.html'
    allow_children = True
    child_classes = ['ProductItemPlugin']
    cache = False
    icon = 'fa fa-th'


@plugin_pool.register_plugin
class ProductItemPlugin(CMSPluginBase):
    model = models.ProductItem
    name = _('Product Item')
    module = MODULE_LABEL
    render_template = 'custom_cms_plugins/product_item.html'
    require_parent = True
    parent_classes = ['ProductListingGridPlugin']
    cache = False
    icon = 'fa fa-cube'


@plugin_pool.register_plugin
class IndustryHeroPlugin(CMSPluginBase):
    model = models.IndustryHero
    name = _('Industry Hero')
    module = MODULE_LABEL
    render_template = 'custom_cms_plugins/industry_hero.html'
    cache = False
    icon = 'fa fa-heartbeat'


@plugin_pool.register_plugin
class SolutionsAccordionPlugin(CMSPluginBase):
    model = models.SolutionsAccordion
    name = _('Solutions Accordion')
    module = MODULE_LABEL
    render_template = 'custom_cms_plugins/solutions_accordion.html'
    allow_children = True
    child_classes = ['SolutionItemPlugin']
    cache = False
    icon = 'fa fa-list-alt'


@plugin_pool.register_plugin
class SolutionItemPlugin(CMSPluginBase):
    model = models.SolutionItem
    name = _('Solution Item')
    module = MODULE_LABEL
    render_template = 'custom_cms_plugins/solution_item.html'
    require_parent = True
    parent_classes = ['SolutionsAccordionPlugin']
    cache = False
    icon = 'fa fa-check-circle'


@plugin_pool.register_plugin
class KeyProductsGridPlugin(CMSPluginBase):
    model = models.KeyProductsGrid
    name = _('Key Products Grid')
    module = MODULE_LABEL
    render_template = 'custom_cms_plugins/key_products_grid.html'
    allow_children = True
    child_classes = ['ProductCardPlugin', 'KeyProductCardPlugin']
    cache = False
    icon = 'fa fa-box-open'


@plugin_pool.register_plugin
class KeyProductCardPlugin(CMSPluginBase):
    model = models.KeyProductCard
    name = _('Key Product Card')
    module = MODULE_LABEL
    render_template = 'custom_cms_plugins/key_product_card.html'
    require_parent = True
    parent_classes = ['KeyProductsGridPlugin']
    cache = False
    icon = 'fa fa-star'


@plugin_pool.register_plugin
class CaseStudiesGridPlugin(CMSPluginBase):
    model = models.CaseStudiesGrid
    name = _('Case Studies Grid')
    module = MODULE_LABEL
    render_template = 'custom_cms_plugins/case_studies_grid.html'
    allow_children = True
    child_classes = ['CaseStudyCardPlugin']
    cache = False
    icon = 'fa fa-clipboard'


@plugin_pool.register_plugin
class CaseStudyCardPlugin(CMSPluginBase):
    model = models.CaseStudyCard
    name = _('Case Study Card')
    module = MODULE_LABEL
    render_template = 'custom_cms_plugins/case_study_card.html'
    require_parent = True
    parent_classes = ['CaseStudiesGridPlugin']
    cache = False
    icon = 'fa fa-chart-line'


@plugin_pool.register_plugin
class ManufacturersGridPlugin(CMSPluginBase):
    model = models.ManufacturersGrid
    name = _('Manufacturers Grid')
    module = MODULE_LABEL
    render_template = 'custom_cms_plugins/manufacturers_grid.html'
    allow_children = True
    child_classes = ['ManufacturerDetailCardPlugin']
    cache = False
    icon = 'fa fa-industry'


@plugin_pool.register_plugin
class ManufacturerDetailCardPlugin(CMSPluginBase):
    model = models.ManufacturerDetailCard
    name = _('Manufacturer Detail Card')
    module = MODULE_LABEL
    render_template = 'custom_cms_plugins/manufacturer_detail_card.html'
    require_parent = True
    parent_classes = ['ManufacturersGridPlugin']
    cache = False
    icon = 'fa fa-certificate'


@plugin_pool.register_plugin
class ContactHeroPlugin(CMSPluginBase):
    model = models.ContactHero
    name = _('Contact Hero')
    module = MODULE_LABEL
    render_template = 'custom_cms_plugins/contact_hero.html'
    cache = False
    icon = 'fa fa-envelope-open'


@plugin_pool.register_plugin
class ContactFormFullPlugin(CMSPluginBase):
    model = models.ContactFormFull
    name = _('Contact Form (Full)')
    module = MODULE_LABEL
    render_template = 'custom_cms_plugins/contact_form_full.html'
    cache = False
    icon = 'fa fa-envelope'


@plugin_pool.register_plugin
class ContactInfoBlockPlugin(CMSPluginBase):
    model = models.ContactInfoBlock
    name = _('Contact Info Block')
    module = MODULE_LABEL
    render_template = 'custom_cms_plugins/contact_info_block.html'
    cache = False
    icon = 'fa fa-phone'


@plugin_pool.register_plugin
class GoogleMapEmbedPlugin(CMSPluginBase):
    model = models.GoogleMapEmbed
    name = _('Google Map Embed')
    module = MODULE_LABEL
    render_template = 'custom_cms_plugins/google_map_embed.html'
    cache = False
    icon = 'fa fa-map'
