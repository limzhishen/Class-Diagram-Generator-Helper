# -*- mode: python ; coding: utf-8 -*-

import os


# 获取当前路径
project_dir = os.getcwd()

a = Analysis(
    ['ClassGenerator_startup.py'],
    pathex=[project_dir],  # 添加项目路径
    binaries=[],
    datas=[
        # 添加整个 component, data, export, fileReader 文件夹
        ('component', 'component'),
        ('data', 'data'),
        ('export', 'export'),
        ('fileReader', 'fileReader')
    ],
    hiddenimports=['customtkinter'],
    hookspath=[],
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
    a.binaries,
    a.datas,
    [],
    name='ClassGenerator_startup',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon='Icon.ico',
)
