# Sample server binary "sfreerdp-server" (mirrors server/Sample/CMakeLists.txt)

# Resource root for sample icons (CMake: SAMPLE_RESOURCE_ROOT)
sample_resource_root = prefix / datadir / product
if get_option('with_resource_versioning')
  sample_resource_root += freerdp_version_major
endif
sample_resource_root += '/images'

sample_server_srcs = [
  'sfreerdp.c', 'sf_audin.c', 'sf_rdpsnd.c', 'sf_encomsp.c',
  'sf_ainput.c',   # CHANNEL_AINPUT_SERVER (ainput server is built)
]

sfreerdp_server = executable(
  'sfreerdp-server',
  files(sample_server_srcs),
  include_directories : [freerdp_public_inc, winpr_inc],
  dependencies : [freerdp_server_dep, freerdp_dep, winpr_dep],
  c_args : ['-DSAMPLE_RESOURCE_ROOT="@0@"'.format(sample_resource_root)],
  install : true,
  install_dir : get_option('bindir'),
)

# Sample icons (CMake installs bmp/png/jpg/webp into SAMPLE_RESOURCE_ROOT)
install_data(
  files('test_icon.bmp', 'test_icon.png', 'test_icon.jpg', 'test_icon.webp'),
  install_dir : sample_resource_root,
)
