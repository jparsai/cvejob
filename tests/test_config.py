"""Test for the config.py."""

# import pytest
import os

from cvejob.config import DefaultConfig, RuntimeConfig


def test_default_config_constructor():
    """Basic test for the class DefaultConfig."""
    config = DefaultConfig()
    assert config is not None


def test_default_config_attributes():
    """Check the attributes existence for a class DefaultConfig."""
    config = DefaultConfig()

    # basic configuration check
    attributes = ("ecosystem", "cve_age", "feed_dir", "feed_names", "date_range", "cve_id",
                  "package_name", "cpe2pkg_path", "pkgfile_dir", "use_nvdtoolkit",
                  "nvdtoolkit_export_dir")
    for attribute in attributes:
        assert hasattr(config, attribute)


def test_default_config_attribute_values_nil():
    """Check the attributes that needs to be set to nil (None)."""
    config = DefaultConfig()

    # the following attributes needs to be set to nil
    assert config.feed_names is None
    assert config.date_range is None
    assert config.cve_id is None
    assert config.package_name is None
    assert config.feed_names is None


def test_default_config_attribute_values_not_nil():
    """Check the attributes that needs not to be set to nil (None)."""
    config = DefaultConfig()

    # the following attributes need not be set to nil
    assert config.ecosystem is not None
    assert config.cve_age is not None
    assert config.feed_dir is not None
    assert config.cpe2pkg_path is not None
    assert config.pkgfile_dir is not None
    assert config.use_nvdtoolkit is not None
    assert config.nvdtoolkit_export_dir is not None


def test_runtime_config():
    """Basic test for the class RuntimeConfig."""
    config = RuntimeConfig()
    assert config is not None


def test_runtime_config_attributes():
    """Check the attributes existence for a class RuntimeConfig."""
    config = RuntimeConfig()
    assert config is not None

    assert hasattr(config, "_config")


def unset_environment_variable(name):
    """Reset specified environment variable."""
    return os.environ.pop(name, None)


def test_runtime_config_attribute_ecosystem():
    """Check the attributes handling for a class RuntimeConfig."""
    old_value = unset_environment_variable('CVEJOB_ECOSYSTEM')

    config = RuntimeConfig()
    assert config._config.ecosystem == 'python'

    os.environ['CVEJOB_ECOSYSTEM'] = 'foobar'
    config = RuntimeConfig()
    assert config._config.ecosystem == 'foobar'

    if old_value is not None:
        os.environ['CVEJOB_ECOSYSTEM'] = old_value


def test_runtime_config_attribute_cve_age():
    """Check the attributes handling for a class RuntimeConfig."""
    old_value = unset_environment_variable('CVEJOB_CVE_AGE')

    config = RuntimeConfig()
    assert config._config.cve_age == 0

    os.environ['CVEJOB_CVE_AGE'] = '42'
    config = RuntimeConfig()
    assert config._config.cve_age == 42

    os.environ['CVEJOB_CVE_AGE'] = '-42'
    config = RuntimeConfig()
    assert config._config.cve_age == -42

    if old_value is not None:
        os.environ['CVEJOB_CVE_AGE'] = old_value


def test_runtime_config_attribute_cvejob_feed_dir():
    """Check the attributes handling for a class RuntimeConfig."""
    old_value = unset_environment_variable('CVEJOB_FEED_DIR')

    config = RuntimeConfig()
    assert config._config.feed_dir == 'nvd-data/'

    os.environ['CVEJOB_FEED_DIR'] = 'directory1'
    config = RuntimeConfig()
    assert config._config.feed_dir == 'directory1'

    if old_value is not None:
        os.environ['CVEJOB_FEED_DIR'] = old_value


def test_runtime_config_attribute_cvejob_feed_names():
    """Check the attributes handling for a class RuntimeConfig."""
    old_value = unset_environment_variable('CVEJOB_FEED_NAMES')

    config = RuntimeConfig()
    assert config._config.feed_names is None

    # TODO: the following test needs to be enabled after the fix in master branch
    # os.environ['CVEJOB_FEED_NAMES'] = 'name1'
    # config = RuntimeConfig()
    # assert config._config.feed_names == ['name1']

    # os.environ['CVEJOB_FEED_NAMES'] = 'name1,name2'
    # config = RuntimeConfig()
    # assert config._config.feed_names == ['name1', 'name2']

    if old_value is not None:
        os.environ['CVEJOB_FEED_NAMES'] = old_value


def test_runtime_config_attribute_cvejob_date_range():
    """Check the attributes handling for a class RuntimeConfig."""
    old_value = unset_environment_variable('CVEJOB_DATE_RANGE')

    config = RuntimeConfig()
    assert config._config.date_range is None

    os.environ['CVEJOB_DATE_RANGE'] = '2017-01-01'
    config = RuntimeConfig()
    assert config._config.date_range == '2017-01-01'

    if old_value is not None:
        os.environ['CVEJOB_DATE_RANGE'] = old_value


def test_runtime_config_attribute_cvejob_cve_id():
    """Check the attributes handling for a class RuntimeConfig."""
    old_value = unset_environment_variable('CVEJOB_CVE_ID')

    config = RuntimeConfig()
    assert config._config.cve_id is None

    os.environ['CVEJOB_CVE_ID'] = 'CVE1234'
    config = RuntimeConfig()
    assert config._config.cve_id == 'CVE1234'

    if old_value is not None:
        os.environ['CVEJOB_CVE_ID'] = old_value


def test_runtime_config_attribute_cvejob_package_name():
    """Check the attributes handling for a class RuntimeConfig."""
    old_value = unset_environment_variable('CVEJOB_PACKAGE_NAME')

    config = RuntimeConfig()
    assert config._config.package_name is None

    os.environ['CVEJOB_PACKAGE_NAME'] = 'test_package'
    config = RuntimeConfig()
    assert config._config.package_name == 'test_package'

    if old_value is not None:
        os.environ['CVEJOB_PACKAGE_NAME'] = old_value


def test_runtime_config_attribute_cvejob_cpe2pkg_path():
    """Check the attributes handling for a class RuntimeConfig."""
    old_value = unset_environment_variable('CVEJOB_CPE2PKG_PATH')

    config = RuntimeConfig()
    assert config._config.cpe2pkg_path == 'cpe2pkg.jar'

    os.environ['CVEJOB_CPE2PKG_PATH'] = 'cpe2pkg10.jar'
    config = RuntimeConfig()
    assert config._config.cpe2pkg_path == 'cpe2pkg10.jar'

    if old_value is not None:
        os.environ['CVEJOB_CPE2PKG_PATH'] = old_value


def test_runtime_config_attribute_cvejob_pkgfile_dir():
    """Check the attributes handling for a class RuntimeConfig."""
    old_value = unset_environment_variable('CVEJOB_PKGFILE_DIR')

    config = RuntimeConfig()
    assert config._config.pkgfile_dir == 'data/'

    os.environ['CVEJOB_PKGFILE_DIR'] = 'cpe2pkg10.jar'
    config = RuntimeConfig()
    assert config._config.pkgfile_dir == 'cpe2pkg10.jar'

    if old_value is not None:
        os.environ['CVEJOB_PKGFILE_DIR'] = old_value


def test_runtime_config_attribute_cvejob_use_nvd_toolkit():
    """Check the attributes handling for a class RuntimeConfig."""
    old_value = unset_environment_variable('CVEJOB_USE_NVD_TOOLKIT')

    config = RuntimeConfig()
    assert not config._config.use_nvdtoolkit

    os.environ['CVEJOB_USE_NVD_TOOLKIT'] = 'true'
    config = RuntimeConfig()
    assert config._config.use_nvdtoolkit

    os.environ['CVEJOB_USE_NVD_TOOLKIT'] = '1'
    config = RuntimeConfig()
    assert config._config.use_nvdtoolkit

    os.environ['CVEJOB_USE_NVD_TOOLKIT'] = 'yes'
    config = RuntimeConfig()
    assert config._config.use_nvdtoolkit

    os.environ['CVEJOB_USE_NVD_TOOLKIT'] = 'false'
    config = RuntimeConfig()
    assert not config._config.use_nvdtoolkit

    os.environ['CVEJOB_USE_NVD_TOOLKIT'] = '0'
    config = RuntimeConfig()
    assert not config._config.use_nvdtoolkit

    os.environ['CVEJOB_USE_NVD_TOOLKIT'] = 'no'
    config = RuntimeConfig()
    assert not config._config.use_nvdtoolkit

    if old_value is not None:
        os.environ['CVEJOB_USE_NVD_TOOLKIT'] = old_value


def test_runtime_config_attribute_cvejob_nvd_toolkit_export_dir():
    """Check the attributes handling for a class RuntimeConfig."""
    old_value = unset_environment_variable('CVEJOB_NVD_TOOLKIT_EXPORT_DIR')

    config = RuntimeConfig()
    assert config._config.nvdtoolkit_export_dir == 'export/'

    os.environ['CVEJOB_NVD_TOOLKIT_EXPORT_DIR'] = 'export2/'
    config = RuntimeConfig()
    assert config._config.nvdtoolkit_export_dir == 'export2/'

    if old_value is not None:
        os.environ['CVEJOB_NVD_TOOLKIT_EXPORT_DIR'] = old_value
