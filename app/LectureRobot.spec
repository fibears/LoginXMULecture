# -*- mode: python -*-

block_cipher = None


a = Analysis(['LectureRobot.py'],
             pathex=['/Users/zengphil/github/LoginXMULecture/app'],
             binaries=None,
             datas=None,
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='LectureRobot',
          debug=False,
          strip=False,
          upx=True,
          console=False , icon='robot.icns')
app = BUNDLE(exe,
             name='LectureRobot.app',
             icon='robot.icns',
             bundle_identifier=None,
             info_plist={'NSHighResolutionCapable': 'True'})
