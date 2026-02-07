from django.db import models
from cms.models.pluginmodel import CMSPlugin
from filer.fields.image import FilerImageField


class LayoutSection(CMSPlugin):
    title = models.CharField(max_length=200, blank=True)
    background_style = models.CharField(
        max_length=100,
        blank=True,
        help_text='Bootstrap background utility, e.g. bg-light, bg-primary-subtle.',
    )
    text_alignment = models.CharField(
        max_length=50,
        blank=True,
        help_text='Optional text alignment class, e.g. text-center.',
    )

    def __str__(self):
        return self.title or 'Layout Section'


class HeroSlider(CMSPlugin):
    heading = models.CharField(max_length=200, blank=True)
    subheading = models.CharField(max_length=255, blank=True)
    autoplay = models.BooleanField(default=True)
    interval_ms = models.PositiveIntegerField(default=6000)

    def __str__(self):
        return self.heading or 'Hero Slider'


class HeroSlide(CMSPlugin):
    image = FilerImageField(
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='+',
        help_text='Suggested: industrial automation, Siemens PLC, pharma production.',
    )
    eyebrow_text = models.CharField(
        max_length=120,
        blank=True,
        help_text='Optional short label above the title, e.g. Trusted automation partner.',
    )
    title = models.CharField(max_length=200)
    subtitle = models.TextField(blank=True)
    button_text = models.CharField(max_length=80, blank=True)
    button_url = models.URLField(blank=True)
    overlay_color = models.CharField(max_length=20, default='#0b1a2a')
    overlay_opacity = models.DecimalField(max_digits=3, decimal_places=2, default=0.55)
    alt_text = models.CharField(max_length=150, blank=True)

    def __str__(self):
        return self.title


class FeaturedProductsGrid(CMSPlugin):
    heading = models.CharField(max_length=200, blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.heading or 'Featured Products'


class ProductCard(CMSPlugin):
    title = models.CharField(max_length=200)
    model_no = models.CharField(max_length=100, blank=True)
    model_label = models.CharField(max_length=60, blank=True, default='Model')
    image = FilerImageField(
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='+',
        help_text='Suggested: industrial automation, PLC, sensor.',
    )
    short_description = models.TextField(blank=True)
    link_url = models.URLField(blank=True)
    button_text = models.CharField(max_length=80, blank=True, default='View details')
    badge = models.CharField(max_length=50, blank=True)
    alt_text = models.CharField(max_length=150, blank=True)

    def __str__(self):
        return self.title


class CategoryTeaserGrid(CMSPlugin):
    heading = models.CharField(max_length=200, blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.heading or 'Category Teaser Grid'


class CategoryCard(CMSPlugin):
    name = models.CharField(max_length=120)
    description = models.TextField(blank=True)
    icon_class = models.CharField(
        max_length=100,
        blank=True,
        help_text='Font Awesome class, e.g. fa-solid fa-microchip.',
    )
    image = FilerImageField(
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='+',
        help_text='Suggested: industrial automation, sensors, control panels.',
    )
    link_url = models.URLField(blank=True)
    button_text = models.CharField(max_length=80, blank=True, default='Explore')
    alt_text = models.CharField(max_length=150, blank=True)

    def __str__(self):
        return self.name


class IndustriesTeaser(CMSPlugin):
    heading = models.CharField(max_length=200, blank=True)
    description = models.TextField(blank=True)
    badge_text = models.CharField(
        max_length=120,
        blank=True,
        help_text='Optional badge label shown above the cards.',
    )

    def __str__(self):
        return self.heading or 'Industries Teaser'


class IndustryCard(CMSPlugin):
    name = models.CharField(max_length=120)
    description = models.TextField(blank=True)
    image = FilerImageField(
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='+',
        help_text='Suggested: pharma production line, clean room.',
    )
    link_url = models.URLField(blank=True)
    button_text = models.CharField(max_length=80, blank=True, default='See solutions')
    alt_text = models.CharField(max_length=150, blank=True)

    def __str__(self):
        return self.name


class BrandsPartnersGrid(CMSPlugin):
    heading = models.CharField(max_length=200, blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.heading or 'Brands & Partners'


class BrandLogoCard(CMSPlugin):
    name = models.CharField(max_length=120)
    short_description = models.TextField(blank=True)
    logo = FilerImageField(
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='+',
        help_text='Suggested: Siemens, SICK, ABB logo.',
    )
    link_url = models.URLField(blank=True)
    button_text = models.CharField(max_length=80, blank=True, default='View brand')
    alt_text = models.CharField(max_length=150, blank=True)

    def __str__(self):
        return self.name


class QuickContactForm(CMSPlugin):
    heading = models.CharField(max_length=200, blank=True)
    description = models.TextField(blank=True)
    benefits = models.TextField(
        blank=True,
        help_text='Enter benefit bullet points, one per line.',
    )
    helper_text = models.CharField(
        max_length=160,
        blank=True,
        help_text='Optional helper text shown near the submit button.',
    )
    submit_label = models.CharField(max_length=60, default='Request a quote')

    def __str__(self):
        return self.heading or 'Quick Contact Form'


class BrandsOverviewGrid(CMSPlugin):
    heading = models.CharField(max_length=200, blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.heading or 'Brands Overview Grid'


class BrandOverviewCard(CMSPlugin):
    name = models.CharField(max_length=120)
    description = models.TextField(blank=True)
    logo = FilerImageField(
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='+',
    )
    link_url = models.URLField(blank=True)
    button_text = models.CharField(max_length=60, default='Explore')
    alt_text = models.CharField(max_length=150, blank=True)

    def __str__(self):
        return self.name


class BrandHero(CMSPlugin):
    brand_name = models.CharField(max_length=200)
    eyebrow_text = models.CharField(
        max_length=120,
        blank=True,
        help_text='Optional label above the brand name.',
    )
    tagline = models.CharField(max_length=200, blank=True)
    description = models.TextField(blank=True)
    banner_image = FilerImageField(
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='+',
    )
    alt_text = models.CharField(max_length=150, blank=True)

    def __str__(self):
        return self.brand_name


class SubCategoriesGrid(CMSPlugin):
    heading = models.CharField(max_length=200, blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.heading or 'Sub-categories Grid'


class SubCategoryCard(CMSPlugin):
    name = models.CharField(max_length=120)
    description = models.TextField(blank=True)
    product_count = models.PositiveIntegerField(null=True, blank=True)
    image = FilerImageField(
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='+',
    )
    link_url = models.URLField(blank=True)
    button_text = models.CharField(max_length=80, blank=True, default='Browse')
    alt_text = models.CharField(max_length=150, blank=True)

    def __str__(self):
        return self.name


class CategoryHeader(CMSPlugin):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    breadcrumb_label = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.title


class ProductListingGrid(CMSPlugin):
    heading = models.CharField(max_length=200, blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.heading or 'Product Listing Grid'


class ProductItem(CMSPlugin):
    name = models.CharField(max_length=200)
    model_no = models.CharField(max_length=100, blank=True)
    model_label = models.CharField(max_length=60, blank=True, default='Model')
    key_specs = models.TextField(
        blank=True,
        help_text='Enter bullet items separated by new lines.',
    )
    image = FilerImageField(
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='+',
    )
    request_quote_url = models.URLField(blank=True)
    request_quote_label = models.CharField(max_length=80, blank=True, default='Request quote')
    detail_url = models.URLField(blank=True)
    detail_label = models.CharField(max_length=80, blank=True, default='View detail')
    alt_text = models.CharField(max_length=150, blank=True)

    def __str__(self):
        return self.name


class IndustryHero(CMSPlugin):
    title = models.CharField(max_length=200)
    eyebrow_text = models.CharField(
        max_length=120,
        blank=True,
        help_text='Optional label above the title.',
    )
    description = models.TextField(blank=True)
    banner_image = FilerImageField(
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='+',
    )
    alt_text = models.CharField(max_length=150, blank=True)

    def __str__(self):
        return self.title


class SolutionsAccordion(CMSPlugin):
    heading = models.CharField(max_length=200, blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.heading or 'Solutions Accordion'


class SolutionItem(CMSPlugin):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    icon_class = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.title


class KeyProductsGrid(CMSPlugin):
    heading = models.CharField(max_length=200, blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.heading or 'Key Products Grid'


class KeyProductCard(CMSPlugin):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    image = FilerImageField(
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='+',
    )
    link_url = models.URLField(blank=True)
    button_text = models.CharField(max_length=80, blank=True, default='Learn more')
    alt_text = models.CharField(max_length=150, blank=True)

    def __str__(self):
        return self.name


class CaseStudiesGrid(CMSPlugin):
    heading = models.CharField(max_length=200, blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.heading or 'Case Studies Grid'


class CaseStudyCard(CMSPlugin):
    title = models.CharField(max_length=200)
    client = models.CharField(max_length=200, blank=True)
    client_label = models.CharField(max_length=80, blank=True, default='Client')
    summary = models.TextField(blank=True)
    results = models.TextField(
        blank=True,
        help_text='Enter bullet items separated by new lines.',
    )
    image = FilerImageField(
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='+',
    )
    link_url = models.URLField(blank=True)
    button_text = models.CharField(max_length=80, blank=True, default='Read case study')
    alt_text = models.CharField(max_length=150, blank=True)

    def __str__(self):
        return self.title


class ManufacturersGrid(CMSPlugin):
    heading = models.CharField(max_length=200, blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.heading or 'Manufacturers Grid'


class ManufacturerDetailCard(CMSPlugin):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    logo = FilerImageField(
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='+',
    )
    key_lines = models.TextField(
        blank=True,
        help_text='Enter bullet items separated by new lines.',
    )
    certificates = FilerImageField(
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='+',
    )
    certificates_label = models.CharField(max_length=80, blank=True, default='Certificates')
    link_url = models.URLField(blank=True)
    button_text = models.CharField(max_length=80, blank=True, default='View catalog')
    alt_text = models.CharField(max_length=150, blank=True)

    def __str__(self):
        return self.name


class ContactHero(CMSPlugin):
    title = models.CharField(max_length=200, blank=True)
    subtitle = models.TextField(blank=True)
    image = FilerImageField(
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='+',
    )
    alt_text = models.CharField(max_length=150, blank=True)

    def __str__(self):
        return self.title or 'Contact Hero'


class ContactFormFull(CMSPlugin):
    heading = models.CharField(max_length=200, blank=True)
    description = models.TextField(blank=True)
    submit_label = models.CharField(max_length=60, default='Send message')

    def __str__(self):
        return self.heading or 'Contact Form Full'


class ContactInfoBlock(CMSPlugin):
    heading = models.CharField(max_length=200, blank=True)
    address_label = models.CharField(max_length=80, blank=True, default='Address')
    address = models.TextField(blank=True)
    phone_label = models.CharField(max_length=80, blank=True, default='Phone')
    phone = models.CharField(max_length=100, blank=True)
    email_label = models.CharField(max_length=80, blank=True, default='Email')
    email = models.EmailField(blank=True)
    hours_label = models.CharField(max_length=80, blank=True, default='Hours')
    hours = models.TextField(
        blank=True,
        help_text='Enter hours with one line per row, e.g. Mon-Fri: 08:00-18:00.',
    )
    social_label = models.CharField(max_length=80, blank=True, default='Connect')
    social_links = models.TextField(
        blank=True,
        help_text='Enter social links, one per line as Label|URL.',
    )

    def __str__(self):
        return self.heading or 'Contact Info Block'


class GoogleMapEmbed(CMSPlugin):
    heading = models.CharField(max_length=200, blank=True)
    embed_url = models.URLField(blank=True)
    iframe_code = models.TextField(blank=True)
    height = models.PositiveIntegerField(default=360)

    def __str__(self):
        return self.heading or 'Google Map Embed'
