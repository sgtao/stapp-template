# -*- mode: python ; coding: utf-8 -*-
from PyInstaller.utils.hooks import collect_data_files, collect_submodules

# streamlit関連の依存関係を収集
streamlit_hidden_imports = collect_submodules("streamlit")
streamlit_data = collect_data_files("streamlit")


a = Analysis(
    ['run_streamlit.py'],
    pathex=[],
    binaries=[],
    datas=[
        ("src/pages", "pages"),
        ("src/components", "components"),
        ("src/functions", "functions"),
        ("src/main.py", "."),
    ]
    + streamlit_data,
    hiddenimports=[
        "streamlit",
        "streamlit.web.cli",
        "src.components.spiral_chart",
        "src.functions.calculations",
        "altair",
        "pandas",
        "numpy",
        "plotly",
        "pillow",
        "packaging",
        "importlib_metadata",
        "validators",
        "tornado",
        "watchdog",
        "click",
        "rich",
        "protobuf",
    ]
    + streamlit_hidden_imports,
    hookspath=['./hooks'],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='run_streamlit',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='run_streamlit',
)
