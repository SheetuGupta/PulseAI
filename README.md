
```
PulseAI
├─ AI
│  ├─ .env
│  ├─ coaching_chatbot
│  │  ├─ .env
│  │  ├─ agent
│  │  │  ├─ context_builder.py
│  │  │  ├─ intent_detector.py
│  │  │  ├─ orchestrator.py
│  │  │  ├─ prompt_builder.py
│  │  │  ├─ safety_guard.py
│  │  │  └─ __pycache__
│  │  │     ├─ context_builder.cpython-313.pyc
│  │  │     ├─ intent_detector.cpython-313.pyc
│  │  │     ├─ orchestrator.cpython-313.pyc
│  │  │     ├─ prompt_builder.cpython-313.pyc
│  │  │     └─ safety_guard.cpython-313.pyc
│  │  ├─ config
│  │  │  ├─ settings.py
│  │  │  └─ __pycache__
│  │  │     └─ settings.cpython-313.pyc
│  │  ├─ database
│  │  │  ├─ connection.py
│  │  │  ├─ migrations.sql
│  │  │  └─ __pycache__
│  │  │     └─ connection.cpython-313.pyc
│  │  ├─ error_log.txt
│  │  ├─ main.py
│  │  ├─ memory
│  │  │  ├─ embedder.py
│  │  │  ├─ retriever.py
│  │  │  ├─ store.py
│  │  │  └─ __pycache__
│  │  │     ├─ embedder.cpython-313.pyc
│  │  │     ├─ retriever.cpython-313.pyc
│  │  │     └─ store.cpython-313.pyc
│  │  ├─ models
│  │  │  ├─ schemas.py
│  │  │  └─ __pycache__
│  │  │     └─ schemas.cpython-313.pyc
│  │  ├─ README.md
│  │  ├─ requirements.txt
│  │  ├─ routers
│  │  │  ├─ chat.py
│  │  │  └─ __pycache__
│  │  │     └─ chat.cpython-313.pyc
│  │  ├─ test_terminal.py
│  │  ├─ utils
│  │  │  ├─ memory_extractor.py
│  │  │  └─ __pycache__
│  │  │     └─ memory_extractor.cpython-313.pyc
│  │  └─ __pycache__
│  │     └─ main.cpython-313.pyc
│  ├─ form_analysis
│  │  ├─ .env
│  │  ├─ config
│  │  │  ├─ settings.py
│  │  │  └─ __pycache__
│  │  │     └─ settings.cpython-313.pyc
│  │  ├─ data
│  │  │  └─ exercise_rules.json
│  │  ├─ main.py
│  │  ├─ models
│  │  │  ├─ schemas.py
│  │  │  └─ __pycache__
│  │  │     └─ schemas.cpython-313.pyc
│  │  ├─ pipeline
│  │  │  ├─ angle_calculator.py
│  │  │  ├─ feedback_builder.py
│  │  │  ├─ gemini_analyzer.py
│  │  │  ├─ pose_estimator.py
│  │  │  ├─ pose_landmarker.task
│  │  │  ├─ video_processor.py
│  │  │  └─ __pycache__
│  │  │     ├─ angle_calculator.cpython-313.pyc
│  │  │     ├─ feedback_builder.cpython-313.pyc
│  │  │     ├─ gemini_analyzer.cpython-313.pyc
│  │  │     ├─ pose_estimator.cpython-313.pyc
│  │  │     └─ video_processor.cpython-313.pyc
│  │  ├─ README.md
│  │  ├─ requirements.txt
│  │  ├─ routers
│  │  │  ├─ form.py
│  │  │  └─ __pycache__
│  │  │     └─ form.cpython-313.pyc
│  │  └─ __pycache__
│  │     └─ main.cpython-313.pyc
│  ├─ mealplanner.py
│  ├─ workoutgenerator.py
│  └─ __pycache__
│     └─ workoutgenerator.cpython-313.pyc
├─ main.py
├─ myvenv
│  ├─ Include
│  ├─ Lib
│  │  └─ site-packages
│  │     ├─ 81d243bd2c585b0f4821__mypyc.cp313-win_amd64.pyd
│  │     ├─ absl
│  │     │  ├─ app.py
│  │     │  ├─ app.pyi
│  │     │  ├─ command_name.py
│  │     │  ├─ flags
│  │     │  │  ├─ argparse_flags.py
│  │     │  │  ├─ _argument_parser.py
│  │     │  │  ├─ _defines.py
│  │     │  │  ├─ _exceptions.py
│  │     │  │  ├─ _flag.py
│  │     │  │  ├─ _flagvalues.py
│  │     │  │  ├─ _helpers.py
│  │     │  │  ├─ _validators.py
│  │     │  │  ├─ _validators_classes.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ argparse_flags.cpython-313.pyc
│  │     │  │     ├─ _argument_parser.cpython-313.pyc
│  │     │  │     ├─ _defines.cpython-313.pyc
│  │     │  │     ├─ _exceptions.cpython-313.pyc
│  │     │  │     ├─ _flag.cpython-313.pyc
│  │     │  │     ├─ _flagvalues.cpython-313.pyc
│  │     │  │     ├─ _helpers.cpython-313.pyc
│  │     │  │     ├─ _validators.cpython-313.pyc
│  │     │  │     ├─ _validators_classes.cpython-313.pyc
│  │     │  │     └─ __init__.cpython-313.pyc
│  │     │  ├─ logging
│  │     │  │  ├─ converter.py
│  │     │  │  ├─ __init__.py
│  │     │  │  ├─ __init__.pyi
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ converter.cpython-313.pyc
│  │     │  │     └─ __init__.cpython-313.pyc
│  │     │  ├─ py.typed
│  │     │  ├─ testing
│  │     │  │  ├─ absltest.py
│  │     │  │  ├─ flagsaver.py
│  │     │  │  ├─ parameterized.py
│  │     │  │  ├─ xml_reporter.py
│  │     │  │  ├─ _bazelize_command.py
│  │     │  │  ├─ _pretty_print_reporter.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ absltest.cpython-313.pyc
│  │     │  │     ├─ flagsaver.cpython-313.pyc
│  │     │  │     ├─ parameterized.cpython-313.pyc
│  │     │  │     ├─ xml_reporter.cpython-313.pyc
│  │     │  │     ├─ _bazelize_command.cpython-313.pyc
│  │     │  │     ├─ _pretty_print_reporter.cpython-313.pyc
│  │     │  │     └─ __init__.cpython-313.pyc
│  │     │  ├─ __init__.py
│  │     │  └─ __pycache__
│  │     │     ├─ app.cpython-313.pyc
│  │     │     ├─ command_name.cpython-313.pyc
│  │     │     └─ __init__.cpython-313.pyc
│  │     ├─ absl_py-2.4.0.dist-info
│  │     │  ├─ INSTALLER
│  │     │  ├─ licenses
│  │     │  │  ├─ AUTHORS
│  │     │  │  └─ LICENSE
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  └─ WHEEL
│  │     ├─ annotated_doc
│  │     │  ├─ main.py
│  │     │  ├─ py.typed
│  │     │  ├─ __init__.py
│  │     │  └─ __pycache__
│  │     │     ├─ main.cpython-313.pyc
│  │     │     └─ __init__.cpython-313.pyc
│  │     ├─ annotated_doc-0.0.4.dist-info
│  │     │  ├─ entry_points.txt
│  │     │  ├─ INSTALLER
│  │     │  ├─ licenses
│  │     │  │  └─ LICENSE
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  └─ WHEEL
│  │     ├─ annotated_types
│  │     │  ├─ py.typed
│  │     │  ├─ test_cases.py
│  │     │  ├─ __init__.py
│  │     │  └─ __pycache__
│  │     │     ├─ test_cases.cpython-313.pyc
│  │     │     └─ __init__.cpython-313.pyc
│  │     ├─ annotated_types-0.7.0.dist-info
│  │     │  ├─ INSTALLER
│  │     │  ├─ licenses
│  │     │  │  └─ LICENSE
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  └─ WHEEL
│  │     ├─ anyio
│  │     │  ├─ abc
│  │     │  │  ├─ _eventloop.py
│  │     │  │  ├─ _resources.py
│  │     │  │  ├─ _sockets.py
│  │     │  │  ├─ _streams.py
│  │     │  │  ├─ _subprocesses.py
│  │     │  │  ├─ _tasks.py
│  │     │  │  ├─ _testing.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ _eventloop.cpython-313.pyc
│  │     │  │     ├─ _resources.cpython-313.pyc
│  │     │  │     ├─ _sockets.cpython-313.pyc
│  │     │  │     ├─ _streams.cpython-313.pyc
│  │     │  │     ├─ _subprocesses.cpython-313.pyc
│  │     │  │     ├─ _tasks.cpython-313.pyc
│  │     │  │     ├─ _testing.cpython-313.pyc
│  │     │  │     └─ __init__.cpython-313.pyc
│  │     │  ├─ from_thread.py
│  │     │  ├─ functools.py
│  │     │  ├─ lowlevel.py
│  │     │  ├─ py.typed
│  │     │  ├─ pytest_plugin.py
│  │     │  ├─ streams
│  │     │  │  ├─ buffered.py
│  │     │  │  ├─ file.py
│  │     │  │  ├─ memory.py
│  │     │  │  ├─ stapled.py
│  │     │  │  ├─ text.py
│  │     │  │  ├─ tls.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ buffered.cpython-313.pyc
│  │     │  │     ├─ file.cpython-313.pyc
│  │     │  │     ├─ memory.cpython-313.pyc
│  │     │  │     ├─ stapled.cpython-313.pyc
│  │     │  │     ├─ text.cpython-313.pyc
│  │     │  │     ├─ tls.cpython-313.pyc
│  │     │  │     └─ __init__.cpython-313.pyc
│  │     │  ├─ to_interpreter.py
│  │     │  ├─ to_process.py
│  │     │  ├─ to_thread.py
│  │     │  ├─ _backends
│  │     │  │  ├─ _asyncio.py
│  │     │  │  ├─ _trio.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ _asyncio.cpython-313.pyc
│  │     │  │     ├─ _trio.cpython-313.pyc
│  │     │  │     └─ __init__.cpython-313.pyc
│  │     │  ├─ _core
│  │     │  │  ├─ _asyncio_selector_thread.py
│  │     │  │  ├─ _contextmanagers.py
│  │     │  │  ├─ _eventloop.py
│  │     │  │  ├─ _exceptions.py
│  │     │  │  ├─ _fileio.py
│  │     │  │  ├─ _resources.py
│  │     │  │  ├─ _signals.py
│  │     │  │  ├─ _sockets.py
│  │     │  │  ├─ _streams.py
│  │     │  │  ├─ _subprocesses.py
│  │     │  │  ├─ _synchronization.py
│  │     │  │  ├─ _tasks.py
│  │     │  │  ├─ _tempfile.py
│  │     │  │  ├─ _testing.py
│  │     │  │  ├─ _typedattr.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ _asyncio_selector_thread.cpython-313.pyc
│  │     │  │     ├─ _contextmanagers.cpython-313.pyc
│  │     │  │     ├─ _eventloop.cpython-313.pyc
│  │     │  │     ├─ _exceptions.cpython-313.pyc
│  │     │  │     ├─ _fileio.cpython-313.pyc
│  │     │  │     ├─ _resources.cpython-313.pyc
│  │     │  │     ├─ _signals.cpython-313.pyc
│  │     │  │     ├─ _sockets.cpython-313.pyc
│  │     │  │     ├─ _streams.cpython-313.pyc
│  │     │  │     ├─ _subprocesses.cpython-313.pyc
│  │     │  │     ├─ _synchronization.cpython-313.pyc
│  │     │  │     ├─ _tasks.cpython-313.pyc
│  │     │  │     ├─ _tempfile.cpython-313.pyc
│  │     │  │     ├─ _testing.cpython-313.pyc
│  │     │  │     ├─ _typedattr.cpython-313.pyc
│  │     │  │     └─ __init__.cpython-313.pyc
│  │     │  ├─ __init__.py
│  │     │  └─ __pycache__
│  │     │     ├─ from_thread.cpython-313.pyc
│  │     │     ├─ functools.cpython-313.pyc
│  │     │     ├─ lowlevel.cpython-313.pyc
│  │     │     ├─ pytest_plugin.cpython-313.pyc
│  │     │     ├─ to_interpreter.cpython-313.pyc
│  │     │     ├─ to_process.cpython-313.pyc
│  │     │     ├─ to_thread.cpython-313.pyc
│  │     │     └─ __init__.cpython-313.pyc
│  │     ├─ anyio-4.12.1.dist-info
│  │     │  ├─ entry_points.txt
│  │     │  ├─ INSTALLER
│  │     │  ├─ licenses
│  │     │  │  └─ LICENSE
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  ├─ top_level.txt
│  │     │  └─ WHEEL
│  │     ├─ certifi
│  │     │  ├─ cacert.pem
│  │     │  ├─ core.py
│  │     │  ├─ py.typed
│  │     │  ├─ __init__.py
│  │     │  ├─ __main__.py
│  │     │  └─ __pycache__
│  │     │     ├─ core.cpython-313.pyc
│  │     │     ├─ __init__.cpython-313.pyc
│  │     │     └─ __main__.cpython-313.pyc
│  │     ├─ certifi-2026.2.25.dist-info
│  │     │  ├─ INSTALLER
│  │     │  ├─ licenses
│  │     │  │  └─ LICENSE
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  ├─ top_level.txt
│  │     │  └─ WHEEL
│  │     ├─ cffi
│  │     │  ├─ api.py
│  │     │  ├─ backend_ctypes.py
│  │     │  ├─ cffi_opcode.py
│  │     │  ├─ commontypes.py
│  │     │  ├─ cparser.py
│  │     │  ├─ error.py
│  │     │  ├─ ffiplatform.py
│  │     │  ├─ lock.py
│  │     │  ├─ model.py
│  │     │  ├─ parse_c_type.h
│  │     │  ├─ pkgconfig.py
│  │     │  ├─ recompiler.py
│  │     │  ├─ setuptools_ext.py
│  │     │  ├─ vengine_cpy.py
│  │     │  ├─ vengine_gen.py
│  │     │  ├─ verifier.py
│  │     │  ├─ _cffi_errors.h
│  │     │  ├─ _cffi_include.h
│  │     │  ├─ _embedding.h
│  │     │  ├─ _imp_emulation.py
│  │     │  ├─ _shimmed_dist_utils.py
│  │     │  ├─ __init__.py
│  │     │  └─ __pycache__
│  │     │     ├─ api.cpython-313.pyc
│  │     │     ├─ backend_ctypes.cpython-313.pyc
│  │     │     ├─ cffi_opcode.cpython-313.pyc
│  │     │     ├─ commontypes.cpython-313.pyc
│  │     │     ├─ cparser.cpython-313.pyc
│  │     │     ├─ error.cpython-313.pyc
│  │     │     ├─ ffiplatform.cpython-313.pyc
│  │     │     ├─ lock.cpython-313.pyc
│  │     │     ├─ model.cpython-313.pyc
│  │     │     ├─ pkgconfig.cpython-313.pyc
│  │     │     ├─ recompiler.cpython-313.pyc
│  │     │     ├─ setuptools_ext.cpython-313.pyc
│  │     │     ├─ vengine_cpy.cpython-313.pyc
│  │     │     ├─ vengine_gen.cpython-313.pyc
│  │     │     ├─ verifier.cpython-313.pyc
│  │     │     ├─ _imp_emulation.cpython-313.pyc
│  │     │     ├─ _shimmed_dist_utils.cpython-313.pyc
│  │     │     └─ __init__.cpython-313.pyc
│  │     ├─ cffi-2.0.0.dist-info
│  │     │  ├─ entry_points.txt
│  │     │  ├─ INSTALLER
│  │     │  ├─ licenses
│  │     │  │  ├─ AUTHORS
│  │     │  │  └─ LICENSE
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  ├─ top_level.txt
│  │     │  └─ WHEEL
│  │     ├─ charset_normalizer
│  │     │  ├─ api.py
│  │     │  ├─ cd.cp313-win_amd64.pyd
│  │     │  ├─ cd.py
│  │     │  ├─ cli
│  │     │  │  ├─ __init__.py
│  │     │  │  ├─ __main__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ __init__.cpython-313.pyc
│  │     │  │     └─ __main__.cpython-313.pyc
│  │     │  ├─ constant.py
│  │     │  ├─ legacy.py
│  │     │  ├─ md.cp313-win_amd64.pyd
│  │     │  ├─ md.py
│  │     │  ├─ models.py
│  │     │  ├─ py.typed
│  │     │  ├─ utils.py
│  │     │  ├─ version.py
│  │     │  ├─ __init__.py
│  │     │  ├─ __main__.py
│  │     │  └─ __pycache__
│  │     │     ├─ api.cpython-313.pyc
│  │     │     ├─ cd.cpython-313.pyc
│  │     │     ├─ constant.cpython-313.pyc
│  │     │     ├─ legacy.cpython-313.pyc
│  │     │     ├─ md.cpython-313.pyc
│  │     │     ├─ models.cpython-313.pyc
│  │     │     ├─ utils.cpython-313.pyc
│  │     │     ├─ version.cpython-313.pyc
│  │     │     ├─ __init__.cpython-313.pyc
│  │     │     └─ __main__.cpython-313.pyc
│  │     ├─ charset_normalizer-3.4.6.dist-info
│  │     │  ├─ entry_points.txt
│  │     │  ├─ INSTALLER
│  │     │  ├─ licenses
│  │     │  │  └─ LICENSE
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  ├─ top_level.txt
│  │     │  └─ WHEEL
│  │     ├─ click
│  │     │  ├─ core.py
│  │     │  ├─ decorators.py
│  │     │  ├─ exceptions.py
│  │     │  ├─ formatting.py
│  │     │  ├─ globals.py
│  │     │  ├─ parser.py
│  │     │  ├─ py.typed
│  │     │  ├─ shell_completion.py
│  │     │  ├─ termui.py
│  │     │  ├─ testing.py
│  │     │  ├─ types.py
│  │     │  ├─ utils.py
│  │     │  ├─ _compat.py
│  │     │  ├─ _termui_impl.py
│  │     │  ├─ _textwrap.py
│  │     │  ├─ _utils.py
│  │     │  ├─ _winconsole.py
│  │     │  ├─ __init__.py
│  │     │  └─ __pycache__
│  │     │     ├─ core.cpython-313.pyc
│  │     │     ├─ decorators.cpython-313.pyc
│  │     │     ├─ exceptions.cpython-313.pyc
│  │     │     ├─ formatting.cpython-313.pyc
│  │     │     ├─ globals.cpython-313.pyc
│  │     │     ├─ parser.cpython-313.pyc
│  │     │     ├─ shell_completion.cpython-313.pyc
│  │     │     ├─ termui.cpython-313.pyc
│  │     │     ├─ testing.cpython-313.pyc
│  │     │     ├─ types.cpython-313.pyc
│  │     │     ├─ utils.cpython-313.pyc
│  │     │     ├─ _compat.cpython-313.pyc
│  │     │     ├─ _termui_impl.cpython-313.pyc
│  │     │     ├─ _textwrap.cpython-313.pyc
│  │     │     ├─ _utils.cpython-313.pyc
│  │     │     ├─ _winconsole.cpython-313.pyc
│  │     │     └─ __init__.cpython-313.pyc
│  │     ├─ click-8.3.1.dist-info
│  │     │  ├─ INSTALLER
│  │     │  ├─ licenses
│  │     │  │  └─ LICENSE.txt
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  └─ WHEEL
│  │     ├─ colorama
│  │     │  ├─ ansi.py
│  │     │  ├─ ansitowin32.py
│  │     │  ├─ initialise.py
│  │     │  ├─ tests
│  │     │  │  ├─ ansitowin32_test.py
│  │     │  │  ├─ ansi_test.py
│  │     │  │  ├─ initialise_test.py
│  │     │  │  ├─ isatty_test.py
│  │     │  │  ├─ utils.py
│  │     │  │  ├─ winterm_test.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ ansitowin32_test.cpython-313.pyc
│  │     │  │     ├─ ansi_test.cpython-313.pyc
│  │     │  │     ├─ initialise_test.cpython-313.pyc
│  │     │  │     ├─ isatty_test.cpython-313.pyc
│  │     │  │     ├─ utils.cpython-313.pyc
│  │     │  │     ├─ winterm_test.cpython-313.pyc
│  │     │  │     └─ __init__.cpython-313.pyc
│  │     │  ├─ win32.py
│  │     │  ├─ winterm.py
│  │     │  ├─ __init__.py
│  │     │  └─ __pycache__
│  │     │     ├─ ansi.cpython-313.pyc
│  │     │     ├─ ansitowin32.cpython-313.pyc
│  │     │     ├─ initialise.cpython-313.pyc
│  │     │     ├─ win32.cpython-313.pyc
│  │     │     ├─ winterm.cpython-313.pyc
│  │     │     └─ __init__.cpython-313.pyc
│  │     ├─ colorama-0.4.6.dist-info
│  │     │  ├─ INSTALLER
│  │     │  ├─ licenses
│  │     │  │  └─ LICENSE.txt
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  └─ WHEEL
│  │     ├─ contourpy
│  │     │  ├─ array.py
│  │     │  ├─ chunk.py
│  │     │  ├─ convert.py
│  │     │  ├─ dechunk.py
│  │     │  ├─ enum_util.py
│  │     │  ├─ py.typed
│  │     │  ├─ typecheck.py
│  │     │  ├─ types.py
│  │     │  ├─ util
│  │     │  │  ├─ bokeh_renderer.py
│  │     │  │  ├─ bokeh_util.py
│  │     │  │  ├─ data.py
│  │     │  │  ├─ mpl_renderer.py
│  │     │  │  ├─ mpl_util.py
│  │     │  │  ├─ renderer.py
│  │     │  │  ├─ _build_config.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ bokeh_renderer.cpython-313.pyc
│  │     │  │     ├─ bokeh_util.cpython-313.pyc
│  │     │  │     ├─ data.cpython-313.pyc
│  │     │  │     ├─ mpl_renderer.cpython-313.pyc
│  │     │  │     ├─ mpl_util.cpython-313.pyc
│  │     │  │     ├─ renderer.cpython-313.pyc
│  │     │  │     ├─ _build_config.cpython-313.pyc
│  │     │  │     └─ __init__.cpython-313.pyc
│  │     │  ├─ _contourpy.cp313-win_amd64.lib
│  │     │  ├─ _contourpy.cp313-win_amd64.pyd
│  │     │  ├─ _contourpy.pyi
│  │     │  ├─ _version.py
│  │     │  ├─ __init__.py
│  │     │  └─ __pycache__
│  │     │     ├─ array.cpython-313.pyc
│  │     │     ├─ chunk.cpython-313.pyc
│  │     │     ├─ convert.cpython-313.pyc
│  │     │     ├─ dechunk.cpython-313.pyc
│  │     │     ├─ enum_util.cpython-313.pyc
│  │     │     ├─ typecheck.cpython-313.pyc
│  │     │     ├─ types.cpython-313.pyc
│  │     │     ├─ _version.cpython-313.pyc
│  │     │     └─ __init__.cpython-313.pyc
│  │     ├─ contourpy-1.3.3.dist-info
│  │     │  ├─ INSTALLER
│  │     │  ├─ LICENSE
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  └─ WHEEL
│  │     ├─ cryptography
│  │     │  ├─ exceptions.py
│  │     │  ├─ fernet.py
│  │     │  ├─ hazmat
│  │     │  │  ├─ asn1
│  │     │  │  │  ├─ asn1.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ asn1.cpython-313.pyc
│  │     │  │  │     └─ __init__.cpython-313.pyc
│  │     │  │  ├─ backends
│  │     │  │  │  ├─ openssl
│  │     │  │  │  │  ├─ backend.py
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  └─ __pycache__
│  │     │  │  │  │     ├─ backend.cpython-313.pyc
│  │     │  │  │  │     └─ __init__.cpython-313.pyc
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     └─ __init__.cpython-313.pyc
│  │     │  │  ├─ bindings
│  │     │  │  │  ├─ openssl
│  │     │  │  │  │  ├─ binding.py
│  │     │  │  │  │  ├─ _conditional.py
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  └─ __pycache__
│  │     │  │  │  │     ├─ binding.cpython-313.pyc
│  │     │  │  │  │     ├─ _conditional.cpython-313.pyc
│  │     │  │  │  │     └─ __init__.cpython-313.pyc
│  │     │  │  │  ├─ _rust
│  │     │  │  │  │  ├─ asn1.pyi
│  │     │  │  │  │  ├─ declarative_asn1.pyi
│  │     │  │  │  │  ├─ exceptions.pyi
│  │     │  │  │  │  ├─ ocsp.pyi
│  │     │  │  │  │  ├─ openssl
│  │     │  │  │  │  │  ├─ aead.pyi
│  │     │  │  │  │  │  ├─ ciphers.pyi
│  │     │  │  │  │  │  ├─ cmac.pyi
│  │     │  │  │  │  │  ├─ dh.pyi
│  │     │  │  │  │  │  ├─ dsa.pyi
│  │     │  │  │  │  │  ├─ ec.pyi
│  │     │  │  │  │  │  ├─ ed25519.pyi
│  │     │  │  │  │  │  ├─ ed448.pyi
│  │     │  │  │  │  │  ├─ hashes.pyi
│  │     │  │  │  │  │  ├─ hmac.pyi
│  │     │  │  │  │  │  ├─ kdf.pyi
│  │     │  │  │  │  │  ├─ keys.pyi
│  │     │  │  │  │  │  ├─ poly1305.pyi
│  │     │  │  │  │  │  ├─ rsa.pyi
│  │     │  │  │  │  │  ├─ x25519.pyi
│  │     │  │  │  │  │  ├─ x448.pyi
│  │     │  │  │  │  │  └─ __init__.pyi
│  │     │  │  │  │  ├─ pkcs12.pyi
│  │     │  │  │  │  ├─ pkcs7.pyi
│  │     │  │  │  │  ├─ test_support.pyi
│  │     │  │  │  │  ├─ x509.pyi
│  │     │  │  │  │  ├─ _openssl.pyi
│  │     │  │  │  │  └─ __init__.pyi
│  │     │  │  │  ├─ _rust.pyd
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     └─ __init__.cpython-313.pyc
│  │     │  │  ├─ decrepit
│  │     │  │  │  ├─ ciphers
│  │     │  │  │  │  ├─ algorithms.py
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  └─ __pycache__
│  │     │  │  │  │     ├─ algorithms.cpython-313.pyc
│  │     │  │  │  │     └─ __init__.cpython-313.pyc
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     └─ __init__.cpython-313.pyc
│  │     │  │  ├─ primitives
│  │     │  │  │  ├─ asymmetric
│  │     │  │  │  │  ├─ dh.py
│  │     │  │  │  │  ├─ dsa.py
│  │     │  │  │  │  ├─ ec.py
│  │     │  │  │  │  ├─ ed25519.py
│  │     │  │  │  │  ├─ ed448.py
│  │     │  │  │  │  ├─ padding.py
│  │     │  │  │  │  ├─ rsa.py
│  │     │  │  │  │  ├─ types.py
│  │     │  │  │  │  ├─ utils.py
│  │     │  │  │  │  ├─ x25519.py
│  │     │  │  │  │  ├─ x448.py
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  └─ __pycache__
│  │     │  │  │  │     ├─ dh.cpython-313.pyc
│  │     │  │  │  │     ├─ dsa.cpython-313.pyc
│  │     │  │  │  │     ├─ ec.cpython-313.pyc
│  │     │  │  │  │     ├─ ed25519.cpython-313.pyc
│  │     │  │  │  │     ├─ ed448.cpython-313.pyc
│  │     │  │  │  │     ├─ padding.cpython-313.pyc
│  │     │  │  │  │     ├─ rsa.cpython-313.pyc
│  │     │  │  │  │     ├─ types.cpython-313.pyc
│  │     │  │  │  │     ├─ utils.cpython-313.pyc
│  │     │  │  │  │     ├─ x25519.cpython-313.pyc
│  │     │  │  │  │     ├─ x448.cpython-313.pyc
│  │     │  │  │  │     └─ __init__.cpython-313.pyc
│  │     │  │  │  ├─ ciphers
│  │     │  │  │  │  ├─ aead.py
│  │     │  │  │  │  ├─ algorithms.py
│  │     │  │  │  │  ├─ base.py
│  │     │  │  │  │  ├─ modes.py
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  └─ __pycache__
│  │     │  │  │  │     ├─ aead.cpython-313.pyc
│  │     │  │  │  │     ├─ algorithms.cpython-313.pyc
│  │     │  │  │  │     ├─ base.cpython-313.pyc
│  │     │  │  │  │     ├─ modes.cpython-313.pyc
│  │     │  │  │  │     └─ __init__.cpython-313.pyc
│  │     │  │  │  ├─ cmac.py
│  │     │  │  │  ├─ constant_time.py
│  │     │  │  │  ├─ hashes.py
│  │     │  │  │  ├─ hmac.py
│  │     │  │  │  ├─ kdf
│  │     │  │  │  │  ├─ argon2.py
│  │     │  │  │  │  ├─ concatkdf.py
│  │     │  │  │  │  ├─ hkdf.py
│  │     │  │  │  │  ├─ kbkdf.py
│  │     │  │  │  │  ├─ pbkdf2.py
│  │     │  │  │  │  ├─ scrypt.py
│  │     │  │  │  │  ├─ x963kdf.py
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  └─ __pycache__
│  │     │  │  │  │     ├─ argon2.cpython-313.pyc
│  │     │  │  │  │     ├─ concatkdf.cpython-313.pyc
│  │     │  │  │  │     ├─ hkdf.cpython-313.pyc
│  │     │  │  │  │     ├─ kbkdf.cpython-313.pyc
│  │     │  │  │  │     ├─ pbkdf2.cpython-313.pyc
│  │     │  │  │  │     ├─ scrypt.cpython-313.pyc
│  │     │  │  │  │     ├─ x963kdf.cpython-313.pyc
│  │     │  │  │  │     └─ __init__.cpython-313.pyc
│  │     │  │  │  ├─ keywrap.py
│  │     │  │  │  ├─ padding.py
│  │     │  │  │  ├─ poly1305.py
│  │     │  │  │  ├─ serialization
│  │     │  │  │  │  ├─ base.py
│  │     │  │  │  │  ├─ pkcs12.py
│  │     │  │  │  │  ├─ pkcs7.py
│  │     │  │  │  │  ├─ ssh.py
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  └─ __pycache__
│  │     │  │  │  │     ├─ base.cpython-313.pyc
│  │     │  │  │  │     ├─ pkcs12.cpython-313.pyc
│  │     │  │  │  │     ├─ pkcs7.cpython-313.pyc
│  │     │  │  │  │     ├─ ssh.cpython-313.pyc
│  │     │  │  │  │     └─ __init__.cpython-313.pyc
│  │     │  │  │  ├─ twofactor
│  │     │  │  │  │  ├─ hotp.py
│  │     │  │  │  │  ├─ totp.py
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  └─ __pycache__
│  │     │  │  │  │     ├─ hotp.cpython-313.pyc
│  │     │  │  │  │     ├─ totp.cpython-313.pyc
│  │     │  │  │  │     └─ __init__.cpython-313.pyc
│  │     │  │  │  ├─ _asymmetric.py
│  │     │  │  │  ├─ _cipheralgorithm.py
│  │     │  │  │  ├─ _serialization.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ cmac.cpython-313.pyc
│  │     │  │  │     ├─ constant_time.cpython-313.pyc
│  │     │  │  │     ├─ hashes.cpython-313.pyc
│  │     │  │  │     ├─ hmac.cpython-313.pyc
│  │     │  │  │     ├─ keywrap.cpython-313.pyc
│  │     │  │  │     ├─ padding.cpython-313.pyc
│  │     │  │  │     ├─ poly1305.cpython-313.pyc
│  │     │  │  │     ├─ _asymmetric.cpython-313.pyc
│  │     │  │  │     ├─ _cipheralgorithm.cpython-313.pyc
│  │     │  │  │     ├─ _serialization.cpython-313.pyc
│  │     │  │  │     └─ __init__.cpython-313.pyc
│  │     │  │  ├─ _oid.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ _oid.cpython-313.pyc
│  │     │  │     └─ __init__.cpython-313.pyc
│  │     │  ├─ py.typed
│  │     │  ├─ utils.py
│  │     │  ├─ x509
│  │     │  │  ├─ base.py
│  │     │  │  ├─ certificate_transparency.py
│  │     │  │  ├─ extensions.py
│  │     │  │  ├─ general_name.py
│  │     │  │  ├─ name.py
│  │     │  │  ├─ ocsp.py
│  │     │  │  ├─ oid.py
│  │     │  │  ├─ verification.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ base.cpython-313.pyc
│  │     │  │     ├─ certificate_transparency.cpython-313.pyc
│  │     │  │     ├─ extensions.cpython-313.pyc
│  │     │  │     ├─ general_name.cpython-313.pyc
│  │     │  │     ├─ name.cpython-313.pyc
│  │     │  │     ├─ ocsp.cpython-313.pyc
│  │     │  │     ├─ oid.cpython-313.pyc
│  │     │  │     ├─ verification.cpython-313.pyc
│  │     │  │     └─ __init__.cpython-313.pyc
│  │     │  ├─ __about__.py
│  │     │  ├─ __init__.py
│  │     │  └─ __pycache__
│  │     │     ├─ exceptions.cpython-313.pyc
│  │     │     ├─ fernet.cpython-313.pyc
│  │     │     ├─ utils.cpython-313.pyc
│  │     │     ├─ __about__.cpython-313.pyc
│  │     │     └─ __init__.cpython-313.pyc
│  │     ├─ cryptography-46.0.5.dist-info
│  │     │  ├─ INSTALLER
│  │     │  ├─ licenses
│  │     │  │  ├─ LICENSE
│  │     │  │  ├─ LICENSE.APACHE
│  │     │  │  └─ LICENSE.BSD
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  └─ WHEEL
│  │     ├─ cv2
│  │     │  ├─ aruco
│  │     │  │  └─ __init__.pyi
│  │     │  ├─ barcode
│  │     │  │  └─ __init__.pyi
│  │     │  ├─ bgsegm
│  │     │  │  └─ __init__.pyi
│  │     │  ├─ bioinspired
│  │     │  │  └─ __init__.pyi
│  │     │  ├─ ccm
│  │     │  │  └─ __init__.pyi
│  │     │  ├─ colored_kinfu
│  │     │  │  └─ __init__.pyi
│  │     │  ├─ config-3.py
│  │     │  ├─ config.py
│  │     │  ├─ cuda
│  │     │  │  └─ __init__.pyi
│  │     │  ├─ cv2.pyd
│  │     │  ├─ data
│  │     │  │  ├─ haarcascade_eye.xml
│  │     │  │  ├─ haarcascade_eye_tree_eyeglasses.xml
│  │     │  │  ├─ haarcascade_frontalcatface.xml
│  │     │  │  ├─ haarcascade_frontalcatface_extended.xml
│  │     │  │  ├─ haarcascade_frontalface_alt.xml
│  │     │  │  ├─ haarcascade_frontalface_alt2.xml
│  │     │  │  ├─ haarcascade_frontalface_alt_tree.xml
│  │     │  │  ├─ haarcascade_frontalface_default.xml
│  │     │  │  ├─ haarcascade_fullbody.xml
│  │     │  │  ├─ haarcascade_lefteye_2splits.xml
│  │     │  │  ├─ haarcascade_license_plate_rus_16stages.xml
│  │     │  │  ├─ haarcascade_lowerbody.xml
│  │     │  │  ├─ haarcascade_profileface.xml
│  │     │  │  ├─ haarcascade_righteye_2splits.xml
│  │     │  │  ├─ haarcascade_russian_plate_number.xml
│  │     │  │  ├─ haarcascade_smile.xml
│  │     │  │  ├─ haarcascade_upperbody.xml
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     └─ __init__.cpython-313.pyc
│  │     │  ├─ datasets
│  │     │  │  └─ __init__.pyi
│  │     │  ├─ detail
│  │     │  │  └─ __init__.pyi
│  │     │  ├─ dnn
│  │     │  │  └─ __init__.pyi
│  │     │  ├─ dnn_superres
│  │     │  │  └─ __init__.pyi
│  │     │  ├─ dpm
│  │     │  │  └─ __init__.pyi
│  │     │  ├─ dynafu
│  │     │  │  └─ __init__.pyi
│  │     │  ├─ Error
│  │     │  │  └─ __init__.pyi
│  │     │  ├─ face
│  │     │  │  └─ __init__.pyi
│  │     │  ├─ fisheye
│  │     │  │  └─ __init__.pyi
│  │     │  ├─ flann
│  │     │  │  └─ __init__.pyi
│  │     │  ├─ ft
│  │     │  │  └─ __init__.pyi
│  │     │  ├─ gapi
│  │     │  │  ├─ core
│  │     │  │  │  ├─ cpu
│  │     │  │  │  │  └─ __init__.pyi
│  │     │  │  │  ├─ fluid
│  │     │  │  │  │  └─ __init__.pyi
│  │     │  │  │  ├─ ocl
│  │     │  │  │  │  └─ __init__.pyi
│  │     │  │  │  └─ __init__.pyi
│  │     │  │  ├─ ie
│  │     │  │  │  ├─ detail
│  │     │  │  │  │  └─ __init__.pyi
│  │     │  │  │  └─ __init__.pyi
│  │     │  │  ├─ imgproc
│  │     │  │  │  ├─ fluid
│  │     │  │  │  │  └─ __init__.pyi
│  │     │  │  │  └─ __init__.pyi
│  │     │  │  ├─ oak
│  │     │  │  │  └─ __init__.pyi
│  │     │  │  ├─ onnx
│  │     │  │  │  ├─ ep
│  │     │  │  │  │  └─ __init__.pyi
│  │     │  │  │  └─ __init__.pyi
│  │     │  │  ├─ ot
│  │     │  │  │  ├─ cpu
│  │     │  │  │  │  └─ __init__.pyi
│  │     │  │  │  └─ __init__.pyi
│  │     │  │  ├─ ov
│  │     │  │  │  └─ __init__.pyi
│  │     │  │  ├─ own
│  │     │  │  │  ├─ detail
│  │     │  │  │  │  └─ __init__.pyi
│  │     │  │  │  └─ __init__.pyi
│  │     │  │  ├─ render
│  │     │  │  │  ├─ ocv
│  │     │  │  │  │  └─ __init__.pyi
│  │     │  │  │  └─ __init__.pyi
│  │     │  │  ├─ streaming
│  │     │  │  │  └─ __init__.pyi
│  │     │  │  ├─ video
│  │     │  │  │  └─ __init__.pyi
│  │     │  │  ├─ wip
│  │     │  │  │  ├─ draw
│  │     │  │  │  │  └─ __init__.pyi
│  │     │  │  │  ├─ gst
│  │     │  │  │  │  └─ __init__.pyi
│  │     │  │  │  ├─ onevpl
│  │     │  │  │  │  └─ __init__.pyi
│  │     │  │  │  └─ __init__.pyi
│  │     │  │  ├─ __init__.py
│  │     │  │  ├─ __init__.pyi
│  │     │  │  └─ __pycache__
│  │     │  │     └─ __init__.cpython-313.pyc
│  │     │  ├─ hfs
│  │     │  │  └─ __init__.pyi
│  │     │  ├─ img_hash
│  │     │  │  └─ __init__.pyi
│  │     │  ├─ instr
│  │     │  │  └─ __init__.pyi
│  │     │  ├─ intensity_transform
│  │     │  │  └─ __init__.pyi
│  │     │  ├─ ipp
│  │     │  │  └─ __init__.pyi
│  │     │  ├─ kinfu
│  │     │  │  ├─ detail
│  │     │  │  │  └─ __init__.pyi
│  │     │  │  └─ __init__.pyi
│  │     │  ├─ large_kinfu
│  │     │  │  └─ __init__.pyi
│  │     │  ├─ legacy
│  │     │  │  └─ __init__.pyi
│  │     │  ├─ LICENSE-3RD-PARTY.txt
│  │     │  ├─ LICENSE.txt
│  │     │  ├─ linemod
│  │     │  │  └─ __init__.pyi
│  │     │  ├─ line_descriptor
│  │     │  │  └─ __init__.pyi
│  │     │  ├─ load_config_py2.py
│  │     │  ├─ load_config_py3.py
│  │     │  ├─ mat_wrapper
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     └─ __init__.cpython-313.pyc
│  │     │  ├─ mcc
│  │     │  │  └─ __init__.pyi
│  │     │  ├─ misc
│  │     │  │  ├─ version.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ version.cpython-313.pyc
│  │     │  │     └─ __init__.cpython-313.pyc
│  │     │  ├─ ml
│  │     │  │  └─ __init__.pyi
│  │     │  ├─ motempl
│  │     │  │  └─ __init__.pyi
│  │     │  ├─ multicalib
│  │     │  │  └─ __init__.pyi
│  │     │  ├─ ocl
│  │     │  │  └─ __init__.pyi
│  │     │  ├─ ogl
│  │     │  │  └─ __init__.pyi
│  │     │  ├─ omnidir
│  │     │  │  └─ __init__.pyi
│  │     │  ├─ opencv_videoio_ffmpeg4100_64.dll
│  │     │  ├─ opencv_videoio_ffmpeg4130_64.dll
│  │     │  ├─ optflow
│  │     │  │  └─ __init__.pyi
│  │     │  ├─ parallel
│  │     │  │  └─ __init__.pyi
│  │     │  ├─ phase_unwrapping
│  │     │  │  └─ __init__.pyi
│  │     │  ├─ plot
│  │     │  │  └─ __init__.pyi
│  │     │  ├─ ppf_match_3d
│  │     │  │  └─ __init__.pyi
│  │     │  ├─ py.typed
│  │     │  ├─ quality
│  │     │  │  └─ __init__.pyi
│  │     │  ├─ rapid
│  │     │  │  └─ __init__.pyi
│  │     │  ├─ reg
│  │     │  │  └─ __init__.pyi
│  │     │  ├─ rgbd
│  │     │  │  └─ __init__.pyi
│  │     │  ├─ saliency
│  │     │  │  └─ __init__.pyi
│  │     │  ├─ samples
│  │     │  │  └─ __init__.pyi
│  │     │  ├─ segmentation
│  │     │  │  └─ __init__.pyi
│  │     │  ├─ signal
│  │     │  │  └─ __init__.pyi
│  │     │  ├─ stereo
│  │     │  │  └─ __init__.pyi
│  │     │  ├─ structured_light
│  │     │  │  └─ __init__.pyi
│  │     │  ├─ text
│  │     │  │  └─ __init__.pyi
│  │     │  ├─ typing
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     └─ __init__.cpython-313.pyc
│  │     │  ├─ utils
│  │     │  │  ├─ fs
│  │     │  │  │  └─ __init__.pyi
│  │     │  │  ├─ logging
│  │     │  │  │  └─ __init__.pyi
│  │     │  │  ├─ nested
│  │     │  │  │  └─ __init__.pyi
│  │     │  │  ├─ __init__.py
│  │     │  │  ├─ __init__.pyi
│  │     │  │  └─ __pycache__
│  │     │  │     └─ __init__.cpython-313.pyc
│  │     │  ├─ version.py
│  │     │  ├─ videoio_registry
│  │     │  │  └─ __init__.pyi
│  │     │  ├─ videostab
│  │     │  │  └─ __init__.pyi
│  │     │  ├─ wechat_qrcode
│  │     │  │  └─ __init__.pyi
│  │     │  ├─ xfeatures2d
│  │     │  │  └─ __init__.pyi
│  │     │  ├─ ximgproc
│  │     │  │  ├─ segmentation
│  │     │  │  │  └─ __init__.pyi
│  │     │  │  └─ __init__.pyi
│  │     │  ├─ xphoto
│  │     │  │  └─ __init__.pyi
│  │     │  ├─ __init__.py
│  │     │  ├─ __init__.pyi
│  │     │  └─ __pycache__
│  │     │     ├─ config-3.cpython-313.pyc
│  │     │     ├─ config.cpython-313.pyc
│  │     │     ├─ load_config_py2.cpython-313.pyc
│  │     │     ├─ load_config_py3.cpython-313.pyc
│  │     │     ├─ version.cpython-313.pyc
│  │     │     └─ __init__.cpython-313.pyc
│  │     ├─ cycler
│  │     │  ├─ py.typed
│  │     │  ├─ __init__.py
│  │     │  └─ __pycache__
│  │     │     └─ __init__.cpython-313.pyc
│  │     ├─ cycler-0.12.1.dist-info
│  │     │  ├─ INSTALLER
│  │     │  ├─ LICENSE
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  ├─ top_level.txt
│  │     │  └─ WHEEL
│  │     ├─ dateutil
│  │     │  ├─ easter.py
│  │     │  ├─ parser
│  │     │  │  ├─ isoparser.py
│  │     │  │  ├─ _parser.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ isoparser.cpython-313.pyc
│  │     │  │     ├─ _parser.cpython-313.pyc
│  │     │  │     └─ __init__.cpython-313.pyc
│  │     │  ├─ relativedelta.py
│  │     │  ├─ rrule.py
│  │     │  ├─ tz
│  │     │  │  ├─ tz.py
│  │     │  │  ├─ win.py
│  │     │  │  ├─ _common.py
│  │     │  │  ├─ _factories.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ tz.cpython-313.pyc
│  │     │  │     ├─ win.cpython-313.pyc
│  │     │  │     ├─ _common.cpython-313.pyc
│  │     │  │     ├─ _factories.cpython-313.pyc
│  │     │  │     └─ __init__.cpython-313.pyc
│  │     │  ├─ tzwin.py
│  │     │  ├─ utils.py
│  │     │  ├─ zoneinfo
│  │     │  │  ├─ dateutil-zoneinfo.tar.gz
│  │     │  │  ├─ rebuild.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ rebuild.cpython-313.pyc
│  │     │  │     └─ __init__.cpython-313.pyc
│  │     │  ├─ _common.py
│  │     │  ├─ _version.py
│  │     │  ├─ __init__.py
│  │     │  └─ __pycache__
│  │     │     ├─ easter.cpython-313.pyc
│  │     │     ├─ relativedelta.cpython-313.pyc
│  │     │     ├─ rrule.cpython-313.pyc
│  │     │     ├─ tzwin.cpython-313.pyc
│  │     │     ├─ utils.cpython-313.pyc
│  │     │     ├─ _common.cpython-313.pyc
│  │     │     ├─ _version.cpython-313.pyc
│  │     │     └─ __init__.cpython-313.pyc
│  │     ├─ distro
│  │     │  ├─ distro.py
│  │     │  ├─ py.typed
│  │     │  ├─ __init__.py
│  │     │  ├─ __main__.py
│  │     │  └─ __pycache__
│  │     │     ├─ distro.cpython-313.pyc
│  │     │     ├─ __init__.cpython-313.pyc
│  │     │     └─ __main__.cpython-313.pyc
│  │     ├─ distro-1.9.0.dist-info
│  │     │  ├─ entry_points.txt
│  │     │  ├─ INSTALLER
│  │     │  ├─ LICENSE
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  ├─ top_level.txt
│  │     │  └─ WHEEL
│  │     ├─ dotenv
│  │     │  ├─ cli.py
│  │     │  ├─ ipython.py
│  │     │  ├─ main.py
│  │     │  ├─ parser.py
│  │     │  ├─ py.typed
│  │     │  ├─ variables.py
│  │     │  ├─ version.py
│  │     │  ├─ __init__.py
│  │     │  ├─ __main__.py
│  │     │  └─ __pycache__
│  │     │     ├─ cli.cpython-313.pyc
│  │     │     ├─ ipython.cpython-313.pyc
│  │     │     ├─ main.cpython-313.pyc
│  │     │     ├─ parser.cpython-313.pyc
│  │     │     ├─ variables.cpython-313.pyc
│  │     │     ├─ version.cpython-313.pyc
│  │     │     ├─ __init__.cpython-313.pyc
│  │     │     └─ __main__.cpython-313.pyc
│  │     ├─ fastapi
│  │     │  ├─ applications.py
│  │     │  ├─ background.py
│  │     │  ├─ cli.py
│  │     │  ├─ concurrency.py
│  │     │  ├─ datastructures.py
│  │     │  ├─ dependencies
│  │     │  │  ├─ models.py
│  │     │  │  ├─ utils.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ models.cpython-313.pyc
│  │     │  │     ├─ utils.cpython-313.pyc
│  │     │  │     └─ __init__.cpython-313.pyc
│  │     │  ├─ encoders.py
│  │     │  ├─ exceptions.py
│  │     │  ├─ exception_handlers.py
│  │     │  ├─ logger.py
│  │     │  ├─ middleware
│  │     │  │  ├─ cors.py
│  │     │  │  ├─ gzip.py
│  │     │  │  ├─ httpsredirect.py
│  │     │  │  ├─ trustedhost.py
│  │     │  │  ├─ wsgi.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ cors.cpython-313.pyc
│  │     │  │     ├─ gzip.cpython-313.pyc
│  │     │  │     ├─ httpsredirect.cpython-313.pyc
│  │     │  │     ├─ trustedhost.cpython-313.pyc
│  │     │  │     ├─ wsgi.cpython-313.pyc
│  │     │  │     └─ __init__.cpython-313.pyc
│  │     │  ├─ openapi
│  │     │  │  ├─ constants.py
│  │     │  │  ├─ docs.py
│  │     │  │  ├─ models.py
│  │     │  │  ├─ utils.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ constants.cpython-313.pyc
│  │     │  │     ├─ docs.cpython-313.pyc
│  │     │  │     ├─ models.cpython-313.pyc
│  │     │  │     ├─ utils.cpython-313.pyc
│  │     │  │     └─ __init__.cpython-313.pyc
│  │     │  ├─ params.py
│  │     │  ├─ param_functions.py
│  │     │  ├─ py.typed
│  │     │  ├─ requests.py
│  │     │  ├─ responses.py
│  │     │  ├─ routing.py
│  │     │  ├─ security
│  │     │  │  ├─ api_key.py
│  │     │  │  ├─ base.py
│  │     │  │  ├─ http.py
│  │     │  │  ├─ oauth2.py
│  │     │  │  ├─ open_id_connect_url.py
│  │     │  │  ├─ utils.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ api_key.cpython-313.pyc
│  │     │  │     ├─ base.cpython-313.pyc
│  │     │  │     ├─ http.cpython-313.pyc
│  │     │  │     ├─ oauth2.cpython-313.pyc
│  │     │  │     ├─ open_id_connect_url.cpython-313.pyc
│  │     │  │     ├─ utils.cpython-313.pyc
│  │     │  │     └─ __init__.cpython-313.pyc
│  │     │  ├─ staticfiles.py
│  │     │  ├─ templating.py
│  │     │  ├─ testclient.py
│  │     │  ├─ types.py
│  │     │  ├─ utils.py
│  │     │  ├─ websockets.py
│  │     │  ├─ _compat.py
│  │     │  ├─ __init__.py
│  │     │  ├─ __main__.py
│  │     │  └─ __pycache__
│  │     │     ├─ applications.cpython-313.pyc
│  │     │     ├─ background.cpython-313.pyc
│  │     │     ├─ cli.cpython-313.pyc
│  │     │     ├─ concurrency.cpython-313.pyc
│  │     │     ├─ datastructures.cpython-313.pyc
│  │     │     ├─ encoders.cpython-313.pyc
│  │     │     ├─ exceptions.cpython-313.pyc
│  │     │     ├─ exception_handlers.cpython-313.pyc
│  │     │     ├─ logger.cpython-313.pyc
│  │     │     ├─ params.cpython-313.pyc
│  │     │     ├─ param_functions.cpython-313.pyc
│  │     │     ├─ requests.cpython-313.pyc
│  │     │     ├─ responses.cpython-313.pyc
│  │     │     ├─ routing.cpython-313.pyc
│  │     │     ├─ staticfiles.cpython-313.pyc
│  │     │     ├─ templating.cpython-313.pyc
│  │     │     ├─ testclient.cpython-313.pyc
│  │     │     ├─ types.cpython-313.pyc
│  │     │     ├─ utils.cpython-313.pyc
│  │     │     ├─ websockets.cpython-313.pyc
│  │     │     ├─ _compat.cpython-313.pyc
│  │     │     ├─ __init__.cpython-313.pyc
│  │     │     └─ __main__.cpython-313.pyc
│  │     ├─ fastapi-0.115.5.dist-info
│  │     │  ├─ entry_points.txt
│  │     │  ├─ INSTALLER
│  │     │  ├─ licenses
│  │     │  │  └─ LICENSE
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  ├─ REQUESTED
│  │     │  └─ WHEEL
│  │     ├─ ffmpeg
│  │     │  ├─ dag.py
│  │     │  ├─ nodes.py
│  │     │  ├─ _ffmpeg.py
│  │     │  ├─ _filters.py
│  │     │  ├─ _probe.py
│  │     │  ├─ _run.py
│  │     │  ├─ _utils.py
│  │     │  ├─ _view.py
│  │     │  ├─ __init__.py
│  │     │  └─ __pycache__
│  │     │     ├─ dag.cpython-313.pyc
│  │     │     ├─ nodes.cpython-313.pyc
│  │     │     ├─ _ffmpeg.cpython-313.pyc
│  │     │     ├─ _filters.cpython-313.pyc
│  │     │     ├─ _probe.cpython-313.pyc
│  │     │     ├─ _run.cpython-313.pyc
│  │     │     ├─ _utils.cpython-313.pyc
│  │     │     ├─ _view.cpython-313.pyc
│  │     │     └─ __init__.cpython-313.pyc
│  │     ├─ ffmpeg_python-0.2.0.dist-info
│  │     │  ├─ INSTALLER
│  │     │  ├─ LICENSE
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  ├─ REQUESTED
│  │     │  ├─ top_level.txt
│  │     │  └─ WHEEL
│  │     ├─ flatbuffers
│  │     │  ├─ builder.py
│  │     │  ├─ compat.py
│  │     │  ├─ encode.py
│  │     │  ├─ flexbuffers.py
│  │     │  ├─ number_types.py
│  │     │  ├─ packer.py
│  │     │  ├─ table.py
│  │     │  ├─ util.py
│  │     │  ├─ _version.py
│  │     │  ├─ __init__.py
│  │     │  └─ __pycache__
│  │     │     ├─ builder.cpython-313.pyc
│  │     │     ├─ compat.cpython-313.pyc
│  │     │     ├─ encode.cpython-313.pyc
│  │     │     ├─ flexbuffers.cpython-313.pyc
│  │     │     ├─ number_types.cpython-313.pyc
│  │     │     ├─ packer.cpython-313.pyc
│  │     │     ├─ table.cpython-313.pyc
│  │     │     ├─ util.cpython-313.pyc
│  │     │     ├─ _version.cpython-313.pyc
│  │     │     └─ __init__.cpython-313.pyc
│  │     ├─ flatbuffers-25.12.19.dist-info
│  │     │  ├─ INSTALLER
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  ├─ top_level.txt
│  │     │  └─ WHEEL
│  │     ├─ fontTools
│  │     │  ├─ afmLib.py
│  │     │  ├─ agl.py
│  │     │  ├─ annotations.py
│  │     │  ├─ cffLib
│  │     │  │  ├─ CFF2ToCFF.py
│  │     │  │  ├─ CFFToCFF2.py
│  │     │  │  ├─ specializer.py
│  │     │  │  ├─ transforms.py
│  │     │  │  ├─ width.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ CFF2ToCFF.cpython-313.pyc
│  │     │  │     ├─ CFFToCFF2.cpython-313.pyc
│  │     │  │     ├─ specializer.cpython-313.pyc
│  │     │  │     ├─ transforms.cpython-313.pyc
│  │     │  │     ├─ width.cpython-313.pyc
│  │     │  │     └─ __init__.cpython-313.pyc
│  │     │  ├─ colorLib
│  │     │  │  ├─ builder.py
│  │     │  │  ├─ errors.py
│  │     │  │  ├─ geometry.py
│  │     │  │  ├─ table_builder.py
│  │     │  │  ├─ unbuilder.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ builder.cpython-313.pyc
│  │     │  │     ├─ errors.cpython-313.pyc
│  │     │  │     ├─ geometry.cpython-313.pyc
│  │     │  │     ├─ table_builder.cpython-313.pyc
│  │     │  │     ├─ unbuilder.cpython-313.pyc
│  │     │  │     └─ __init__.cpython-313.pyc
│  │     │  ├─ config
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     └─ __init__.cpython-313.pyc
│  │     │  ├─ cu2qu
│  │     │  │  ├─ benchmark.py
│  │     │  │  ├─ cli.py
│  │     │  │  ├─ cu2qu.c
│  │     │  │  ├─ cu2qu.cp313-win_amd64.pyd
│  │     │  │  ├─ cu2qu.py
│  │     │  │  ├─ errors.py
│  │     │  │  ├─ ufo.py
│  │     │  │  ├─ __init__.py
│  │     │  │  ├─ __main__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ benchmark.cpython-313.pyc
│  │     │  │     ├─ cli.cpython-313.pyc
│  │     │  │     ├─ cu2qu.cpython-313.pyc
│  │     │  │     ├─ errors.cpython-313.pyc
│  │     │  │     ├─ ufo.cpython-313.pyc
│  │     │  │     ├─ __init__.cpython-313.pyc
│  │     │  │     └─ __main__.cpython-313.pyc
│  │     │  ├─ designspaceLib
│  │     │  │  ├─ split.py
│  │     │  │  ├─ statNames.py
│  │     │  │  ├─ types.py
│  │     │  │  ├─ __init__.py
│  │     │  │  ├─ __main__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ split.cpython-313.pyc
│  │     │  │     ├─ statNames.cpython-313.pyc
│  │     │  │     ├─ types.cpython-313.pyc
│  │     │  │     ├─ __init__.cpython-313.pyc
│  │     │  │     └─ __main__.cpython-313.pyc
│  │     │  ├─ diff
│  │     │  │  ├─ color.py
│  │     │  │  ├─ diff.py
│  │     │  │  ├─ utils.py
│  │     │  │  ├─ __init__.py
│  │     │  │  ├─ __main__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ color.cpython-313.pyc
│  │     │  │     ├─ diff.cpython-313.pyc
│  │     │  │     ├─ utils.cpython-313.pyc
│  │     │  │     ├─ __init__.cpython-313.pyc
│  │     │  │     └─ __main__.cpython-313.pyc
│  │     │  ├─ encodings
│  │     │  │  ├─ codecs.py
│  │     │  │  ├─ MacRoman.py
│  │     │  │  ├─ StandardEncoding.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ codecs.cpython-313.pyc
│  │     │  │     ├─ MacRoman.cpython-313.pyc
│  │     │  │     ├─ StandardEncoding.cpython-313.pyc
│  │     │  │     └─ __init__.cpython-313.pyc
│  │     │  ├─ feaLib
│  │     │  │  ├─ ast.py
│  │     │  │  ├─ builder.py
│  │     │  │  ├─ error.py
│  │     │  │  ├─ lexer.c
│  │     │  │  ├─ lexer.cp313-win_amd64.pyd
│  │     │  │  ├─ lexer.py
│  │     │  │  ├─ location.py
│  │     │  │  ├─ lookupDebugInfo.py
│  │     │  │  ├─ parser.py
│  │     │  │  ├─ variableScalar.py
│  │     │  │  ├─ __init__.py
│  │     │  │  ├─ __main__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ ast.cpython-313.pyc
│  │     │  │     ├─ builder.cpython-313.pyc
│  │     │  │     ├─ error.cpython-313.pyc
│  │     │  │     ├─ lexer.cpython-313.pyc
│  │     │  │     ├─ location.cpython-313.pyc
│  │     │  │     ├─ lookupDebugInfo.cpython-313.pyc
│  │     │  │     ├─ parser.cpython-313.pyc
│  │     │  │     ├─ variableScalar.cpython-313.pyc
│  │     │  │     ├─ __init__.cpython-313.pyc
│  │     │  │     └─ __main__.cpython-313.pyc
│  │     │  ├─ fontBuilder.py
│  │     │  ├─ help.py
│  │     │  ├─ merge
│  │     │  │  ├─ base.py
│  │     │  │  ├─ cmap.py
│  │     │  │  ├─ layout.py
│  │     │  │  ├─ options.py
│  │     │  │  ├─ tables.py
│  │     │  │  ├─ unicode.py
│  │     │  │  ├─ util.py
│  │     │  │  ├─ __init__.py
│  │     │  │  ├─ __main__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ base.cpython-313.pyc
│  │     │  │     ├─ cmap.cpython-313.pyc
│  │     │  │     ├─ layout.cpython-313.pyc
│  │     │  │     ├─ options.cpython-313.pyc
│  │     │  │     ├─ tables.cpython-313.pyc
│  │     │  │     ├─ unicode.cpython-313.pyc
│  │     │  │     ├─ util.cpython-313.pyc
│  │     │  │     ├─ __init__.cpython-313.pyc
│  │     │  │     └─ __main__.cpython-313.pyc
│  │     │  ├─ misc
│  │     │  │  ├─ arrayTools.py
│  │     │  │  ├─ bezierTools.c
│  │     │  │  ├─ bezierTools.cp313-win_amd64.pyd
│  │     │  │  ├─ bezierTools.py
│  │     │  │  ├─ classifyTools.py
│  │     │  │  ├─ cliTools.py
│  │     │  │  ├─ configTools.py
│  │     │  │  ├─ cython.py
│  │     │  │  ├─ dictTools.py
│  │     │  │  ├─ eexec.py
│  │     │  │  ├─ encodingTools.py
│  │     │  │  ├─ enumTools.py
│  │     │  │  ├─ etree.py
│  │     │  │  ├─ filenames.py
│  │     │  │  ├─ filesystem
│  │     │  │  │  ├─ _base.py
│  │     │  │  │  ├─ _copy.py
│  │     │  │  │  ├─ _errors.py
│  │     │  │  │  ├─ _info.py
│  │     │  │  │  ├─ _osfs.py
│  │     │  │  │  ├─ _path.py
│  │     │  │  │  ├─ _subfs.py
│  │     │  │  │  ├─ _tempfs.py
│  │     │  │  │  ├─ _tools.py
│  │     │  │  │  ├─ _walk.py
│  │     │  │  │  ├─ _zipfs.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ _base.cpython-313.pyc
│  │     │  │  │     ├─ _copy.cpython-313.pyc
│  │     │  │  │     ├─ _errors.cpython-313.pyc
│  │     │  │  │     ├─ _info.cpython-313.pyc
│  │     │  │  │     ├─ _osfs.cpython-313.pyc
│  │     │  │  │     ├─ _path.cpython-313.pyc
│  │     │  │  │     ├─ _subfs.cpython-313.pyc
│  │     │  │  │     ├─ _tempfs.cpython-313.pyc
│  │     │  │  │     ├─ _tools.cpython-313.pyc
│  │     │  │  │     ├─ _walk.cpython-313.pyc
│  │     │  │  │     ├─ _zipfs.cpython-313.pyc
│  │     │  │  │     └─ __init__.cpython-313.pyc
│  │     │  │  ├─ fixedTools.py
│  │     │  │  ├─ intTools.py
│  │     │  │  ├─ iterTools.py
│  │     │  │  ├─ lazyTools.py
│  │     │  │  ├─ loggingTools.py
│  │     │  │  ├─ macCreatorType.py
│  │     │  │  ├─ macRes.py
│  │     │  │  ├─ plistlib
│  │     │  │  │  ├─ py.typed
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     └─ __init__.cpython-313.pyc
│  │     │  │  ├─ psCharStrings.py
│  │     │  │  ├─ psLib.py
│  │     │  │  ├─ psOperators.py
│  │     │  │  ├─ py23.py
│  │     │  │  ├─ roundTools.py
│  │     │  │  ├─ sstruct.py
│  │     │  │  ├─ symfont.py
│  │     │  │  ├─ testTools.py
│  │     │  │  ├─ textTools.py
│  │     │  │  ├─ timeTools.py
│  │     │  │  ├─ transform.py
│  │     │  │  ├─ treeTools.py
│  │     │  │  ├─ vector.py
│  │     │  │  ├─ visitor.py
│  │     │  │  ├─ xmlReader.py
│  │     │  │  ├─ xmlWriter.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ arrayTools.cpython-313.pyc
│  │     │  │     ├─ bezierTools.cpython-313.pyc
│  │     │  │     ├─ classifyTools.cpython-313.pyc
│  │     │  │     ├─ cliTools.cpython-313.pyc
│  │     │  │     ├─ configTools.cpython-313.pyc
│  │     │  │     ├─ cython.cpython-313.pyc
│  │     │  │     ├─ dictTools.cpython-313.pyc
│  │     │  │     ├─ eexec.cpython-313.pyc
│  │     │  │     ├─ encodingTools.cpython-313.pyc
│  │     │  │     ├─ enumTools.cpython-313.pyc
│  │     │  │     ├─ etree.cpython-313.pyc
│  │     │  │     ├─ filenames.cpython-313.pyc
│  │     │  │     ├─ fixedTools.cpython-313.pyc
│  │     │  │     ├─ intTools.cpython-313.pyc
│  │     │  │     ├─ iterTools.cpython-313.pyc
│  │     │  │     ├─ lazyTools.cpython-313.pyc
│  │     │  │     ├─ loggingTools.cpython-313.pyc
│  │     │  │     ├─ macCreatorType.cpython-313.pyc
│  │     │  │     ├─ macRes.cpython-313.pyc
│  │     │  │     ├─ psCharStrings.cpython-313.pyc
│  │     │  │     ├─ psLib.cpython-313.pyc
│  │     │  │     ├─ psOperators.cpython-313.pyc
│  │     │  │     ├─ py23.cpython-313.pyc
│  │     │  │     ├─ roundTools.cpython-313.pyc
│  │     │  │     ├─ sstruct.cpython-313.pyc
│  │     │  │     ├─ symfont.cpython-313.pyc
│  │     │  │     ├─ testTools.cpython-313.pyc
│  │     │  │     ├─ textTools.cpython-313.pyc
│  │     │  │     ├─ timeTools.cpython-313.pyc
│  │     │  │     ├─ transform.cpython-313.pyc
│  │     │  │     ├─ treeTools.cpython-313.pyc
│  │     │  │     ├─ vector.cpython-313.pyc
│  │     │  │     ├─ visitor.cpython-313.pyc
│  │     │  │     ├─ xmlReader.cpython-313.pyc
│  │     │  │     ├─ xmlWriter.cpython-313.pyc
│  │     │  │     └─ __init__.cpython-313.pyc
│  │     │  ├─ mtiLib
│  │     │  │  ├─ __init__.py
│  │     │  │  ├─ __main__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ __init__.cpython-313.pyc
│  │     │  │     └─ __main__.cpython-313.pyc
│  │     │  ├─ otlLib
│  │     │  │  ├─ builder.py
│  │     │  │  ├─ error.py
│  │     │  │  ├─ maxContextCalc.py
│  │     │  │  ├─ optimize
│  │     │  │  │  ├─ gpos.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  ├─ __main__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ gpos.cpython-313.pyc
│  │     │  │  │     ├─ __init__.cpython-313.pyc
│  │     │  │  │     └─ __main__.cpython-313.pyc
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ builder.cpython-313.pyc
│  │     │  │     ├─ error.cpython-313.pyc
│  │     │  │     ├─ maxContextCalc.cpython-313.pyc
│  │     │  │     └─ __init__.cpython-313.pyc
│  │     │  ├─ pens
│  │     │  │  ├─ areaPen.py
│  │     │  │  ├─ basePen.py
│  │     │  │  ├─ boundsPen.py
│  │     │  │  ├─ cairoPen.py
│  │     │  │  ├─ cocoaPen.py
│  │     │  │  ├─ cu2quPen.py
│  │     │  │  ├─ explicitClosingLinePen.py
│  │     │  │  ├─ filterPen.py
│  │     │  │  ├─ freetypePen.py
│  │     │  │  ├─ hashPointPen.py
│  │     │  │  ├─ momentsPen.c
│  │     │  │  ├─ momentsPen.cp313-win_amd64.pyd
│  │     │  │  ├─ momentsPen.py
│  │     │  │  ├─ perimeterPen.py
│  │     │  │  ├─ pointInsidePen.py
│  │     │  │  ├─ pointPen.py
│  │     │  │  ├─ qtPen.py
│  │     │  │  ├─ qu2cuPen.py
│  │     │  │  ├─ quartzPen.py
│  │     │  │  ├─ recordingPen.py
│  │     │  │  ├─ reportLabPen.py
│  │     │  │  ├─ reverseContourPen.py
│  │     │  │  ├─ roundingPen.py
│  │     │  │  ├─ statisticsPen.py
│  │     │  │  ├─ svgPathPen.py
│  │     │  │  ├─ t2CharStringPen.py
│  │     │  │  ├─ teePen.py
│  │     │  │  ├─ transformPen.py
│  │     │  │  ├─ ttGlyphPen.py
│  │     │  │  ├─ wxPen.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ areaPen.cpython-313.pyc
│  │     │  │     ├─ basePen.cpython-313.pyc
│  │     │  │     ├─ boundsPen.cpython-313.pyc
│  │     │  │     ├─ cairoPen.cpython-313.pyc
│  │     │  │     ├─ cocoaPen.cpython-313.pyc
│  │     │  │     ├─ cu2quPen.cpython-313.pyc
│  │     │  │     ├─ explicitClosingLinePen.cpython-313.pyc
│  │     │  │     ├─ filterPen.cpython-313.pyc
│  │     │  │     ├─ freetypePen.cpython-313.pyc
│  │     │  │     ├─ hashPointPen.cpython-313.pyc
│  │     │  │     ├─ momentsPen.cpython-313.pyc
│  │     │  │     ├─ perimeterPen.cpython-313.pyc
│  │     │  │     ├─ pointInsidePen.cpython-313.pyc
│  │     │  │     ├─ pointPen.cpython-313.pyc
│  │     │  │     ├─ qtPen.cpython-313.pyc
│  │     │  │     ├─ qu2cuPen.cpython-313.pyc
│  │     │  │     ├─ quartzPen.cpython-313.pyc
│  │     │  │     ├─ recordingPen.cpython-313.pyc
│  │     │  │     ├─ reportLabPen.cpython-313.pyc
│  │     │  │     ├─ reverseContourPen.cpython-313.pyc
│  │     │  │     ├─ roundingPen.cpython-313.pyc
│  │     │  │     ├─ statisticsPen.cpython-313.pyc
│  │     │  │     ├─ svgPathPen.cpython-313.pyc
│  │     │  │     ├─ t2CharStringPen.cpython-313.pyc
│  │     │  │     ├─ teePen.cpython-313.pyc
│  │     │  │     ├─ transformPen.cpython-313.pyc
│  │     │  │     ├─ ttGlyphPen.cpython-313.pyc
│  │     │  │     ├─ wxPen.cpython-313.pyc
│  │     │  │     └─ __init__.cpython-313.pyc
│  │     │  ├─ qu2cu
│  │     │  │  ├─ benchmark.py
│  │     │  │  ├─ cli.py
│  │     │  │  ├─ qu2cu.c
│  │     │  │  ├─ qu2cu.cp313-win_amd64.pyd
│  │     │  │  ├─ qu2cu.py
│  │     │  │  ├─ __init__.py
│  │     │  │  ├─ __main__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ benchmark.cpython-313.pyc
│  │     │  │     ├─ cli.cpython-313.pyc
│  │     │  │     ├─ qu2cu.cpython-313.pyc
│  │     │  │     ├─ __init__.cpython-313.pyc
│  │     │  │     └─ __main__.cpython-313.pyc
│  │     │  ├─ subset
│  │     │  │  ├─ cff.py
│  │     │  │  ├─ svg.py
│  │     │  │  ├─ util.py
│  │     │  │  ├─ __init__.py
│  │     │  │  ├─ __main__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ cff.cpython-313.pyc
│  │     │  │     ├─ svg.cpython-313.pyc
│  │     │  │     ├─ util.cpython-313.pyc
│  │     │  │     ├─ __init__.cpython-313.pyc
│  │     │  │     └─ __main__.cpython-313.pyc
│  │     │  ├─ svgLib
│  │     │  │  ├─ path
│  │     │  │  │  ├─ arc.py
│  │     │  │  │  ├─ parser.py
│  │     │  │  │  ├─ shapes.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ arc.cpython-313.pyc
│  │     │  │  │     ├─ parser.cpython-313.pyc
│  │     │  │  │     ├─ shapes.cpython-313.pyc
│  │     │  │  │     └─ __init__.cpython-313.pyc
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     └─ __init__.cpython-313.pyc
│  │     │  ├─ t1Lib
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     └─ __init__.cpython-313.pyc
│  │     │  ├─ tfmLib.py
│  │     │  ├─ ttLib
│  │     │  │  ├─ macUtils.py
│  │     │  │  ├─ removeOverlaps.py
│  │     │  │  ├─ reorderGlyphs.py
│  │     │  │  ├─ scaleUpem.py
│  │     │  │  ├─ sfnt.py
│  │     │  │  ├─ standardGlyphOrder.py
│  │     │  │  ├─ tables
│  │     │  │  │  ├─ asciiTable.py
│  │     │  │  │  ├─ BitmapGlyphMetrics.py
│  │     │  │  │  ├─ B_A_S_E_.py
│  │     │  │  │  ├─ C_B_D_T_.py
│  │     │  │  │  ├─ C_B_L_C_.py
│  │     │  │  │  ├─ C_F_F_.py
│  │     │  │  │  ├─ C_F_F__2.py
│  │     │  │  │  ├─ C_O_L_R_.py
│  │     │  │  │  ├─ C_P_A_L_.py
│  │     │  │  │  ├─ DefaultTable.py
│  │     │  │  │  ├─ D_S_I_G_.py
│  │     │  │  │  ├─ D__e_b_g.py
│  │     │  │  │  ├─ E_B_D_T_.py
│  │     │  │  │  ├─ E_B_L_C_.py
│  │     │  │  │  ├─ F_F_T_M_.py
│  │     │  │  │  ├─ F__e_a_t.py
│  │     │  │  │  ├─ grUtils.py
│  │     │  │  │  ├─ G_D_E_F_.py
│  │     │  │  │  ├─ G_P_O_S_.py
│  │     │  │  │  ├─ G_S_U_B_.py
│  │     │  │  │  ├─ G_V_A_R_.py
│  │     │  │  │  ├─ G__l_a_t.py
│  │     │  │  │  ├─ G__l_o_c.py
│  │     │  │  │  ├─ H_V_A_R_.py
│  │     │  │  │  ├─ J_S_T_F_.py
│  │     │  │  │  ├─ L_T_S_H_.py
│  │     │  │  │  ├─ M_A_T_H_.py
│  │     │  │  │  ├─ M_V_A_R_.py
│  │     │  │  │  ├─ otBase.py
│  │     │  │  │  ├─ otConverters.py
│  │     │  │  │  ├─ otData.py
│  │     │  │  │  ├─ otTables.py
│  │     │  │  │  ├─ otTraverse.py
│  │     │  │  │  ├─ O_S_2f_2.py
│  │     │  │  │  ├─ sbixGlyph.py
│  │     │  │  │  ├─ sbixStrike.py
│  │     │  │  │  ├─ S_T_A_T_.py
│  │     │  │  │  ├─ S_V_G_.py
│  │     │  │  │  ├─ S__i_l_f.py
│  │     │  │  │  ├─ S__i_l_l.py
│  │     │  │  │  ├─ table_API_readme.txt
│  │     │  │  │  ├─ ttProgram.py
│  │     │  │  │  ├─ TupleVariation.py
│  │     │  │  │  ├─ T_S_I_B_.py
│  │     │  │  │  ├─ T_S_I_C_.py
│  │     │  │  │  ├─ T_S_I_D_.py
│  │     │  │  │  ├─ T_S_I_J_.py
│  │     │  │  │  ├─ T_S_I_P_.py
│  │     │  │  │  ├─ T_S_I_S_.py
│  │     │  │  │  ├─ T_S_I_V_.py
│  │     │  │  │  ├─ T_S_I__0.py
│  │     │  │  │  ├─ T_S_I__1.py
│  │     │  │  │  ├─ T_S_I__2.py
│  │     │  │  │  ├─ T_S_I__3.py
│  │     │  │  │  ├─ T_S_I__5.py
│  │     │  │  │  ├─ T_T_F_A_.py
│  │     │  │  │  ├─ V_A_R_C_.py
│  │     │  │  │  ├─ V_D_M_X_.py
│  │     │  │  │  ├─ V_O_R_G_.py
│  │     │  │  │  ├─ V_V_A_R_.py
│  │     │  │  │  ├─ _a_n_k_r.py
│  │     │  │  │  ├─ _a_v_a_r.py
│  │     │  │  │  ├─ _b_s_l_n.py
│  │     │  │  │  ├─ _c_i_d_g.py
│  │     │  │  │  ├─ _c_m_a_p.py
│  │     │  │  │  ├─ _c_v_a_r.py
│  │     │  │  │  ├─ _c_v_t.py
│  │     │  │  │  ├─ _f_e_a_t.py
│  │     │  │  │  ├─ _f_p_g_m.py
│  │     │  │  │  ├─ _f_v_a_r.py
│  │     │  │  │  ├─ _g_a_s_p.py
│  │     │  │  │  ├─ _g_c_i_d.py
│  │     │  │  │  ├─ _g_l_y_f.py
│  │     │  │  │  ├─ _g_v_a_r.py
│  │     │  │  │  ├─ _h_d_m_x.py
│  │     │  │  │  ├─ _h_e_a_d.py
│  │     │  │  │  ├─ _h_h_e_a.py
│  │     │  │  │  ├─ _h_m_t_x.py
│  │     │  │  │  ├─ _k_e_r_n.py
│  │     │  │  │  ├─ _l_c_a_r.py
│  │     │  │  │  ├─ _l_o_c_a.py
│  │     │  │  │  ├─ _l_t_a_g.py
│  │     │  │  │  ├─ _m_a_x_p.py
│  │     │  │  │  ├─ _m_e_t_a.py
│  │     │  │  │  ├─ _m_o_r_t.py
│  │     │  │  │  ├─ _m_o_r_x.py
│  │     │  │  │  ├─ _n_a_m_e.py
│  │     │  │  │  ├─ _o_p_b_d.py
│  │     │  │  │  ├─ _p_o_s_t.py
│  │     │  │  │  ├─ _p_r_e_p.py
│  │     │  │  │  ├─ _p_r_o_p.py
│  │     │  │  │  ├─ _s_b_i_x.py
│  │     │  │  │  ├─ _t_r_a_k.py
│  │     │  │  │  ├─ _v_h_e_a.py
│  │     │  │  │  ├─ _v_m_t_x.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ asciiTable.cpython-313.pyc
│  │     │  │  │     ├─ BitmapGlyphMetrics.cpython-313.pyc
│  │     │  │  │     ├─ B_A_S_E_.cpython-313.pyc
│  │     │  │  │     ├─ C_B_D_T_.cpython-313.pyc
│  │     │  │  │     ├─ C_B_L_C_.cpython-313.pyc
│  │     │  │  │     ├─ C_F_F_.cpython-313.pyc
│  │     │  │  │     ├─ C_F_F__2.cpython-313.pyc
│  │     │  │  │     ├─ C_O_L_R_.cpython-313.pyc
│  │     │  │  │     ├─ C_P_A_L_.cpython-313.pyc
│  │     │  │  │     ├─ DefaultTable.cpython-313.pyc
│  │     │  │  │     ├─ D_S_I_G_.cpython-313.pyc
│  │     │  │  │     ├─ D__e_b_g.cpython-313.pyc
│  │     │  │  │     ├─ E_B_D_T_.cpython-313.pyc
│  │     │  │  │     ├─ E_B_L_C_.cpython-313.pyc
│  │     │  │  │     ├─ F_F_T_M_.cpython-313.pyc
│  │     │  │  │     ├─ F__e_a_t.cpython-313.pyc
│  │     │  │  │     ├─ grUtils.cpython-313.pyc
│  │     │  │  │     ├─ G_D_E_F_.cpython-313.pyc
│  │     │  │  │     ├─ G_P_O_S_.cpython-313.pyc
│  │     │  │  │     ├─ G_S_U_B_.cpython-313.pyc
│  │     │  │  │     ├─ G_V_A_R_.cpython-313.pyc
│  │     │  │  │     ├─ G__l_a_t.cpython-313.pyc
│  │     │  │  │     ├─ G__l_o_c.cpython-313.pyc
│  │     │  │  │     ├─ H_V_A_R_.cpython-313.pyc
│  │     │  │  │     ├─ J_S_T_F_.cpython-313.pyc
│  │     │  │  │     ├─ L_T_S_H_.cpython-313.pyc
│  │     │  │  │     ├─ M_A_T_H_.cpython-313.pyc
│  │     │  │  │     ├─ M_V_A_R_.cpython-313.pyc
│  │     │  │  │     ├─ otBase.cpython-313.pyc
│  │     │  │  │     ├─ otConverters.cpython-313.pyc
│  │     │  │  │     ├─ otData.cpython-313.pyc
│  │     │  │  │     ├─ otTables.cpython-313.pyc
│  │     │  │  │     ├─ otTraverse.cpython-313.pyc
│  │     │  │  │     ├─ O_S_2f_2.cpython-313.pyc
│  │     │  │  │     ├─ sbixGlyph.cpython-313.pyc
│  │     │  │  │     ├─ sbixStrike.cpython-313.pyc
│  │     │  │  │     ├─ S_T_A_T_.cpython-313.pyc
│  │     │  │  │     ├─ S_V_G_.cpython-313.pyc
│  │     │  │  │     ├─ S__i_l_f.cpython-313.pyc
│  │     │  │  │     ├─ S__i_l_l.cpython-313.pyc
│  │     │  │  │     ├─ ttProgram.cpython-313.pyc
│  │     │  │  │     ├─ TupleVariation.cpython-313.pyc
│  │     │  │  │     ├─ T_S_I_B_.cpython-313.pyc
│  │     │  │  │     ├─ T_S_I_C_.cpython-313.pyc
│  │     │  │  │     ├─ T_S_I_D_.cpython-313.pyc
│  │     │  │  │     ├─ T_S_I_J_.cpython-313.pyc
│  │     │  │  │     ├─ T_S_I_P_.cpython-313.pyc
│  │     │  │  │     ├─ T_S_I_S_.cpython-313.pyc
│  │     │  │  │     ├─ T_S_I_V_.cpython-313.pyc
│  │     │  │  │     ├─ T_S_I__0.cpython-313.pyc
│  │     │  │  │     ├─ T_S_I__1.cpython-313.pyc
│  │     │  │  │     ├─ T_S_I__2.cpython-313.pyc
│  │     │  │  │     ├─ T_S_I__3.cpython-313.pyc
│  │     │  │  │     ├─ T_S_I__5.cpython-313.pyc
│  │     │  │  │     ├─ T_T_F_A_.cpython-313.pyc
│  │     │  │  │     ├─ V_A_R_C_.cpython-313.pyc
│  │     │  │  │     ├─ V_D_M_X_.cpython-313.pyc
│  │     │  │  │     ├─ V_O_R_G_.cpython-313.pyc
│  │     │  │  │     ├─ V_V_A_R_.cpython-313.pyc
│  │     │  │  │     ├─ _a_n_k_r.cpython-313.pyc
│  │     │  │  │     ├─ _a_v_a_r.cpython-313.pyc
│  │     │  │  │     ├─ _b_s_l_n.cpython-313.pyc
│  │     │  │  │     ├─ _c_i_d_g.cpython-313.pyc
│  │     │  │  │     ├─ _c_m_a_p.cpython-313.pyc
│  │     │  │  │     ├─ _c_v_a_r.cpython-313.pyc
│  │     │  │  │     ├─ _c_v_t.cpython-313.pyc
│  │     │  │  │     ├─ _f_e_a_t.cpython-313.pyc
│  │     │  │  │     ├─ _f_p_g_m.cpython-313.pyc
│  │     │  │  │     ├─ _f_v_a_r.cpython-313.pyc
│  │     │  │  │     ├─ _g_a_s_p.cpython-313.pyc
│  │     │  │  │     ├─ _g_c_i_d.cpython-313.pyc
│  │     │  │  │     ├─ _g_l_y_f.cpython-313.pyc
│  │     │  │  │     ├─ _g_v_a_r.cpython-313.pyc
│  │     │  │  │     ├─ _h_d_m_x.cpython-313.pyc
│  │     │  │  │     ├─ _h_e_a_d.cpython-313.pyc
│  │     │  │  │     ├─ _h_h_e_a.cpython-313.pyc
│  │     │  │  │     ├─ _h_m_t_x.cpython-313.pyc
│  │     │  │  │     ├─ _k_e_r_n.cpython-313.pyc
│  │     │  │  │     ├─ _l_c_a_r.cpython-313.pyc
│  │     │  │  │     ├─ _l_o_c_a.cpython-313.pyc
│  │     │  │  │     ├─ _l_t_a_g.cpython-313.pyc
│  │     │  │  │     ├─ _m_a_x_p.cpython-313.pyc
│  │     │  │  │     ├─ _m_e_t_a.cpython-313.pyc
│  │     │  │  │     ├─ _m_o_r_t.cpython-313.pyc
│  │     │  │  │     ├─ _m_o_r_x.cpython-313.pyc
│  │     │  │  │     ├─ _n_a_m_e.cpython-313.pyc
│  │     │  │  │     ├─ _o_p_b_d.cpython-313.pyc
│  │     │  │  │     ├─ _p_o_s_t.cpython-313.pyc
│  │     │  │  │     ├─ _p_r_e_p.cpython-313.pyc
│  │     │  │  │     ├─ _p_r_o_p.cpython-313.pyc
│  │     │  │  │     ├─ _s_b_i_x.cpython-313.pyc
│  │     │  │  │     ├─ _t_r_a_k.cpython-313.pyc
│  │     │  │  │     ├─ _v_h_e_a.cpython-313.pyc
│  │     │  │  │     ├─ _v_m_t_x.cpython-313.pyc
│  │     │  │  │     └─ __init__.cpython-313.pyc
│  │     │  │  ├─ ttCollection.py
│  │     │  │  ├─ ttFont.py
│  │     │  │  ├─ ttGlyphSet.py
│  │     │  │  ├─ ttVisitor.py
│  │     │  │  ├─ woff2.py
│  │     │  │  ├─ __init__.py
│  │     │  │  ├─ __main__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ macUtils.cpython-313.pyc
│  │     │  │     ├─ removeOverlaps.cpython-313.pyc
│  │     │  │     ├─ reorderGlyphs.cpython-313.pyc
│  │     │  │     ├─ scaleUpem.cpython-313.pyc
│  │     │  │     ├─ sfnt.cpython-313.pyc
│  │     │  │     ├─ standardGlyphOrder.cpython-313.pyc
│  │     │  │     ├─ ttCollection.cpython-313.pyc
│  │     │  │     ├─ ttFont.cpython-313.pyc
│  │     │  │     ├─ ttGlyphSet.cpython-313.pyc
│  │     │  │     ├─ ttVisitor.cpython-313.pyc
│  │     │  │     ├─ woff2.cpython-313.pyc
│  │     │  │     ├─ __init__.cpython-313.pyc
│  │     │  │     └─ __main__.cpython-313.pyc
│  │     │  ├─ ttx.py
│  │     │  ├─ ufoLib
│  │     │  │  ├─ converters.py
│  │     │  │  ├─ errors.py
│  │     │  │  ├─ etree.py
│  │     │  │  ├─ filenames.py
│  │     │  │  ├─ glifLib.py
│  │     │  │  ├─ kerning.py
│  │     │  │  ├─ plistlib.py
│  │     │  │  ├─ pointPen.py
│  │     │  │  ├─ utils.py
│  │     │  │  ├─ validators.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ converters.cpython-313.pyc
│  │     │  │     ├─ errors.cpython-313.pyc
│  │     │  │     ├─ etree.cpython-313.pyc
│  │     │  │     ├─ filenames.cpython-313.pyc
│  │     │  │     ├─ glifLib.cpython-313.pyc
│  │     │  │     ├─ kerning.cpython-313.pyc
│  │     │  │     ├─ plistlib.cpython-313.pyc
│  │     │  │     ├─ pointPen.cpython-313.pyc
│  │     │  │     ├─ utils.cpython-313.pyc
│  │     │  │     ├─ validators.cpython-313.pyc
│  │     │  │     └─ __init__.cpython-313.pyc
│  │     │  ├─ unicode.py
│  │     │  ├─ unicodedata
│  │     │  │  ├─ Blocks.py
│  │     │  │  ├─ Mirrored.py
│  │     │  │  ├─ OTTags.py
│  │     │  │  ├─ ScriptExtensions.py
│  │     │  │  ├─ Scripts.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ Blocks.cpython-313.pyc
│  │     │  │     ├─ Mirrored.cpython-313.pyc
│  │     │  │     ├─ OTTags.cpython-313.pyc
│  │     │  │     ├─ ScriptExtensions.cpython-313.pyc
│  │     │  │     ├─ Scripts.cpython-313.pyc
│  │     │  │     └─ __init__.cpython-313.pyc
│  │     │  ├─ varLib
│  │     │  │  ├─ avar
│  │     │  │  │  ├─ build.py
│  │     │  │  │  ├─ map.py
│  │     │  │  │  ├─ plan.py
│  │     │  │  │  ├─ unbuild.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  ├─ __main__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ build.cpython-313.pyc
│  │     │  │  │     ├─ map.cpython-313.pyc
│  │     │  │  │     ├─ plan.cpython-313.pyc
│  │     │  │  │     ├─ unbuild.cpython-313.pyc
│  │     │  │  │     ├─ __init__.cpython-313.pyc
│  │     │  │  │     └─ __main__.cpython-313.pyc
│  │     │  │  ├─ avarPlanner.py
│  │     │  │  ├─ builder.py
│  │     │  │  ├─ cff.py
│  │     │  │  ├─ errors.py
│  │     │  │  ├─ featureVars.py
│  │     │  │  ├─ hvar.py
│  │     │  │  ├─ instancer
│  │     │  │  │  ├─ featureVars.py
│  │     │  │  │  ├─ names.py
│  │     │  │  │  ├─ solver.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  ├─ __main__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ featureVars.cpython-313.pyc
│  │     │  │  │     ├─ names.cpython-313.pyc
│  │     │  │  │     ├─ solver.cpython-313.pyc
│  │     │  │  │     ├─ __init__.cpython-313.pyc
│  │     │  │  │     └─ __main__.cpython-313.pyc
│  │     │  │  ├─ interpolatable.py
│  │     │  │  ├─ interpolatableHelpers.py
│  │     │  │  ├─ interpolatablePlot.py
│  │     │  │  ├─ interpolatableTestContourOrder.py
│  │     │  │  ├─ interpolatableTestStartingPoint.py
│  │     │  │  ├─ interpolate_layout.py
│  │     │  │  ├─ iup.c
│  │     │  │  ├─ iup.cp313-win_amd64.pyd
│  │     │  │  ├─ iup.py
│  │     │  │  ├─ merger.py
│  │     │  │  ├─ models.py
│  │     │  │  ├─ multiVarStore.py
│  │     │  │  ├─ mutator.py
│  │     │  │  ├─ mvar.py
│  │     │  │  ├─ plot.py
│  │     │  │  ├─ stat.py
│  │     │  │  ├─ varStore.py
│  │     │  │  ├─ __init__.py
│  │     │  │  ├─ __main__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ avarPlanner.cpython-313.pyc
│  │     │  │     ├─ builder.cpython-313.pyc
│  │     │  │     ├─ cff.cpython-313.pyc
│  │     │  │     ├─ errors.cpython-313.pyc
│  │     │  │     ├─ featureVars.cpython-313.pyc
│  │     │  │     ├─ hvar.cpython-313.pyc
│  │     │  │     ├─ interpolatable.cpython-313.pyc
│  │     │  │     ├─ interpolatableHelpers.cpython-313.pyc
│  │     │  │     ├─ interpolatablePlot.cpython-313.pyc
│  │     │  │     ├─ interpolatableTestContourOrder.cpython-313.pyc
│  │     │  │     ├─ interpolatableTestStartingPoint.cpython-313.pyc
│  │     │  │     ├─ interpolate_layout.cpython-313.pyc
│  │     │  │     ├─ iup.cpython-313.pyc
│  │     │  │     ├─ merger.cpython-313.pyc
│  │     │  │     ├─ models.cpython-313.pyc
│  │     │  │     ├─ multiVarStore.cpython-313.pyc
│  │     │  │     ├─ mutator.cpython-313.pyc
│  │     │  │     ├─ mvar.cpython-313.pyc
│  │     │  │     ├─ plot.cpython-313.pyc
│  │     │  │     ├─ stat.cpython-313.pyc
│  │     │  │     ├─ varStore.cpython-313.pyc
│  │     │  │     ├─ __init__.cpython-313.pyc
│  │     │  │     └─ __main__.cpython-313.pyc
│  │     │  ├─ voltLib
│  │     │  │  ├─ ast.py
│  │     │  │  ├─ error.py
│  │     │  │  ├─ lexer.py
│  │     │  │  ├─ parser.py
│  │     │  │  ├─ voltToFea.py
│  │     │  │  ├─ __init__.py
│  │     │  │  ├─ __main__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ ast.cpython-313.pyc
│  │     │  │     ├─ error.cpython-313.pyc
│  │     │  │     ├─ lexer.cpython-313.pyc
│  │     │  │     ├─ parser.cpython-313.pyc
│  │     │  │     ├─ voltToFea.cpython-313.pyc
│  │     │  │     ├─ __init__.cpython-313.pyc
│  │     │  │     └─ __main__.cpython-313.pyc
│  │     │  ├─ __init__.py
│  │     │  ├─ __main__.py
│  │     │  └─ __pycache__
│  │     │     ├─ afmLib.cpython-313.pyc
│  │     │     ├─ agl.cpython-313.pyc
│  │     │     ├─ annotations.cpython-313.pyc
│  │     │     ├─ fontBuilder.cpython-313.pyc
│  │     │     ├─ help.cpython-313.pyc
│  │     │     ├─ tfmLib.cpython-313.pyc
│  │     │     ├─ ttx.cpython-313.pyc
│  │     │     ├─ unicode.cpython-313.pyc
│  │     │     ├─ __init__.cpython-313.pyc
│  │     │     └─ __main__.cpython-313.pyc
│  │     ├─ fonttools-4.62.1.dist-info
│  │     │  ├─ entry_points.txt
│  │     │  ├─ INSTALLER
│  │     │  ├─ licenses
│  │     │  │  ├─ LICENSE
│  │     │  │  └─ LICENSE.external
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  ├─ top_level.txt
│  │     │  └─ WHEEL
│  │     ├─ future
│  │     │  ├─ backports
│  │     │  │  ├─ datetime.py
│  │     │  │  ├─ email
│  │     │  │  │  ├─ base64mime.py
│  │     │  │  │  ├─ charset.py
│  │     │  │  │  ├─ encoders.py
│  │     │  │  │  ├─ errors.py
│  │     │  │  │  ├─ feedparser.py
│  │     │  │  │  ├─ generator.py
│  │     │  │  │  ├─ header.py
│  │     │  │  │  ├─ headerregistry.py
│  │     │  │  │  ├─ iterators.py
│  │     │  │  │  ├─ message.py
│  │     │  │  │  ├─ mime
│  │     │  │  │  │  ├─ application.py
│  │     │  │  │  │  ├─ audio.py
│  │     │  │  │  │  ├─ base.py
│  │     │  │  │  │  ├─ image.py
│  │     │  │  │  │  ├─ message.py
│  │     │  │  │  │  ├─ multipart.py
│  │     │  │  │  │  ├─ nonmultipart.py
│  │     │  │  │  │  ├─ text.py
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  └─ __pycache__
│  │     │  │  │  │     ├─ application.cpython-313.pyc
│  │     │  │  │  │     ├─ audio.cpython-313.pyc
│  │     │  │  │  │     ├─ base.cpython-313.pyc
│  │     │  │  │  │     ├─ image.cpython-313.pyc
│  │     │  │  │  │     ├─ message.cpython-313.pyc
│  │     │  │  │  │     ├─ multipart.cpython-313.pyc
│  │     │  │  │  │     ├─ nonmultipart.cpython-313.pyc
│  │     │  │  │  │     ├─ text.cpython-313.pyc
│  │     │  │  │  │     └─ __init__.cpython-313.pyc
│  │     │  │  │  ├─ parser.py
│  │     │  │  │  ├─ policy.py
│  │     │  │  │  ├─ quoprimime.py
│  │     │  │  │  ├─ utils.py
│  │     │  │  │  ├─ _encoded_words.py
│  │     │  │  │  ├─ _header_value_parser.py
│  │     │  │  │  ├─ _parseaddr.py
│  │     │  │  │  ├─ _policybase.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ base64mime.cpython-313.pyc
│  │     │  │  │     ├─ charset.cpython-313.pyc
│  │     │  │  │     ├─ encoders.cpython-313.pyc
│  │     │  │  │     ├─ errors.cpython-313.pyc
│  │     │  │  │     ├─ feedparser.cpython-313.pyc
│  │     │  │  │     ├─ generator.cpython-313.pyc
│  │     │  │  │     ├─ header.cpython-313.pyc
│  │     │  │  │     ├─ headerregistry.cpython-313.pyc
│  │     │  │  │     ├─ iterators.cpython-313.pyc
│  │     │  │  │     ├─ message.cpython-313.pyc
│  │     │  │  │     ├─ parser.cpython-313.pyc
│  │     │  │  │     ├─ policy.cpython-313.pyc
│  │     │  │  │     ├─ quoprimime.cpython-313.pyc
│  │     │  │  │     ├─ utils.cpython-313.pyc
│  │     │  │  │     ├─ _encoded_words.cpython-313.pyc
│  │     │  │  │     ├─ _header_value_parser.cpython-313.pyc
│  │     │  │  │     ├─ _parseaddr.cpython-313.pyc
│  │     │  │  │     ├─ _policybase.cpython-313.pyc
│  │     │  │  │     └─ __init__.cpython-313.pyc
│  │     │  │  ├─ html
│  │     │  │  │  ├─ entities.py
│  │     │  │  │  ├─ parser.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ entities.cpython-313.pyc
│  │     │  │  │     ├─ parser.cpython-313.pyc
│  │     │  │  │     └─ __init__.cpython-313.pyc
│  │     │  │  ├─ http
│  │     │  │  │  ├─ client.py
│  │     │  │  │  ├─ cookiejar.py
│  │     │  │  │  ├─ cookies.py
│  │     │  │  │  ├─ server.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ client.cpython-313.pyc
│  │     │  │  │     ├─ cookiejar.cpython-313.pyc
│  │     │  │  │     ├─ cookies.cpython-313.pyc
│  │     │  │  │     ├─ server.cpython-313.pyc
│  │     │  │  │     └─ __init__.cpython-313.pyc
│  │     │  │  ├─ misc.py
│  │     │  │  ├─ socket.py
│  │     │  │  ├─ socketserver.py
│  │     │  │  ├─ test
│  │     │  │  │  ├─ badcert.pem
│  │     │  │  │  ├─ badkey.pem
│  │     │  │  │  ├─ dh512.pem
│  │     │  │  │  ├─ https_svn_python_org_root.pem
│  │     │  │  │  ├─ keycert.passwd.pem
│  │     │  │  │  ├─ keycert.pem
│  │     │  │  │  ├─ keycert2.pem
│  │     │  │  │  ├─ nokia.pem
│  │     │  │  │  ├─ nullbytecert.pem
│  │     │  │  │  ├─ nullcert.pem
│  │     │  │  │  ├─ pystone.py
│  │     │  │  │  ├─ sha256.pem
│  │     │  │  │  ├─ ssl_cert.pem
│  │     │  │  │  ├─ ssl_key.passwd.pem
│  │     │  │  │  ├─ ssl_key.pem
│  │     │  │  │  ├─ ssl_servers.py
│  │     │  │  │  ├─ support.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ pystone.cpython-313.pyc
│  │     │  │  │     ├─ ssl_servers.cpython-313.pyc
│  │     │  │  │     ├─ support.cpython-313.pyc
│  │     │  │  │     └─ __init__.cpython-313.pyc
│  │     │  │  ├─ total_ordering.py
│  │     │  │  ├─ urllib
│  │     │  │  │  ├─ error.py
│  │     │  │  │  ├─ parse.py
│  │     │  │  │  ├─ request.py
│  │     │  │  │  ├─ response.py
│  │     │  │  │  ├─ robotparser.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ error.cpython-313.pyc
│  │     │  │  │     ├─ parse.cpython-313.pyc
│  │     │  │  │     ├─ request.cpython-313.pyc
│  │     │  │  │     ├─ response.cpython-313.pyc
│  │     │  │  │     ├─ robotparser.cpython-313.pyc
│  │     │  │  │     └─ __init__.cpython-313.pyc
│  │     │  │  ├─ xmlrpc
│  │     │  │  │  ├─ client.py
│  │     │  │  │  ├─ server.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ client.cpython-313.pyc
│  │     │  │  │     ├─ server.cpython-313.pyc
│  │     │  │  │     └─ __init__.cpython-313.pyc
│  │     │  │  ├─ _markupbase.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ datetime.cpython-313.pyc
│  │     │  │     ├─ misc.cpython-313.pyc
│  │     │  │     ├─ socket.cpython-313.pyc
│  │     │  │     ├─ socketserver.cpython-313.pyc
│  │     │  │     ├─ total_ordering.cpython-313.pyc
│  │     │  │     ├─ _markupbase.cpython-313.pyc
│  │     │  │     └─ __init__.cpython-313.pyc
│  │     │  ├─ builtins
│  │     │  │  ├─ disabled.py
│  │     │  │  ├─ iterators.py
│  │     │  │  ├─ misc.py
│  │     │  │  ├─ newnext.py
│  │     │  │  ├─ newround.py
│  │     │  │  ├─ newsuper.py
│  │     │  │  ├─ new_min_max.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ disabled.cpython-313.pyc
│  │     │  │     ├─ iterators.cpython-313.pyc
│  │     │  │     ├─ misc.cpython-313.pyc
│  │     │  │     ├─ newnext.cpython-313.pyc
│  │     │  │     ├─ newround.cpython-313.pyc
│  │     │  │     ├─ newsuper.cpython-313.pyc
│  │     │  │     ├─ new_min_max.cpython-313.pyc
│  │     │  │     └─ __init__.cpython-313.pyc
│  │     │  ├─ moves
│  │     │  │  ├─ builtins.py
│  │     │  │  ├─ collections.py
│  │     │  │  ├─ configparser.py
│  │     │  │  ├─ copyreg.py
│  │     │  │  ├─ dbm
│  │     │  │  │  ├─ dumb.py
│  │     │  │  │  ├─ gnu.py
│  │     │  │  │  ├─ ndbm.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ dumb.cpython-313.pyc
│  │     │  │  │     ├─ gnu.cpython-313.pyc
│  │     │  │  │     ├─ ndbm.cpython-313.pyc
│  │     │  │  │     └─ __init__.cpython-313.pyc
│  │     │  │  ├─ html
│  │     │  │  │  ├─ entities.py
│  │     │  │  │  ├─ parser.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ entities.cpython-313.pyc
│  │     │  │  │     ├─ parser.cpython-313.pyc
│  │     │  │  │     └─ __init__.cpython-313.pyc
│  │     │  │  ├─ http
│  │     │  │  │  ├─ client.py
│  │     │  │  │  ├─ cookiejar.py
│  │     │  │  │  ├─ cookies.py
│  │     │  │  │  ├─ server.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ client.cpython-313.pyc
│  │     │  │  │     ├─ cookiejar.cpython-313.pyc
│  │     │  │  │     ├─ cookies.cpython-313.pyc
│  │     │  │  │     ├─ server.cpython-313.pyc
│  │     │  │  │     └─ __init__.cpython-313.pyc
│  │     │  │  ├─ itertools.py
│  │     │  │  ├─ multiprocessing.py
│  │     │  │  ├─ pickle.py
│  │     │  │  ├─ queue.py
│  │     │  │  ├─ reprlib.py
│  │     │  │  ├─ socketserver.py
│  │     │  │  ├─ subprocess.py
│  │     │  │  ├─ sys.py
│  │     │  │  ├─ test
│  │     │  │  │  ├─ support.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ support.cpython-313.pyc
│  │     │  │  │     └─ __init__.cpython-313.pyc
│  │     │  │  ├─ tkinter
│  │     │  │  │  ├─ colorchooser.py
│  │     │  │  │  ├─ commondialog.py
│  │     │  │  │  ├─ constants.py
│  │     │  │  │  ├─ dialog.py
│  │     │  │  │  ├─ dnd.py
│  │     │  │  │  ├─ filedialog.py
│  │     │  │  │  ├─ font.py
│  │     │  │  │  ├─ messagebox.py
│  │     │  │  │  ├─ scrolledtext.py
│  │     │  │  │  ├─ simpledialog.py
│  │     │  │  │  ├─ tix.py
│  │     │  │  │  ├─ ttk.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ colorchooser.cpython-313.pyc
│  │     │  │  │     ├─ commondialog.cpython-313.pyc
│  │     │  │  │     ├─ constants.cpython-313.pyc
│  │     │  │  │     ├─ dialog.cpython-313.pyc
│  │     │  │  │     ├─ dnd.cpython-313.pyc
│  │     │  │  │     ├─ filedialog.cpython-313.pyc
│  │     │  │  │     ├─ font.cpython-313.pyc
│  │     │  │  │     ├─ messagebox.cpython-313.pyc
│  │     │  │  │     ├─ scrolledtext.cpython-313.pyc
│  │     │  │  │     ├─ simpledialog.cpython-313.pyc
│  │     │  │  │     ├─ tix.cpython-313.pyc
│  │     │  │  │     ├─ ttk.cpython-313.pyc
│  │     │  │  │     └─ __init__.cpython-313.pyc
│  │     │  │  ├─ urllib
│  │     │  │  │  ├─ error.py
│  │     │  │  │  ├─ parse.py
│  │     │  │  │  ├─ request.py
│  │     │  │  │  ├─ response.py
│  │     │  │  │  ├─ robotparser.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ error.cpython-313.pyc
│  │     │  │  │     ├─ parse.cpython-313.pyc
│  │     │  │  │     ├─ request.cpython-313.pyc
│  │     │  │  │     ├─ response.cpython-313.pyc
│  │     │  │  │     ├─ robotparser.cpython-313.pyc
│  │     │  │  │     └─ __init__.cpython-313.pyc
│  │     │  │  ├─ winreg.py
│  │     │  │  ├─ xmlrpc
│  │     │  │  │  ├─ client.py
│  │     │  │  │  ├─ server.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ client.cpython-313.pyc
│  │     │  │  │     ├─ server.cpython-313.pyc
│  │     │  │  │     └─ __init__.cpython-313.pyc
│  │     │  │  ├─ _dummy_thread.py
│  │     │  │  ├─ _markupbase.py
│  │     │  │  ├─ _thread.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ builtins.cpython-313.pyc
│  │     │  │     ├─ collections.cpython-313.pyc
│  │     │  │     ├─ configparser.cpython-313.pyc
│  │     │  │     ├─ copyreg.cpython-313.pyc
│  │     │  │     ├─ itertools.cpython-313.pyc
│  │     │  │     ├─ multiprocessing.cpython-313.pyc
│  │     │  │     ├─ pickle.cpython-313.pyc
│  │     │  │     ├─ queue.cpython-313.pyc
│  │     │  │     ├─ reprlib.cpython-313.pyc
│  │     │  │     ├─ socketserver.cpython-313.pyc
│  │     │  │     ├─ subprocess.cpython-313.pyc
│  │     │  │     ├─ sys.cpython-313.pyc
│  │     │  │     ├─ winreg.cpython-313.pyc
│  │     │  │     ├─ _dummy_thread.cpython-313.pyc
│  │     │  │     ├─ _markupbase.cpython-313.pyc
│  │     │  │     ├─ _thread.cpython-313.pyc
│  │     │  │     └─ __init__.cpython-313.pyc
│  │     │  ├─ standard_library
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     └─ __init__.cpython-313.pyc
│  │     │  ├─ tests
│  │     │  │  ├─ base.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ base.cpython-313.pyc
│  │     │  │     └─ __init__.cpython-313.pyc
│  │     │  ├─ types
│  │     │  │  ├─ newbytes.py
│  │     │  │  ├─ newdict.py
│  │     │  │  ├─ newint.py
│  │     │  │  ├─ newlist.py
│  │     │  │  ├─ newmemoryview.py
│  │     │  │  ├─ newobject.py
│  │     │  │  ├─ newopen.py
│  │     │  │  ├─ newrange.py
│  │     │  │  ├─ newstr.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ newbytes.cpython-313.pyc
│  │     │  │     ├─ newdict.cpython-313.pyc
│  │     │  │     ├─ newint.cpython-313.pyc
│  │     │  │     ├─ newlist.cpython-313.pyc
│  │     │  │     ├─ newmemoryview.cpython-313.pyc
│  │     │  │     ├─ newobject.cpython-313.pyc
│  │     │  │     ├─ newopen.cpython-313.pyc
│  │     │  │     ├─ newrange.cpython-313.pyc
│  │     │  │     ├─ newstr.cpython-313.pyc
│  │     │  │     └─ __init__.cpython-313.pyc
│  │     │  ├─ utils
│  │     │  │  ├─ surrogateescape.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ surrogateescape.cpython-313.pyc
│  │     │  │     └─ __init__.cpython-313.pyc
│  │     │  ├─ __init__.py
│  │     │  └─ __pycache__
│  │     │     └─ __init__.cpython-313.pyc
│  │     ├─ future-1.0.0.dist-info
│  │     │  ├─ entry_points.txt
│  │     │  ├─ INSTALLER
│  │     │  ├─ LICENSE.txt
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  ├─ top_level.txt
│  │     │  └─ WHEEL
│  │     ├─ google
│  │     │  ├─ auth
│  │     │  │  ├─ aio
│  │     │  │  │  ├─ credentials.py
│  │     │  │  │  ├─ transport
│  │     │  │  │  │  ├─ aiohttp.py
│  │     │  │  │  │  ├─ mtls.py
│  │     │  │  │  │  ├─ sessions.py
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  └─ __pycache__
│  │     │  │  │  │     ├─ aiohttp.cpython-313.pyc
│  │     │  │  │  │     ├─ mtls.cpython-313.pyc
│  │     │  │  │  │     ├─ sessions.cpython-313.pyc
│  │     │  │  │  │     └─ __init__.cpython-313.pyc
│  │     │  │  │  ├─ _helpers.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ credentials.cpython-313.pyc
│  │     │  │  │     ├─ _helpers.cpython-313.pyc
│  │     │  │  │     └─ __init__.cpython-313.pyc
│  │     │  │  ├─ api_key.py
│  │     │  │  ├─ app_engine.py
│  │     │  │  ├─ aws.py
│  │     │  │  ├─ compute_engine
│  │     │  │  │  ├─ credentials.py
│  │     │  │  │  ├─ _metadata.py
│  │     │  │  │  ├─ _mtls.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ credentials.cpython-313.pyc
│  │     │  │  │     ├─ _metadata.cpython-313.pyc
│  │     │  │  │     ├─ _mtls.cpython-313.pyc
│  │     │  │  │     └─ __init__.cpython-313.pyc
│  │     │  │  ├─ credentials.py
│  │     │  │  ├─ crypt
│  │     │  │  │  ├─ base.py
│  │     │  │  │  ├─ es.py
│  │     │  │  │  ├─ es256.py
│  │     │  │  │  ├─ rsa.py
│  │     │  │  │  ├─ _cryptography_rsa.py
│  │     │  │  │  ├─ _helpers.py
│  │     │  │  │  ├─ _python_rsa.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ base.cpython-313.pyc
│  │     │  │  │     ├─ es.cpython-313.pyc
│  │     │  │  │     ├─ es256.cpython-313.pyc
│  │     │  │  │     ├─ rsa.cpython-313.pyc
│  │     │  │  │     ├─ _cryptography_rsa.cpython-313.pyc
│  │     │  │  │     ├─ _helpers.cpython-313.pyc
│  │     │  │  │     ├─ _python_rsa.cpython-313.pyc
│  │     │  │  │     └─ __init__.cpython-313.pyc
│  │     │  │  ├─ downscoped.py
│  │     │  │  ├─ environment_vars.py
│  │     │  │  ├─ exceptions.py
│  │     │  │  ├─ external_account.py
│  │     │  │  ├─ external_account_authorized_user.py
│  │     │  │  ├─ iam.py
│  │     │  │  ├─ identity_pool.py
│  │     │  │  ├─ impersonated_credentials.py
│  │     │  │  ├─ jwt.py
│  │     │  │  ├─ metrics.py
│  │     │  │  ├─ pluggable.py
│  │     │  │  ├─ py.typed
│  │     │  │  ├─ transport
│  │     │  │  │  ├─ grpc.py
│  │     │  │  │  ├─ mtls.py
│  │     │  │  │  ├─ requests.py
│  │     │  │  │  ├─ urllib3.py
│  │     │  │  │  ├─ _aiohttp_requests.py
│  │     │  │  │  ├─ _custom_tls_signer.py
│  │     │  │  │  ├─ _http_client.py
│  │     │  │  │  ├─ _mtls_helper.py
│  │     │  │  │  ├─ _requests_base.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ grpc.cpython-313.pyc
│  │     │  │  │     ├─ mtls.cpython-313.pyc
│  │     │  │  │     ├─ requests.cpython-313.pyc
│  │     │  │  │     ├─ urllib3.cpython-313.pyc
│  │     │  │  │     ├─ _aiohttp_requests.cpython-313.pyc
│  │     │  │  │     ├─ _custom_tls_signer.cpython-313.pyc
│  │     │  │  │     ├─ _http_client.cpython-313.pyc
│  │     │  │  │     ├─ _mtls_helper.cpython-313.pyc
│  │     │  │  │     ├─ _requests_base.cpython-313.pyc
│  │     │  │  │     └─ __init__.cpython-313.pyc
│  │     │  │  ├─ version.py
│  │     │  │  ├─ _agent_identity_utils.py
│  │     │  │  ├─ _cache.py
│  │     │  │  ├─ _cloud_sdk.py
│  │     │  │  ├─ _constants.py
│  │     │  │  ├─ _credentials_async.py
│  │     │  │  ├─ _credentials_base.py
│  │     │  │  ├─ _default.py
│  │     │  │  ├─ _default_async.py
│  │     │  │  ├─ _exponential_backoff.py
│  │     │  │  ├─ _helpers.py
│  │     │  │  ├─ _jwt_async.py
│  │     │  │  ├─ _oauth2client.py
│  │     │  │  ├─ _refresh_worker.py
│  │     │  │  ├─ _service_account_info.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ api_key.cpython-313.pyc
│  │     │  │     ├─ app_engine.cpython-313.pyc
│  │     │  │     ├─ aws.cpython-313.pyc
│  │     │  │     ├─ credentials.cpython-313.pyc
│  │     │  │     ├─ downscoped.cpython-313.pyc
│  │     │  │     ├─ environment_vars.cpython-313.pyc
│  │     │  │     ├─ exceptions.cpython-313.pyc
│  │     │  │     ├─ external_account.cpython-313.pyc
│  │     │  │     ├─ external_account_authorized_user.cpython-313.pyc
│  │     │  │     ├─ iam.cpython-313.pyc
│  │     │  │     ├─ identity_pool.cpython-313.pyc
│  │     │  │     ├─ impersonated_credentials.cpython-313.pyc
│  │     │  │     ├─ jwt.cpython-313.pyc
│  │     │  │     ├─ metrics.cpython-313.pyc
│  │     │  │     ├─ pluggable.cpython-313.pyc
│  │     │  │     ├─ version.cpython-313.pyc
│  │     │  │     ├─ _agent_identity_utils.cpython-313.pyc
│  │     │  │     ├─ _cache.cpython-313.pyc
│  │     │  │     ├─ _cloud_sdk.cpython-313.pyc
│  │     │  │     ├─ _constants.cpython-313.pyc
│  │     │  │     ├─ _credentials_async.cpython-313.pyc
│  │     │  │     ├─ _credentials_base.cpython-313.pyc
│  │     │  │     ├─ _default.cpython-313.pyc
│  │     │  │     ├─ _default_async.cpython-313.pyc
│  │     │  │     ├─ _exponential_backoff.cpython-313.pyc
│  │     │  │     ├─ _helpers.cpython-313.pyc
│  │     │  │     ├─ _jwt_async.cpython-313.pyc
│  │     │  │     ├─ _oauth2client.cpython-313.pyc
│  │     │  │     ├─ _refresh_worker.cpython-313.pyc
│  │     │  │     ├─ _service_account_info.cpython-313.pyc
│  │     │  │     └─ __init__.cpython-313.pyc
│  │     │  ├─ genai
│  │     │  │  ├─ batches.py
│  │     │  │  ├─ caches.py
│  │     │  │  ├─ chats.py
│  │     │  │  ├─ client.py
│  │     │  │  ├─ errors.py
│  │     │  │  ├─ files.py
│  │     │  │  ├─ live.py
│  │     │  │  ├─ live_music.py
│  │     │  │  ├─ models.py
│  │     │  │  ├─ operations.py
│  │     │  │  ├─ pagers.py
│  │     │  │  ├─ py.typed
│  │     │  │  ├─ tokens.py
│  │     │  │  ├─ tunings.py
│  │     │  │  ├─ types.py
│  │     │  │  ├─ version.py
│  │     │  │  ├─ _adapters.py
│  │     │  │  ├─ _api_client.py
│  │     │  │  ├─ _api_module.py
│  │     │  │  ├─ _automatic_function_calling_util.py
│  │     │  │  ├─ _base_url.py
│  │     │  │  ├─ _common.py
│  │     │  │  ├─ _extra_utils.py
│  │     │  │  ├─ _live_converters.py
│  │     │  │  ├─ _mcp_utils.py
│  │     │  │  ├─ _replay_api_client.py
│  │     │  │  ├─ _test_api_client.py
│  │     │  │  ├─ _tokens_converters.py
│  │     │  │  ├─ _transformers.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ batches.cpython-313.pyc
│  │     │  │     ├─ caches.cpython-313.pyc
│  │     │  │     ├─ chats.cpython-313.pyc
│  │     │  │     ├─ client.cpython-313.pyc
│  │     │  │     ├─ errors.cpython-313.pyc
│  │     │  │     ├─ files.cpython-313.pyc
│  │     │  │     ├─ live.cpython-313.pyc
│  │     │  │     ├─ live_music.cpython-313.pyc
│  │     │  │     ├─ models.cpython-313.pyc
│  │     │  │     ├─ operations.cpython-313.pyc
│  │     │  │     ├─ pagers.cpython-313.pyc
│  │     │  │     ├─ tokens.cpython-313.pyc
│  │     │  │     ├─ tunings.cpython-313.pyc
│  │     │  │     ├─ types.cpython-313.pyc
│  │     │  │     ├─ version.cpython-313.pyc
│  │     │  │     ├─ _adapters.cpython-313.pyc
│  │     │  │     ├─ _api_client.cpython-313.pyc
│  │     │  │     ├─ _api_module.cpython-313.pyc
│  │     │  │     ├─ _automatic_function_calling_util.cpython-313.pyc
│  │     │  │     ├─ _base_url.cpython-313.pyc
│  │     │  │     ├─ _common.cpython-313.pyc
│  │     │  │     ├─ _extra_utils.cpython-313.pyc
│  │     │  │     ├─ _live_converters.cpython-313.pyc
│  │     │  │     ├─ _mcp_utils.cpython-313.pyc
│  │     │  │     ├─ _replay_api_client.cpython-313.pyc
│  │     │  │     ├─ _test_api_client.cpython-313.pyc
│  │     │  │     ├─ _tokens_converters.cpython-313.pyc
│  │     │  │     ├─ _transformers.cpython-313.pyc
│  │     │  │     └─ __init__.cpython-313.pyc
│  │     │  └─ oauth2
│  │     │     ├─ challenges.py
│  │     │     ├─ credentials.py
│  │     │     ├─ gdch_credentials.py
│  │     │     ├─ id_token.py
│  │     │     ├─ py.typed
│  │     │     ├─ reauth.py
│  │     │     ├─ service_account.py
│  │     │     ├─ sts.py
│  │     │     ├─ utils.py
│  │     │     ├─ webauthn_handler.py
│  │     │     ├─ webauthn_handler_factory.py
│  │     │     ├─ webauthn_types.py
│  │     │     ├─ _client.py
│  │     │     ├─ _client_async.py
│  │     │     ├─ _credentials_async.py
│  │     │     ├─ _id_token_async.py
│  │     │     ├─ _reauth_async.py
│  │     │     ├─ _service_account_async.py
│  │     │     ├─ __init__.py
│  │     │     └─ __pycache__
│  │     │        ├─ challenges.cpython-313.pyc
│  │     │        ├─ credentials.cpython-313.pyc
│  │     │        ├─ gdch_credentials.cpython-313.pyc
│  │     │        ├─ id_token.cpython-313.pyc
│  │     │        ├─ reauth.cpython-313.pyc
│  │     │        ├─ service_account.cpython-313.pyc
│  │     │        ├─ sts.cpython-313.pyc
│  │     │        ├─ utils.cpython-313.pyc
│  │     │        ├─ webauthn_handler.cpython-313.pyc
│  │     │        ├─ webauthn_handler_factory.cpython-313.pyc
│  │     │        ├─ webauthn_types.cpython-313.pyc
│  │     │        ├─ _client.cpython-313.pyc
│  │     │        ├─ _client_async.cpython-313.pyc
│  │     │        ├─ _credentials_async.cpython-313.pyc
│  │     │        ├─ _id_token_async.cpython-313.pyc
│  │     │        ├─ _reauth_async.cpython-313.pyc
│  │     │        ├─ _service_account_async.cpython-313.pyc
│  │     │        └─ __init__.cpython-313.pyc
│  │     ├─ google_auth-2.49.1.dist-info
│  │     │  ├─ INSTALLER
│  │     │  ├─ licenses
│  │     │  │  └─ LICENSE
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  ├─ top_level.txt
│  │     │  └─ WHEEL
│  │     ├─ google_genai-1.16.0.dist-info
│  │     │  ├─ INSTALLER
│  │     │  ├─ licenses
│  │     │  │  └─ LICENSE
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  ├─ REQUESTED
│  │     │  ├─ top_level.txt
│  │     │  └─ WHEEL
│  │     ├─ h11
│  │     │  ├─ py.typed
│  │     │  ├─ _abnf.py
│  │     │  ├─ _connection.py
│  │     │  ├─ _events.py
│  │     │  ├─ _headers.py
│  │     │  ├─ _readers.py
│  │     │  ├─ _receivebuffer.py
│  │     │  ├─ _state.py
│  │     │  ├─ _util.py
│  │     │  ├─ _version.py
│  │     │  ├─ _writers.py
│  │     │  ├─ __init__.py
│  │     │  └─ __pycache__
│  │     │     ├─ _abnf.cpython-313.pyc
│  │     │     ├─ _connection.cpython-313.pyc
│  │     │     ├─ _events.cpython-313.pyc
│  │     │     ├─ _headers.cpython-313.pyc
│  │     │     ├─ _readers.cpython-313.pyc
│  │     │     ├─ _receivebuffer.cpython-313.pyc
│  │     │     ├─ _state.cpython-313.pyc
│  │     │     ├─ _util.cpython-313.pyc
│  │     │     ├─ _version.cpython-313.pyc
│  │     │     ├─ _writers.cpython-313.pyc
│  │     │     └─ __init__.cpython-313.pyc
│  │     ├─ h11-0.16.0.dist-info
│  │     │  ├─ INSTALLER
│  │     │  ├─ licenses
│  │     │  │  └─ LICENSE.txt
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  ├─ top_level.txt
│  │     │  └─ WHEEL
│  │     ├─ httpcore
│  │     │  ├─ py.typed
│  │     │  ├─ _api.py
│  │     │  ├─ _async
│  │     │  │  ├─ connection.py
│  │     │  │  ├─ connection_pool.py
│  │     │  │  ├─ http11.py
│  │     │  │  ├─ http2.py
│  │     │  │  ├─ http_proxy.py
│  │     │  │  ├─ interfaces.py
│  │     │  │  ├─ socks_proxy.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ connection.cpython-313.pyc
│  │     │  │     ├─ connection_pool.cpython-313.pyc
│  │     │  │     ├─ http11.cpython-313.pyc
│  │     │  │     ├─ http2.cpython-313.pyc
│  │     │  │     ├─ http_proxy.cpython-313.pyc
│  │     │  │     ├─ interfaces.cpython-313.pyc
│  │     │  │     ├─ socks_proxy.cpython-313.pyc
│  │     │  │     └─ __init__.cpython-313.pyc
│  │     │  ├─ _backends
│  │     │  │  ├─ anyio.py
│  │     │  │  ├─ auto.py
│  │     │  │  ├─ base.py
│  │     │  │  ├─ mock.py
│  │     │  │  ├─ sync.py
│  │     │  │  ├─ trio.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ anyio.cpython-313.pyc
│  │     │  │     ├─ auto.cpython-313.pyc
│  │     │  │     ├─ base.cpython-313.pyc
│  │     │  │     ├─ mock.cpython-313.pyc
│  │     │  │     ├─ sync.cpython-313.pyc
│  │     │  │     ├─ trio.cpython-313.pyc
│  │     │  │     └─ __init__.cpython-313.pyc
│  │     │  ├─ _exceptions.py
│  │     │  ├─ _models.py
│  │     │  ├─ _ssl.py
│  │     │  ├─ _sync
│  │     │  │  ├─ connection.py
│  │     │  │  ├─ connection_pool.py
│  │     │  │  ├─ http11.py
│  │     │  │  ├─ http2.py
│  │     │  │  ├─ http_proxy.py
│  │     │  │  ├─ interfaces.py
│  │     │  │  ├─ socks_proxy.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ connection.cpython-313.pyc
│  │     │  │     ├─ connection_pool.cpython-313.pyc
│  │     │  │     ├─ http11.cpython-313.pyc
│  │     │  │     ├─ http2.cpython-313.pyc
│  │     │  │     ├─ http_proxy.cpython-313.pyc
│  │     │  │     ├─ interfaces.cpython-313.pyc
│  │     │  │     ├─ socks_proxy.cpython-313.pyc
│  │     │  │     └─ __init__.cpython-313.pyc
│  │     │  ├─ _synchronization.py
│  │     │  ├─ _trace.py
│  │     │  ├─ _utils.py
│  │     │  ├─ __init__.py
│  │     │  └─ __pycache__
│  │     │     ├─ _api.cpython-313.pyc
│  │     │     ├─ _exceptions.cpython-313.pyc
│  │     │     ├─ _models.cpython-313.pyc
│  │     │     ├─ _ssl.cpython-313.pyc
│  │     │     ├─ _synchronization.cpython-313.pyc
│  │     │     ├─ _trace.cpython-313.pyc
│  │     │     ├─ _utils.cpython-313.pyc
│  │     │     └─ __init__.cpython-313.pyc
│  │     ├─ httpcore-1.0.9.dist-info
│  │     │  ├─ INSTALLER
│  │     │  ├─ licenses
│  │     │  │  └─ LICENSE.md
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  └─ WHEEL
│  │     ├─ httpx
│  │     │  ├─ py.typed
│  │     │  ├─ _api.py
│  │     │  ├─ _auth.py
│  │     │  ├─ _client.py
│  │     │  ├─ _config.py
│  │     │  ├─ _content.py
│  │     │  ├─ _decoders.py
│  │     │  ├─ _exceptions.py
│  │     │  ├─ _main.py
│  │     │  ├─ _models.py
│  │     │  ├─ _multipart.py
│  │     │  ├─ _status_codes.py
│  │     │  ├─ _transports
│  │     │  │  ├─ asgi.py
│  │     │  │  ├─ base.py
│  │     │  │  ├─ default.py
│  │     │  │  ├─ mock.py
│  │     │  │  ├─ wsgi.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ asgi.cpython-313.pyc
│  │     │  │     ├─ base.cpython-313.pyc
│  │     │  │     ├─ default.cpython-313.pyc
│  │     │  │     ├─ mock.cpython-313.pyc
│  │     │  │     ├─ wsgi.cpython-313.pyc
│  │     │  │     └─ __init__.cpython-313.pyc
│  │     │  ├─ _types.py
│  │     │  ├─ _urlparse.py
│  │     │  ├─ _urls.py
│  │     │  ├─ _utils.py
│  │     │  ├─ __init__.py
│  │     │  ├─ __pycache__
│  │     │  │  ├─ _api.cpython-313.pyc
│  │     │  │  ├─ _auth.cpython-313.pyc
│  │     │  │  ├─ _client.cpython-313.pyc
│  │     │  │  ├─ _config.cpython-313.pyc
│  │     │  │  ├─ _content.cpython-313.pyc
│  │     │  │  ├─ _decoders.cpython-313.pyc
│  │     │  │  ├─ _exceptions.cpython-313.pyc
│  │     │  │  ├─ _main.cpython-313.pyc
│  │     │  │  ├─ _models.cpython-313.pyc
│  │     │  │  ├─ _multipart.cpython-313.pyc
│  │     │  │  ├─ _status_codes.cpython-313.pyc
│  │     │  │  ├─ _types.cpython-313.pyc
│  │     │  │  ├─ _urlparse.cpython-313.pyc
│  │     │  │  ├─ _urls.cpython-313.pyc
│  │     │  │  ├─ _utils.cpython-313.pyc
│  │     │  │  ├─ __init__.cpython-313.pyc
│  │     │  │  └─ __version__.cpython-313.pyc
│  │     │  └─ __version__.py
│  │     ├─ httpx-0.28.1.dist-info
│  │     │  ├─ entry_points.txt
│  │     │  ├─ INSTALLER
│  │     │  ├─ licenses
│  │     │  │  └─ LICENSE.md
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  └─ WHEEL
│  │     ├─ idna
│  │     │  ├─ codec.py
│  │     │  ├─ compat.py
│  │     │  ├─ core.py
│  │     │  ├─ idnadata.py
│  │     │  ├─ intranges.py
│  │     │  ├─ package_data.py
│  │     │  ├─ py.typed
│  │     │  ├─ uts46data.py
│  │     │  ├─ __init__.py
│  │     │  └─ __pycache__
│  │     │     ├─ codec.cpython-313.pyc
│  │     │     ├─ compat.cpython-313.pyc
│  │     │     ├─ core.cpython-313.pyc
│  │     │     ├─ idnadata.cpython-313.pyc
│  │     │     ├─ intranges.cpython-313.pyc
│  │     │     ├─ package_data.cpython-313.pyc
│  │     │     ├─ uts46data.cpython-313.pyc
│  │     │     └─ __init__.cpython-313.pyc
│  │     ├─ idna-3.11.dist-info
│  │     │  ├─ INSTALLER
│  │     │  ├─ licenses
│  │     │  │  └─ LICENSE.md
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  └─ WHEEL
│  │     ├─ kiwisolver
│  │     │  ├─ exceptions.py
│  │     │  ├─ py.typed
│  │     │  ├─ _cext.cp313-win_amd64.pyd
│  │     │  ├─ _cext.pyi
│  │     │  ├─ __init__.py
│  │     │  └─ __pycache__
│  │     │     ├─ exceptions.cpython-313.pyc
│  │     │     └─ __init__.cpython-313.pyc
│  │     ├─ kiwisolver-1.5.0.dist-info
│  │     │  ├─ INSTALLER
│  │     │  ├─ licenses
│  │     │  │  └─ LICENSE
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  ├─ top_level.txt
│  │     │  └─ WHEEL
│  │     ├─ libfuturize
│  │     │  ├─ fixer_util.py
│  │     │  ├─ fixes
│  │     │  │  ├─ fix_absolute_import.py
│  │     │  │  ├─ fix_add__future__imports_except_unicode_literals.py
│  │     │  │  ├─ fix_basestring.py
│  │     │  │  ├─ fix_bytes.py
│  │     │  │  ├─ fix_cmp.py
│  │     │  │  ├─ fix_division.py
│  │     │  │  ├─ fix_division_safe.py
│  │     │  │  ├─ fix_execfile.py
│  │     │  │  ├─ fix_future_builtins.py
│  │     │  │  ├─ fix_future_standard_library.py
│  │     │  │  ├─ fix_future_standard_library_urllib.py
│  │     │  │  ├─ fix_input.py
│  │     │  │  ├─ fix_metaclass.py
│  │     │  │  ├─ fix_next_call.py
│  │     │  │  ├─ fix_object.py
│  │     │  │  ├─ fix_oldstr_wrap.py
│  │     │  │  ├─ fix_order___future__imports.py
│  │     │  │  ├─ fix_print.py
│  │     │  │  ├─ fix_print_with_import.py
│  │     │  │  ├─ fix_raise.py
│  │     │  │  ├─ fix_remove_old__future__imports.py
│  │     │  │  ├─ fix_unicode_keep_u.py
│  │     │  │  ├─ fix_unicode_literals_import.py
│  │     │  │  ├─ fix_UserDict.py
│  │     │  │  ├─ fix_xrange_with_import.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ fix_absolute_import.cpython-313.pyc
│  │     │  │     ├─ fix_add__future__imports_except_unicode_literals.cpython-313.pyc
│  │     │  │     ├─ fix_basestring.cpython-313.pyc
│  │     │  │     ├─ fix_bytes.cpython-313.pyc
│  │     │  │     ├─ fix_cmp.cpython-313.pyc
│  │     │  │     ├─ fix_division.cpython-313.pyc
│  │     │  │     ├─ fix_division_safe.cpython-313.pyc
│  │     │  │     ├─ fix_execfile.cpython-313.pyc
│  │     │  │     ├─ fix_future_builtins.cpython-313.pyc
│  │     │  │     ├─ fix_future_standard_library.cpython-313.pyc
│  │     │  │     ├─ fix_future_standard_library_urllib.cpython-313.pyc
│  │     │  │     ├─ fix_input.cpython-313.pyc
│  │     │  │     ├─ fix_metaclass.cpython-313.pyc
│  │     │  │     ├─ fix_next_call.cpython-313.pyc
│  │     │  │     ├─ fix_object.cpython-313.pyc
│  │     │  │     ├─ fix_oldstr_wrap.cpython-313.pyc
│  │     │  │     ├─ fix_order___future__imports.cpython-313.pyc
│  │     │  │     ├─ fix_print.cpython-313.pyc
│  │     │  │     ├─ fix_print_with_import.cpython-313.pyc
│  │     │  │     ├─ fix_raise.cpython-313.pyc
│  │     │  │     ├─ fix_remove_old__future__imports.cpython-313.pyc
│  │     │  │     ├─ fix_unicode_keep_u.cpython-313.pyc
│  │     │  │     ├─ fix_unicode_literals_import.cpython-313.pyc
│  │     │  │     ├─ fix_UserDict.cpython-313.pyc
│  │     │  │     ├─ fix_xrange_with_import.cpython-313.pyc
│  │     │  │     └─ __init__.cpython-313.pyc
│  │     │  ├─ main.py
│  │     │  ├─ __init__.py
│  │     │  └─ __pycache__
│  │     │     ├─ fixer_util.cpython-313.pyc
│  │     │     ├─ main.cpython-313.pyc
│  │     │     └─ __init__.cpython-313.pyc
│  │     ├─ libpasteurize
│  │     │  ├─ fixes
│  │     │  │  ├─ feature_base.py
│  │     │  │  ├─ fix_add_all_future_builtins.py
│  │     │  │  ├─ fix_add_all__future__imports.py
│  │     │  │  ├─ fix_add_future_standard_library_import.py
│  │     │  │  ├─ fix_annotations.py
│  │     │  │  ├─ fix_division.py
│  │     │  │  ├─ fix_features.py
│  │     │  │  ├─ fix_fullargspec.py
│  │     │  │  ├─ fix_future_builtins.py
│  │     │  │  ├─ fix_getcwd.py
│  │     │  │  ├─ fix_imports.py
│  │     │  │  ├─ fix_imports2.py
│  │     │  │  ├─ fix_kwargs.py
│  │     │  │  ├─ fix_memoryview.py
│  │     │  │  ├─ fix_metaclass.py
│  │     │  │  ├─ fix_newstyle.py
│  │     │  │  ├─ fix_next.py
│  │     │  │  ├─ fix_printfunction.py
│  │     │  │  ├─ fix_raise.py
│  │     │  │  ├─ fix_raise_.py
│  │     │  │  ├─ fix_throw.py
│  │     │  │  ├─ fix_unpacking.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ feature_base.cpython-313.pyc
│  │     │  │     ├─ fix_add_all_future_builtins.cpython-313.pyc
│  │     │  │     ├─ fix_add_all__future__imports.cpython-313.pyc
│  │     │  │     ├─ fix_add_future_standard_library_import.cpython-313.pyc
│  │     │  │     ├─ fix_annotations.cpython-313.pyc
│  │     │  │     ├─ fix_division.cpython-313.pyc
│  │     │  │     ├─ fix_features.cpython-313.pyc
│  │     │  │     ├─ fix_fullargspec.cpython-313.pyc
│  │     │  │     ├─ fix_future_builtins.cpython-313.pyc
│  │     │  │     ├─ fix_getcwd.cpython-313.pyc
│  │     │  │     ├─ fix_imports.cpython-313.pyc
│  │     │  │     ├─ fix_imports2.cpython-313.pyc
│  │     │  │     ├─ fix_kwargs.cpython-313.pyc
│  │     │  │     ├─ fix_memoryview.cpython-313.pyc
│  │     │  │     ├─ fix_metaclass.cpython-313.pyc
│  │     │  │     ├─ fix_newstyle.cpython-313.pyc
│  │     │  │     ├─ fix_next.cpython-313.pyc
│  │     │  │     ├─ fix_printfunction.cpython-313.pyc
│  │     │  │     ├─ fix_raise.cpython-313.pyc
│  │     │  │     ├─ fix_raise_.cpython-313.pyc
│  │     │  │     ├─ fix_throw.cpython-313.pyc
│  │     │  │     ├─ fix_unpacking.cpython-313.pyc
│  │     │  │     └─ __init__.cpython-313.pyc
│  │     │  ├─ main.py
│  │     │  ├─ __init__.py
│  │     │  └─ __pycache__
│  │     │     ├─ main.cpython-313.pyc
│  │     │     └─ __init__.cpython-313.pyc
│  │     ├─ matplotlib
│  │     │  ├─ animation.py
│  │     │  ├─ animation.pyi
│  │     │  ├─ artist.py
│  │     │  ├─ artist.pyi
│  │     │  ├─ axes
│  │     │  │  ├─ _axes.py
│  │     │  │  ├─ _axes.pyi
│  │     │  │  ├─ _base.py
│  │     │  │  ├─ _base.pyi
│  │     │  │  ├─ _secondary_axes.py
│  │     │  │  ├─ _secondary_axes.pyi
│  │     │  │  ├─ __init__.py
│  │     │  │  ├─ __init__.pyi
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ _axes.cpython-313.pyc
│  │     │  │     ├─ _base.cpython-313.pyc
│  │     │  │     ├─ _secondary_axes.cpython-313.pyc
│  │     │  │     └─ __init__.cpython-313.pyc
│  │     │  ├─ axis.py
│  │     │  ├─ axis.pyi
│  │     │  ├─ backends
│  │     │  │  ├─ backend_agg.py
│  │     │  │  ├─ backend_cairo.py
│  │     │  │  ├─ backend_gtk3.py
│  │     │  │  ├─ backend_gtk3agg.py
│  │     │  │  ├─ backend_gtk3cairo.py
│  │     │  │  ├─ backend_gtk4.py
│  │     │  │  ├─ backend_gtk4agg.py
│  │     │  │  ├─ backend_gtk4cairo.py
│  │     │  │  ├─ backend_macosx.py
│  │     │  │  ├─ backend_mixed.py
│  │     │  │  ├─ backend_nbagg.py
│  │     │  │  ├─ backend_pdf.py
│  │     │  │  ├─ backend_pgf.py
│  │     │  │  ├─ backend_ps.py
│  │     │  │  ├─ backend_qt.py
│  │     │  │  ├─ backend_qt5.py
│  │     │  │  ├─ backend_qt5agg.py
│  │     │  │  ├─ backend_qt5cairo.py
│  │     │  │  ├─ backend_qtagg.py
│  │     │  │  ├─ backend_qtcairo.py
│  │     │  │  ├─ backend_svg.py
│  │     │  │  ├─ backend_template.py
│  │     │  │  ├─ backend_tkagg.py
│  │     │  │  ├─ backend_tkcairo.py
│  │     │  │  ├─ backend_webagg.py
│  │     │  │  ├─ backend_webagg_core.py
│  │     │  │  ├─ backend_wx.py
│  │     │  │  ├─ backend_wxagg.py
│  │     │  │  ├─ backend_wxcairo.py
│  │     │  │  ├─ qt_compat.py
│  │     │  │  ├─ qt_editor
│  │     │  │  │  ├─ figureoptions.py
│  │     │  │  │  ├─ _formlayout.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ figureoptions.cpython-313.pyc
│  │     │  │  │     ├─ _formlayout.cpython-313.pyc
│  │     │  │  │     └─ __init__.cpython-313.pyc
│  │     │  │  ├─ registry.py
│  │     │  │  ├─ web_backend
│  │     │  │  │  ├─ all_figures.html
│  │     │  │  │  ├─ css
│  │     │  │  │  │  ├─ boilerplate.css
│  │     │  │  │  │  ├─ fbm.css
│  │     │  │  │  │  ├─ mpl.css
│  │     │  │  │  │  └─ page.css
│  │     │  │  │  ├─ ipython_inline_figure.html
│  │     │  │  │  ├─ js
│  │     │  │  │  │  ├─ mpl.js
│  │     │  │  │  │  ├─ mpl_tornado.js
│  │     │  │  │  │  └─ nbagg_mpl.js
│  │     │  │  │  └─ single_figure.html
│  │     │  │  ├─ _backend_agg.cp313-win_amd64.pyd
│  │     │  │  ├─ _backend_agg.pyi
│  │     │  │  ├─ _backend_gtk.py
│  │     │  │  ├─ _backend_pdf_ps.py
│  │     │  │  ├─ _backend_tk.py
│  │     │  │  ├─ _macosx.pyi
│  │     │  │  ├─ _tkagg.cp313-win_amd64.pyd
│  │     │  │  ├─ _tkagg.pyi
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ backend_agg.cpython-313.pyc
│  │     │  │     ├─ backend_cairo.cpython-313.pyc
│  │     │  │     ├─ backend_gtk3.cpython-313.pyc
│  │     │  │     ├─ backend_gtk3agg.cpython-313.pyc
│  │     │  │     ├─ backend_gtk3cairo.cpython-313.pyc
│  │     │  │     ├─ backend_gtk4.cpython-313.pyc
│  │     │  │     ├─ backend_gtk4agg.cpython-313.pyc
│  │     │  │     ├─ backend_gtk4cairo.cpython-313.pyc
│  │     │  │     ├─ backend_macosx.cpython-313.pyc
│  │     │  │     ├─ backend_mixed.cpython-313.pyc
│  │     │  │     ├─ backend_nbagg.cpython-313.pyc
│  │     │  │     ├─ backend_pdf.cpython-313.pyc
│  │     │  │     ├─ backend_pgf.cpython-313.pyc
│  │     │  │     ├─ backend_ps.cpython-313.pyc
│  │     │  │     ├─ backend_qt.cpython-313.pyc
│  │     │  │     ├─ backend_qt5.cpython-313.pyc
│  │     │  │     ├─ backend_qt5agg.cpython-313.pyc
│  │     │  │     ├─ backend_qt5cairo.cpython-313.pyc
│  │     │  │     ├─ backend_qtagg.cpython-313.pyc
│  │     │  │     ├─ backend_qtcairo.cpython-313.pyc
│  │     │  │     ├─ backend_svg.cpython-313.pyc
│  │     │  │     ├─ backend_template.cpython-313.pyc
│  │     │  │     ├─ backend_tkagg.cpython-313.pyc
│  │     │  │     ├─ backend_tkcairo.cpython-313.pyc
│  │     │  │     ├─ backend_webagg.cpython-313.pyc
│  │     │  │     ├─ backend_webagg_core.cpython-313.pyc
│  │     │  │     ├─ backend_wx.cpython-313.pyc
│  │     │  │     ├─ backend_wxagg.cpython-313.pyc
│  │     │  │     ├─ backend_wxcairo.cpython-313.pyc
│  │     │  │     ├─ qt_compat.cpython-313.pyc
│  │     │  │     ├─ registry.cpython-313.pyc
│  │     │  │     ├─ _backend_gtk.cpython-313.pyc
│  │     │  │     ├─ _backend_pdf_ps.cpython-313.pyc
│  │     │  │     ├─ _backend_tk.cpython-313.pyc
│  │     │  │     └─ __init__.cpython-313.pyc
│  │     │  ├─ backend_bases.py
│  │     │  ├─ backend_bases.pyi
│  │     │  ├─ backend_managers.py
│  │     │  ├─ backend_managers.pyi
│  │     │  ├─ backend_tools.py
│  │     │  ├─ backend_tools.pyi
│  │     │  ├─ bezier.py
│  │     │  ├─ bezier.pyi
│  │     │  ├─ category.py
│  │     │  ├─ cbook.py
│  │     │  ├─ cbook.pyi
│  │     │  ├─ cm.py
│  │     │  ├─ cm.pyi
│  │     │  ├─ collections.py
│  │     │  ├─ collections.pyi
│  │     │  ├─ colorbar.py
│  │     │  ├─ colorbar.pyi
│  │     │  ├─ colorizer.py
│  │     │  ├─ colorizer.pyi
│  │     │  ├─ colors.py
│  │     │  ├─ colors.pyi
│  │     │  ├─ container.py
│  │     │  ├─ container.pyi
│  │     │  ├─ contour.py
│  │     │  ├─ contour.pyi
│  │     │  ├─ dates.py
│  │     │  ├─ dviread.py
│  │     │  ├─ dviread.pyi
│  │     │  ├─ figure.py
│  │     │  ├─ figure.pyi
│  │     │  ├─ font_manager.py
│  │     │  ├─ font_manager.pyi
│  │     │  ├─ ft2font.cp313-win_amd64.pyd
│  │     │  ├─ ft2font.pyi
│  │     │  ├─ gridspec.py
│  │     │  ├─ gridspec.pyi
│  │     │  ├─ hatch.py
│  │     │  ├─ hatch.pyi
│  │     │  ├─ image.py
│  │     │  ├─ image.pyi
│  │     │  ├─ inset.py
│  │     │  ├─ inset.pyi
│  │     │  ├─ layout_engine.py
│  │     │  ├─ layout_engine.pyi
│  │     │  ├─ legend.py
│  │     │  ├─ legend.pyi
│  │     │  ├─ legend_handler.py
│  │     │  ├─ legend_handler.pyi
│  │     │  ├─ lines.py
│  │     │  ├─ lines.pyi
│  │     │  ├─ markers.py
│  │     │  ├─ markers.pyi
│  │     │  ├─ mathtext.py
│  │     │  ├─ mathtext.pyi
│  │     │  ├─ mlab.py
│  │     │  ├─ mlab.pyi
│  │     │  ├─ mpl-data
│  │     │  │  ├─ fonts
│  │     │  │  │  ├─ afm
│  │     │  │  │  │  ├─ cmex10.afm
│  │     │  │  │  │  ├─ cmmi10.afm
│  │     │  │  │  │  ├─ cmr10.afm
│  │     │  │  │  │  ├─ cmsy10.afm
│  │     │  │  │  │  ├─ cmtt10.afm
│  │     │  │  │  │  ├─ pagd8a.afm
│  │     │  │  │  │  ├─ pagdo8a.afm
│  │     │  │  │  │  ├─ pagk8a.afm
│  │     │  │  │  │  ├─ pagko8a.afm
│  │     │  │  │  │  ├─ pbkd8a.afm
│  │     │  │  │  │  ├─ pbkdi8a.afm
│  │     │  │  │  │  ├─ pbkl8a.afm
│  │     │  │  │  │  ├─ pbkli8a.afm
│  │     │  │  │  │  ├─ pcrb8a.afm
│  │     │  │  │  │  ├─ pcrbo8a.afm
│  │     │  │  │  │  ├─ pcrr8a.afm
│  │     │  │  │  │  ├─ pcrro8a.afm
│  │     │  │  │  │  ├─ phvb8a.afm
│  │     │  │  │  │  ├─ phvb8an.afm
│  │     │  │  │  │  ├─ phvbo8a.afm
│  │     │  │  │  │  ├─ phvbo8an.afm
│  │     │  │  │  │  ├─ phvl8a.afm
│  │     │  │  │  │  ├─ phvlo8a.afm
│  │     │  │  │  │  ├─ phvr8a.afm
│  │     │  │  │  │  ├─ phvr8an.afm
│  │     │  │  │  │  ├─ phvro8a.afm
│  │     │  │  │  │  ├─ phvro8an.afm
│  │     │  │  │  │  ├─ pncb8a.afm
│  │     │  │  │  │  ├─ pncbi8a.afm
│  │     │  │  │  │  ├─ pncr8a.afm
│  │     │  │  │  │  ├─ pncri8a.afm
│  │     │  │  │  │  ├─ pplb8a.afm
│  │     │  │  │  │  ├─ pplbi8a.afm
│  │     │  │  │  │  ├─ pplr8a.afm
│  │     │  │  │  │  ├─ pplri8a.afm
│  │     │  │  │  │  ├─ psyr.afm
│  │     │  │  │  │  ├─ ptmb8a.afm
│  │     │  │  │  │  ├─ ptmbi8a.afm
│  │     │  │  │  │  ├─ ptmr8a.afm
│  │     │  │  │  │  ├─ ptmri8a.afm
│  │     │  │  │  │  ├─ putb8a.afm
│  │     │  │  │  │  ├─ putbi8a.afm
│  │     │  │  │  │  ├─ putr8a.afm
│  │     │  │  │  │  ├─ putri8a.afm
│  │     │  │  │  │  ├─ pzcmi8a.afm
│  │     │  │  │  │  └─ pzdr.afm
│  │     │  │  │  ├─ pdfcorefonts
│  │     │  │  │  │  ├─ Courier-Bold.afm
│  │     │  │  │  │  ├─ Courier-BoldOblique.afm
│  │     │  │  │  │  ├─ Courier-Oblique.afm
│  │     │  │  │  │  ├─ Courier.afm
│  │     │  │  │  │  ├─ Helvetica-Bold.afm
│  │     │  │  │  │  ├─ Helvetica-BoldOblique.afm
│  │     │  │  │  │  ├─ Helvetica-Oblique.afm
│  │     │  │  │  │  ├─ Helvetica.afm
│  │     │  │  │  │  ├─ readme.txt
│  │     │  │  │  │  ├─ Symbol.afm
│  │     │  │  │  │  ├─ Times-Bold.afm
│  │     │  │  │  │  ├─ Times-BoldItalic.afm
│  │     │  │  │  │  ├─ Times-Italic.afm
│  │     │  │  │  │  ├─ Times-Roman.afm
│  │     │  │  │  │  └─ ZapfDingbats.afm
│  │     │  │  │  └─ ttf
│  │     │  │  │     ├─ cmb10.ttf
│  │     │  │  │     ├─ cmex10.ttf
│  │     │  │  │     ├─ cmmi10.ttf
│  │     │  │  │     ├─ cmr10.ttf
│  │     │  │  │     ├─ cmss10.ttf
│  │     │  │  │     ├─ cmsy10.ttf
│  │     │  │  │     ├─ cmtt10.ttf
│  │     │  │  │     ├─ DejaVuSans-Bold.ttf
│  │     │  │  │     ├─ DejaVuSans-BoldOblique.ttf
│  │     │  │  │     ├─ DejaVuSans-Oblique.ttf
│  │     │  │  │     ├─ DejaVuSans.ttf
│  │     │  │  │     ├─ DejaVuSansDisplay.ttf
│  │     │  │  │     ├─ DejaVuSansMono-Bold.ttf
│  │     │  │  │     ├─ DejaVuSansMono-BoldOblique.ttf
│  │     │  │  │     ├─ DejaVuSansMono-Oblique.ttf
│  │     │  │  │     ├─ DejaVuSansMono.ttf
│  │     │  │  │     ├─ DejaVuSerif-Bold.ttf
│  │     │  │  │     ├─ DejaVuSerif-BoldItalic.ttf
│  │     │  │  │     ├─ DejaVuSerif-Italic.ttf
│  │     │  │  │     ├─ DejaVuSerif.ttf
│  │     │  │  │     ├─ DejaVuSerifDisplay.ttf
│  │     │  │  │     ├─ LICENSE_DEJAVU
│  │     │  │  │     ├─ LICENSE_STIX
│  │     │  │  │     ├─ STIXGeneral.ttf
│  │     │  │  │     ├─ STIXGeneralBol.ttf
│  │     │  │  │     ├─ STIXGeneralBolIta.ttf
│  │     │  │  │     ├─ STIXGeneralItalic.ttf
│  │     │  │  │     ├─ STIXNonUni.ttf
│  │     │  │  │     ├─ STIXNonUniBol.ttf
│  │     │  │  │     ├─ STIXNonUniBolIta.ttf
│  │     │  │  │     ├─ STIXNonUniIta.ttf
│  │     │  │  │     ├─ STIXSizFiveSymReg.ttf
│  │     │  │  │     ├─ STIXSizFourSymBol.ttf
│  │     │  │  │     ├─ STIXSizFourSymReg.ttf
│  │     │  │  │     ├─ STIXSizOneSymBol.ttf
│  │     │  │  │     ├─ STIXSizOneSymReg.ttf
│  │     │  │  │     ├─ STIXSizThreeSymBol.ttf
│  │     │  │  │     ├─ STIXSizThreeSymReg.ttf
│  │     │  │  │     ├─ STIXSizTwoSymBol.ttf
│  │     │  │  │     └─ STIXSizTwoSymReg.ttf
│  │     │  │  ├─ images
│  │     │  │  │  ├─ back-symbolic.svg
│  │     │  │  │  ├─ back.pdf
│  │     │  │  │  ├─ back.png
│  │     │  │  │  ├─ back.svg
│  │     │  │  │  ├─ back_large.png
│  │     │  │  │  ├─ filesave-symbolic.svg
│  │     │  │  │  ├─ filesave.pdf
│  │     │  │  │  ├─ filesave.png
│  │     │  │  │  ├─ filesave.svg
│  │     │  │  │  ├─ filesave_large.png
│  │     │  │  │  ├─ forward-symbolic.svg
│  │     │  │  │  ├─ forward.pdf
│  │     │  │  │  ├─ forward.png
│  │     │  │  │  ├─ forward.svg
│  │     │  │  │  ├─ forward_large.png
│  │     │  │  │  ├─ hand.pdf
│  │     │  │  │  ├─ hand.png
│  │     │  │  │  ├─ hand.svg
│  │     │  │  │  ├─ help-symbolic.svg
│  │     │  │  │  ├─ help.pdf
│  │     │  │  │  ├─ help.png
│  │     │  │  │  ├─ help.svg
│  │     │  │  │  ├─ help_large.png
│  │     │  │  │  ├─ home-symbolic.svg
│  │     │  │  │  ├─ home.pdf
│  │     │  │  │  ├─ home.png
│  │     │  │  │  ├─ home.svg
│  │     │  │  │  ├─ home_large.png
│  │     │  │  │  ├─ matplotlib.pdf
│  │     │  │  │  ├─ matplotlib.png
│  │     │  │  │  ├─ matplotlib.svg
│  │     │  │  │  ├─ matplotlib_large.png
│  │     │  │  │  ├─ move-symbolic.svg
│  │     │  │  │  ├─ move.pdf
│  │     │  │  │  ├─ move.png
│  │     │  │  │  ├─ move.svg
│  │     │  │  │  ├─ move_large.png
│  │     │  │  │  ├─ qt4_editor_options.pdf
│  │     │  │  │  ├─ qt4_editor_options.png
│  │     │  │  │  ├─ qt4_editor_options.svg
│  │     │  │  │  ├─ qt4_editor_options_large.png
│  │     │  │  │  ├─ subplots-symbolic.svg
│  │     │  │  │  ├─ subplots.pdf
│  │     │  │  │  ├─ subplots.png
│  │     │  │  │  ├─ subplots.svg
│  │     │  │  │  ├─ subplots_large.png
│  │     │  │  │  ├─ zoom_to_rect-symbolic.svg
│  │     │  │  │  ├─ zoom_to_rect.pdf
│  │     │  │  │  ├─ zoom_to_rect.png
│  │     │  │  │  ├─ zoom_to_rect.svg
│  │     │  │  │  └─ zoom_to_rect_large.png
│  │     │  │  ├─ kpsewhich.lua
│  │     │  │  ├─ matplotlibrc
│  │     │  │  ├─ plot_directive
│  │     │  │  │  └─ plot_directive.css
│  │     │  │  ├─ sample_data
│  │     │  │  │  ├─ axes_grid
│  │     │  │  │  │  └─ bivariate_normal.npy
│  │     │  │  │  ├─ data_x_x2_x3.csv
│  │     │  │  │  ├─ eeg.dat
│  │     │  │  │  ├─ embedding_in_wx3.xrc
│  │     │  │  │  ├─ goog.npz
│  │     │  │  │  ├─ grace_hopper.jpg
│  │     │  │  │  ├─ jacksboro_fault_dem.npz
│  │     │  │  │  ├─ logo2.png
│  │     │  │  │  ├─ membrane.dat
│  │     │  │  │  ├─ Minduka_Present_Blue_Pack.png
│  │     │  │  │  ├─ msft.csv
│  │     │  │  │  ├─ README.txt
│  │     │  │  │  ├─ s1045.ima.gz
│  │     │  │  │  ├─ Stocks.csv
│  │     │  │  │  └─ topobathy.npz
│  │     │  │  └─ stylelib
│  │     │  │     ├─ bmh.mplstyle
│  │     │  │     ├─ classic.mplstyle
│  │     │  │     ├─ dark_background.mplstyle
│  │     │  │     ├─ fast.mplstyle
│  │     │  │     ├─ fivethirtyeight.mplstyle
│  │     │  │     ├─ ggplot.mplstyle
│  │     │  │     ├─ grayscale.mplstyle
│  │     │  │     ├─ petroff10.mplstyle
│  │     │  │     ├─ seaborn-v0_8-bright.mplstyle
│  │     │  │     ├─ seaborn-v0_8-colorblind.mplstyle
│  │     │  │     ├─ seaborn-v0_8-dark-palette.mplstyle
│  │     │  │     ├─ seaborn-v0_8-dark.mplstyle
│  │     │  │     ├─ seaborn-v0_8-darkgrid.mplstyle
│  │     │  │     ├─ seaborn-v0_8-deep.mplstyle
│  │     │  │     ├─ seaborn-v0_8-muted.mplstyle
│  │     │  │     ├─ seaborn-v0_8-notebook.mplstyle
│  │     │  │     ├─ seaborn-v0_8-paper.mplstyle
│  │     │  │     ├─ seaborn-v0_8-pastel.mplstyle
│  │     │  │     ├─ seaborn-v0_8-poster.mplstyle
│  │     │  │     ├─ seaborn-v0_8-talk.mplstyle
│  │     │  │     ├─ seaborn-v0_8-ticks.mplstyle
│  │     │  │     ├─ seaborn-v0_8-white.mplstyle
│  │     │  │     ├─ seaborn-v0_8-whitegrid.mplstyle
│  │     │  │     ├─ seaborn-v0_8.mplstyle
│  │     │  │     ├─ Solarize_Light2.mplstyle
│  │     │  │     ├─ tableau-colorblind10.mplstyle
│  │     │  │     ├─ _classic_test_patch.mplstyle
│  │     │  │     ├─ _mpl-gallery-nogrid.mplstyle
│  │     │  │     └─ _mpl-gallery.mplstyle
│  │     │  ├─ offsetbox.py
│  │     │  ├─ offsetbox.pyi
│  │     │  ├─ patches.py
│  │     │  ├─ patches.pyi
│  │     │  ├─ path.py
│  │     │  ├─ path.pyi
│  │     │  ├─ patheffects.py
│  │     │  ├─ patheffects.pyi
│  │     │  ├─ projections
│  │     │  │  ├─ geo.py
│  │     │  │  ├─ geo.pyi
│  │     │  │  ├─ polar.py
│  │     │  │  ├─ polar.pyi
│  │     │  │  ├─ __init__.py
│  │     │  │  ├─ __init__.pyi
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ geo.cpython-313.pyc
│  │     │  │     ├─ polar.cpython-313.pyc
│  │     │  │     └─ __init__.cpython-313.pyc
│  │     │  ├─ py.typed
│  │     │  ├─ pylab.py
│  │     │  ├─ pyplot.py
│  │     │  ├─ quiver.py
│  │     │  ├─ quiver.pyi
│  │     │  ├─ rcsetup.py
│  │     │  ├─ rcsetup.pyi
│  │     │  ├─ sankey.py
│  │     │  ├─ sankey.pyi
│  │     │  ├─ scale.py
│  │     │  ├─ scale.pyi
│  │     │  ├─ sphinxext
│  │     │  │  ├─ figmpl_directive.py
│  │     │  │  ├─ mathmpl.py
│  │     │  │  ├─ plot_directive.py
│  │     │  │  ├─ roles.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ figmpl_directive.cpython-313.pyc
│  │     │  │     ├─ mathmpl.cpython-313.pyc
│  │     │  │     ├─ plot_directive.cpython-313.pyc
│  │     │  │     ├─ roles.cpython-313.pyc
│  │     │  │     └─ __init__.cpython-313.pyc
│  │     │  ├─ spines.py
│  │     │  ├─ spines.pyi
│  │     │  ├─ stackplot.py
│  │     │  ├─ stackplot.pyi
│  │     │  ├─ streamplot.py
│  │     │  ├─ streamplot.pyi
│  │     │  ├─ style
│  │     │  │  ├─ core.py
│  │     │  │  ├─ core.pyi
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ core.cpython-313.pyc
│  │     │  │     └─ __init__.cpython-313.pyc
│  │     │  ├─ table.py
│  │     │  ├─ table.pyi
│  │     │  ├─ testing
│  │     │  │  ├─ compare.py
│  │     │  │  ├─ compare.pyi
│  │     │  │  ├─ conftest.py
│  │     │  │  ├─ conftest.pyi
│  │     │  │  ├─ decorators.py
│  │     │  │  ├─ decorators.pyi
│  │     │  │  ├─ exceptions.py
│  │     │  │  ├─ jpl_units
│  │     │  │  │  ├─ Duration.py
│  │     │  │  │  ├─ Epoch.py
│  │     │  │  │  ├─ EpochConverter.py
│  │     │  │  │  ├─ StrConverter.py
│  │     │  │  │  ├─ UnitDbl.py
│  │     │  │  │  ├─ UnitDblConverter.py
│  │     │  │  │  ├─ UnitDblFormatter.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ Duration.cpython-313.pyc
│  │     │  │  │     ├─ Epoch.cpython-313.pyc
│  │     │  │  │     ├─ EpochConverter.cpython-313.pyc
│  │     │  │  │     ├─ StrConverter.cpython-313.pyc
│  │     │  │  │     ├─ UnitDbl.cpython-313.pyc
│  │     │  │  │     ├─ UnitDblConverter.cpython-313.pyc
│  │     │  │  │     ├─ UnitDblFormatter.cpython-313.pyc
│  │     │  │  │     └─ __init__.cpython-313.pyc
│  │     │  │  ├─ widgets.py
│  │     │  │  ├─ widgets.pyi
│  │     │  │  ├─ _markers.py
│  │     │  │  ├─ __init__.py
│  │     │  │  ├─ __init__.pyi
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ compare.cpython-313.pyc
│  │     │  │     ├─ conftest.cpython-313.pyc
│  │     │  │     ├─ decorators.cpython-313.pyc
│  │     │  │     ├─ exceptions.cpython-313.pyc
│  │     │  │     ├─ widgets.cpython-313.pyc
│  │     │  │     ├─ _markers.cpython-313.pyc
│  │     │  │     └─ __init__.cpython-313.pyc
│  │     │  ├─ tests
│  │     │  │  ├─ conftest.py
│  │     │  │  ├─ test_afm.py
│  │     │  │  ├─ test_agg.py
│  │     │  │  ├─ test_agg_filter.py
│  │     │  │  ├─ test_animation.py
│  │     │  │  ├─ test_api.py
│  │     │  │  ├─ test_arrow_patches.py
│  │     │  │  ├─ test_artist.py
│  │     │  │  ├─ test_axes.py
│  │     │  │  ├─ test_axis.py
│  │     │  │  ├─ test_backends_interactive.py
│  │     │  │  ├─ test_backend_bases.py
│  │     │  │  ├─ test_backend_cairo.py
│  │     │  │  ├─ test_backend_gtk3.py
│  │     │  │  ├─ test_backend_inline.py
│  │     │  │  ├─ test_backend_macosx.py
│  │     │  │  ├─ test_backend_nbagg.py
│  │     │  │  ├─ test_backend_pdf.py
│  │     │  │  ├─ test_backend_pgf.py
│  │     │  │  ├─ test_backend_ps.py
│  │     │  │  ├─ test_backend_qt.py
│  │     │  │  ├─ test_backend_registry.py
│  │     │  │  ├─ test_backend_svg.py
│  │     │  │  ├─ test_backend_template.py
│  │     │  │  ├─ test_backend_tk.py
│  │     │  │  ├─ test_backend_tools.py
│  │     │  │  ├─ test_backend_webagg.py
│  │     │  │  ├─ test_basic.py
│  │     │  │  ├─ test_bbox_tight.py
│  │     │  │  ├─ test_bezier.py
│  │     │  │  ├─ test_category.py
│  │     │  │  ├─ test_cbook.py
│  │     │  │  ├─ test_collections.py
│  │     │  │  ├─ test_colorbar.py
│  │     │  │  ├─ test_colors.py
│  │     │  │  ├─ test_compare_images.py
│  │     │  │  ├─ test_constrainedlayout.py
│  │     │  │  ├─ test_container.py
│  │     │  │  ├─ test_contour.py
│  │     │  │  ├─ test_cycles.py
│  │     │  │  ├─ test_dates.py
│  │     │  │  ├─ test_datetime.py
│  │     │  │  ├─ test_determinism.py
│  │     │  │  ├─ test_doc.py
│  │     │  │  ├─ test_dviread.py
│  │     │  │  ├─ test_figure.py
│  │     │  │  ├─ test_fontconfig_pattern.py
│  │     │  │  ├─ test_font_manager.py
│  │     │  │  ├─ test_ft2font.py
│  │     │  │  ├─ test_getattr.py
│  │     │  │  ├─ test_gridspec.py
│  │     │  │  ├─ test_image.py
│  │     │  │  ├─ test_legend.py
│  │     │  │  ├─ test_lines.py
│  │     │  │  ├─ test_marker.py
│  │     │  │  ├─ test_mathtext.py
│  │     │  │  ├─ test_matplotlib.py
│  │     │  │  ├─ test_mlab.py
│  │     │  │  ├─ test_multivariate_colormaps.py
│  │     │  │  ├─ test_offsetbox.py
│  │     │  │  ├─ test_patches.py
│  │     │  │  ├─ test_path.py
│  │     │  │  ├─ test_patheffects.py
│  │     │  │  ├─ test_pickle.py
│  │     │  │  ├─ test_png.py
│  │     │  │  ├─ test_polar.py
│  │     │  │  ├─ test_preprocess_data.py
│  │     │  │  ├─ test_pyplot.py
│  │     │  │  ├─ test_quiver.py
│  │     │  │  ├─ test_rcparams.py
│  │     │  │  ├─ test_sankey.py
│  │     │  │  ├─ test_scale.py
│  │     │  │  ├─ test_simplification.py
│  │     │  │  ├─ test_skew.py
│  │     │  │  ├─ test_sphinxext.py
│  │     │  │  ├─ test_spines.py
│  │     │  │  ├─ test_streamplot.py
│  │     │  │  ├─ test_style.py
│  │     │  │  ├─ test_subplots.py
│  │     │  │  ├─ test_table.py
│  │     │  │  ├─ test_testing.py
│  │     │  │  ├─ test_texmanager.py
│  │     │  │  ├─ test_text.py
│  │     │  │  ├─ test_textpath.py
│  │     │  │  ├─ test_ticker.py
│  │     │  │  ├─ test_tightlayout.py
│  │     │  │  ├─ test_transforms.py
│  │     │  │  ├─ test_triangulation.py
│  │     │  │  ├─ test_type1font.py
│  │     │  │  ├─ test_units.py
│  │     │  │  ├─ test_usetex.py
│  │     │  │  ├─ test_widgets.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ conftest.cpython-313.pyc
│  │     │  │     ├─ test_afm.cpython-313.pyc
│  │     │  │     ├─ test_agg.cpython-313.pyc
│  │     │  │     ├─ test_agg_filter.cpython-313.pyc
│  │     │  │     ├─ test_animation.cpython-313.pyc
│  │     │  │     ├─ test_api.cpython-313.pyc
│  │     │  │     ├─ test_arrow_patches.cpython-313.pyc
│  │     │  │     ├─ test_artist.cpython-313.pyc
│  │     │  │     ├─ test_axes.cpython-313.pyc
│  │     │  │     ├─ test_axis.cpython-313.pyc
│  │     │  │     ├─ test_backends_interactive.cpython-313.pyc
│  │     │  │     ├─ test_backend_bases.cpython-313.pyc
│  │     │  │     ├─ test_backend_cairo.cpython-313.pyc
│  │     │  │     ├─ test_backend_gtk3.cpython-313.pyc
│  │     │  │     ├─ test_backend_inline.cpython-313.pyc
│  │     │  │     ├─ test_backend_macosx.cpython-313.pyc
│  │     │  │     ├─ test_backend_nbagg.cpython-313.pyc
│  │     │  │     ├─ test_backend_pdf.cpython-313.pyc
│  │     │  │     ├─ test_backend_pgf.cpython-313.pyc
│  │     │  │     ├─ test_backend_ps.cpython-313.pyc
│  │     │  │     ├─ test_backend_qt.cpython-313.pyc
│  │     │  │     ├─ test_backend_registry.cpython-313.pyc
│  │     │  │     ├─ test_backend_svg.cpython-313.pyc
│  │     │  │     ├─ test_backend_template.cpython-313.pyc
│  │     │  │     ├─ test_backend_tk.cpython-313.pyc
│  │     │  │     ├─ test_backend_tools.cpython-313.pyc
│  │     │  │     ├─ test_backend_webagg.cpython-313.pyc
│  │     │  │     ├─ test_basic.cpython-313.pyc
│  │     │  │     ├─ test_bbox_tight.cpython-313.pyc
│  │     │  │     ├─ test_bezier.cpython-313.pyc
│  │     │  │     ├─ test_category.cpython-313.pyc
│  │     │  │     ├─ test_cbook.cpython-313.pyc
│  │     │  │     ├─ test_collections.cpython-313.pyc
│  │     │  │     ├─ test_colorbar.cpython-313.pyc
│  │     │  │     ├─ test_colors.cpython-313.pyc
│  │     │  │     ├─ test_compare_images.cpython-313.pyc
│  │     │  │     ├─ test_constrainedlayout.cpython-313.pyc
│  │     │  │     ├─ test_container.cpython-313.pyc
│  │     │  │     ├─ test_contour.cpython-313.pyc
│  │     │  │     ├─ test_cycles.cpython-313.pyc
│  │     │  │     ├─ test_dates.cpython-313.pyc
│  │     │  │     ├─ test_datetime.cpython-313.pyc
│  │     │  │     ├─ test_determinism.cpython-313.pyc
│  │     │  │     ├─ test_doc.cpython-313.pyc
│  │     │  │     ├─ test_dviread.cpython-313.pyc
│  │     │  │     ├─ test_figure.cpython-313.pyc
│  │     │  │     ├─ test_fontconfig_pattern.cpython-313.pyc
│  │     │  │     ├─ test_font_manager.cpython-313.pyc
│  │     │  │     ├─ test_ft2font.cpython-313.pyc
│  │     │  │     ├─ test_getattr.cpython-313.pyc
│  │     │  │     ├─ test_gridspec.cpython-313.pyc
│  │     │  │     ├─ test_image.cpython-313.pyc
│  │     │  │     ├─ test_legend.cpython-313.pyc
│  │     │  │     ├─ test_lines.cpython-313.pyc
│  │     │  │     ├─ test_marker.cpython-313.pyc
│  │     │  │     ├─ test_mathtext.cpython-313.pyc
│  │     │  │     ├─ test_matplotlib.cpython-313.pyc
│  │     │  │     ├─ test_mlab.cpython-313.pyc
│  │     │  │     ├─ test_multivariate_colormaps.cpython-313.pyc
│  │     │  │     ├─ test_offsetbox.cpython-313.pyc
│  │     │  │     ├─ test_patches.cpython-313.pyc
│  │     │  │     ├─ test_path.cpython-313.pyc
│  │     │  │     ├─ test_patheffects.cpython-313.pyc
│  │     │  │     ├─ test_pickle.cpython-313.pyc
│  │     │  │     ├─ test_png.cpython-313.pyc
│  │     │  │     ├─ test_polar.cpython-313.pyc
│  │     │  │     ├─ test_preprocess_data.cpython-313.pyc
│  │     │  │     ├─ test_pyplot.cpython-313.pyc
│  │     │  │     ├─ test_quiver.cpython-313.pyc
│  │     │  │     ├─ test_rcparams.cpython-313.pyc
│  │     │  │     ├─ test_sankey.cpython-313.pyc
│  │     │  │     ├─ test_scale.cpython-313.pyc
│  │     │  │     ├─ test_simplification.cpython-313.pyc
│  │     │  │     ├─ test_skew.cpython-313.pyc
│  │     │  │     ├─ test_sphinxext.cpython-313.pyc
│  │     │  │     ├─ test_spines.cpython-313.pyc
│  │     │  │     ├─ test_streamplot.cpython-313.pyc
│  │     │  │     ├─ test_style.cpython-313.pyc
│  │     │  │     ├─ test_subplots.cpython-313.pyc
│  │     │  │     ├─ test_table.cpython-313.pyc
│  │     │  │     ├─ test_testing.cpython-313.pyc
│  │     │  │     ├─ test_texmanager.cpython-313.pyc
│  │     │  │     ├─ test_text.cpython-313.pyc
│  │     │  │     ├─ test_textpath.cpython-313.pyc
│  │     │  │     ├─ test_ticker.cpython-313.pyc
│  │     │  │     ├─ test_tightlayout.cpython-313.pyc
│  │     │  │     ├─ test_transforms.cpython-313.pyc
│  │     │  │     ├─ test_triangulation.cpython-313.pyc
│  │     │  │     ├─ test_type1font.cpython-313.pyc
│  │     │  │     ├─ test_units.cpython-313.pyc
│  │     │  │     ├─ test_usetex.cpython-313.pyc
│  │     │  │     ├─ test_widgets.cpython-313.pyc
│  │     │  │     └─ __init__.cpython-313.pyc
│  │     │  ├─ texmanager.py
│  │     │  ├─ texmanager.pyi
│  │     │  ├─ text.py
│  │     │  ├─ text.pyi
│  │     │  ├─ textpath.py
│  │     │  ├─ textpath.pyi
│  │     │  ├─ ticker.py
│  │     │  ├─ ticker.pyi
│  │     │  ├─ transforms.py
│  │     │  ├─ transforms.pyi
│  │     │  ├─ tri
│  │     │  │  ├─ _triangulation.py
│  │     │  │  ├─ _triangulation.pyi
│  │     │  │  ├─ _tricontour.py
│  │     │  │  ├─ _tricontour.pyi
│  │     │  │  ├─ _trifinder.py
│  │     │  │  ├─ _trifinder.pyi
│  │     │  │  ├─ _triinterpolate.py
│  │     │  │  ├─ _triinterpolate.pyi
│  │     │  │  ├─ _tripcolor.py
│  │     │  │  ├─ _tripcolor.pyi
│  │     │  │  ├─ _triplot.py
│  │     │  │  ├─ _triplot.pyi
│  │     │  │  ├─ _trirefine.py
│  │     │  │  ├─ _trirefine.pyi
│  │     │  │  ├─ _tritools.py
│  │     │  │  ├─ _tritools.pyi
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ _triangulation.cpython-313.pyc
│  │     │  │     ├─ _tricontour.cpython-313.pyc
│  │     │  │     ├─ _trifinder.cpython-313.pyc
│  │     │  │     ├─ _triinterpolate.cpython-313.pyc
│  │     │  │     ├─ _tripcolor.cpython-313.pyc
│  │     │  │     ├─ _triplot.cpython-313.pyc
│  │     │  │     ├─ _trirefine.cpython-313.pyc
│  │     │  │     ├─ _tritools.cpython-313.pyc
│  │     │  │     └─ __init__.cpython-313.pyc
│  │     │  ├─ typing.py
│  │     │  ├─ units.py
│  │     │  ├─ widgets.py
│  │     │  ├─ widgets.pyi
│  │     │  ├─ _afm.py
│  │     │  ├─ _animation_data.py
│  │     │  ├─ _api
│  │     │  │  ├─ deprecation.py
│  │     │  │  ├─ deprecation.pyi
│  │     │  │  ├─ __init__.py
│  │     │  │  ├─ __init__.pyi
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ deprecation.cpython-313.pyc
│  │     │  │     └─ __init__.cpython-313.pyc
│  │     │  ├─ _blocking_input.py
│  │     │  ├─ _cm.py
│  │     │  ├─ _cm_bivar.py
│  │     │  ├─ _cm_listed.py
│  │     │  ├─ _cm_multivar.py
│  │     │  ├─ _color_data.py
│  │     │  ├─ _color_data.pyi
│  │     │  ├─ _constrained_layout.py
│  │     │  ├─ _c_internal_utils.cp313-win_amd64.pyd
│  │     │  ├─ _c_internal_utils.pyi
│  │     │  ├─ _docstring.py
│  │     │  ├─ _docstring.pyi
│  │     │  ├─ _enums.py
│  │     │  ├─ _enums.pyi
│  │     │  ├─ _fontconfig_pattern.py
│  │     │  ├─ _image.cp313-win_amd64.pyd
│  │     │  ├─ _image.pyi
│  │     │  ├─ _internal_utils.py
│  │     │  ├─ _layoutgrid.py
│  │     │  ├─ _mathtext.py
│  │     │  ├─ _mathtext_data.py
│  │     │  ├─ _path.cp313-win_amd64.pyd
│  │     │  ├─ _path.pyi
│  │     │  ├─ _pylab_helpers.py
│  │     │  ├─ _pylab_helpers.pyi
│  │     │  ├─ _qhull.cp313-win_amd64.pyd
│  │     │  ├─ _qhull.pyi
│  │     │  ├─ _text_helpers.py
│  │     │  ├─ _tight_bbox.py
│  │     │  ├─ _tight_layout.py
│  │     │  ├─ _tri.cp313-win_amd64.pyd
│  │     │  ├─ _tri.pyi
│  │     │  ├─ _type1font.py
│  │     │  ├─ _version.py
│  │     │  ├─ __init__.py
│  │     │  ├─ __init__.pyi
│  │     │  └─ __pycache__
│  │     │     ├─ animation.cpython-313.pyc
│  │     │     ├─ artist.cpython-313.pyc
│  │     │     ├─ axis.cpython-313.pyc
│  │     │     ├─ backend_bases.cpython-313.pyc
│  │     │     ├─ backend_managers.cpython-313.pyc
│  │     │     ├─ backend_tools.cpython-313.pyc
│  │     │     ├─ bezier.cpython-313.pyc
│  │     │     ├─ category.cpython-313.pyc
│  │     │     ├─ cbook.cpython-313.pyc
│  │     │     ├─ cm.cpython-313.pyc
│  │     │     ├─ collections.cpython-313.pyc
│  │     │     ├─ colorbar.cpython-313.pyc
│  │     │     ├─ colorizer.cpython-313.pyc
│  │     │     ├─ colors.cpython-313.pyc
│  │     │     ├─ container.cpython-313.pyc
│  │     │     ├─ contour.cpython-313.pyc
│  │     │     ├─ dates.cpython-313.pyc
│  │     │     ├─ dviread.cpython-313.pyc
│  │     │     ├─ figure.cpython-313.pyc
│  │     │     ├─ font_manager.cpython-313.pyc
│  │     │     ├─ gridspec.cpython-313.pyc
│  │     │     ├─ hatch.cpython-313.pyc
│  │     │     ├─ image.cpython-313.pyc
│  │     │     ├─ inset.cpython-313.pyc
│  │     │     ├─ layout_engine.cpython-313.pyc
│  │     │     ├─ legend.cpython-313.pyc
│  │     │     ├─ legend_handler.cpython-313.pyc
│  │     │     ├─ lines.cpython-313.pyc
│  │     │     ├─ markers.cpython-313.pyc
│  │     │     ├─ mathtext.cpython-313.pyc
│  │     │     ├─ mlab.cpython-313.pyc
│  │     │     ├─ offsetbox.cpython-313.pyc
│  │     │     ├─ patches.cpython-313.pyc
│  │     │     ├─ path.cpython-313.pyc
│  │     │     ├─ patheffects.cpython-313.pyc
│  │     │     ├─ pylab.cpython-313.pyc
│  │     │     ├─ pyplot.cpython-313.pyc
│  │     │     ├─ quiver.cpython-313.pyc
│  │     │     ├─ rcsetup.cpython-313.pyc
│  │     │     ├─ sankey.cpython-313.pyc
│  │     │     ├─ scale.cpython-313.pyc
│  │     │     ├─ spines.cpython-313.pyc
│  │     │     ├─ stackplot.cpython-313.pyc
│  │     │     ├─ streamplot.cpython-313.pyc
│  │     │     ├─ table.cpython-313.pyc
│  │     │     ├─ texmanager.cpython-313.pyc
│  │     │     ├─ text.cpython-313.pyc
│  │     │     ├─ textpath.cpython-313.pyc
│  │     │     ├─ ticker.cpython-313.pyc
│  │     │     ├─ transforms.cpython-313.pyc
│  │     │     ├─ typing.cpython-313.pyc
│  │     │     ├─ units.cpython-313.pyc
│  │     │     ├─ widgets.cpython-313.pyc
│  │     │     ├─ _afm.cpython-313.pyc
│  │     │     ├─ _animation_data.cpython-313.pyc
│  │     │     ├─ _blocking_input.cpython-313.pyc
│  │     │     ├─ _cm.cpython-313.pyc
│  │     │     ├─ _cm_bivar.cpython-313.pyc
│  │     │     ├─ _cm_listed.cpython-313.pyc
│  │     │     ├─ _cm_multivar.cpython-313.pyc
│  │     │     ├─ _color_data.cpython-313.pyc
│  │     │     ├─ _constrained_layout.cpython-313.pyc
│  │     │     ├─ _docstring.cpython-313.pyc
│  │     │     ├─ _enums.cpython-313.pyc
│  │     │     ├─ _fontconfig_pattern.cpython-313.pyc
│  │     │     ├─ _internal_utils.cpython-313.pyc
│  │     │     ├─ _layoutgrid.cpython-313.pyc
│  │     │     ├─ _mathtext.cpython-313.pyc
│  │     │     ├─ _mathtext_data.cpython-313.pyc
│  │     │     ├─ _pylab_helpers.cpython-313.pyc
│  │     │     ├─ _text_helpers.cpython-313.pyc
│  │     │     ├─ _tight_bbox.cpython-313.pyc
│  │     │     ├─ _tight_layout.cpython-313.pyc
│  │     │     ├─ _type1font.cpython-313.pyc
│  │     │     ├─ _version.cpython-313.pyc
│  │     │     └─ __init__.cpython-313.pyc
│  │     ├─ matplotlib-3.10.8.dist-info
│  │     │  ├─ INSTALLER
│  │     │  ├─ LICENSE
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  └─ WHEEL
│  │     ├─ mediapipe
│  │     │  ├─ modules
│  │     │  │  ├─ hand_landmark
│  │     │  │  │  └─ handedness.txt
│  │     │  │  └─ objectron
│  │     │  │     └─ object_detection_oidv4_labelmap.txt
│  │     │  ├─ tasks
│  │     │  │  ├─ c
│  │     │  │  │  ├─ libmediapipe.dll
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     └─ __init__.cpython-313.pyc
│  │     │  │  ├─ metadata
│  │     │  │  │  ├─ image_segmenter_metadata_schema.fbs
│  │     │  │  │  ├─ image_segmenter_metadata_schema_py_generated.py
│  │     │  │  │  ├─ metadata_schema.fbs
│  │     │  │  │  ├─ metadata_schema_py_generated.py
│  │     │  │  │  ├─ object_detector_metadata_schema.fbs
│  │     │  │  │  ├─ object_detector_metadata_schema_py_generated.py
│  │     │  │  │  ├─ schema_py_generated.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ image_segmenter_metadata_schema_py_generated.cpython-313.pyc
│  │     │  │  │     ├─ metadata_schema_py_generated.cpython-313.pyc
│  │     │  │  │     ├─ object_detector_metadata_schema_py_generated.cpython-313.pyc
│  │     │  │  │     └─ schema_py_generated.cpython-313.pyc
│  │     │  │  ├─ python
│  │     │  │  │  ├─ audio
│  │     │  │  │  │  ├─ audio_classifier.py
│  │     │  │  │  │  ├─ core
│  │     │  │  │  │  │  ├─ audio_record.py
│  │     │  │  │  │  │  ├─ audio_task_running_mode.py
│  │     │  │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  │  └─ __pycache__
│  │     │  │  │  │  │     ├─ audio_record.cpython-313.pyc
│  │     │  │  │  │  │     ├─ audio_task_running_mode.cpython-313.pyc
│  │     │  │  │  │  │     └─ __init__.cpython-313.pyc
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  └─ __pycache__
│  │     │  │  │  │     ├─ audio_classifier.cpython-313.pyc
│  │     │  │  │  │     └─ __init__.cpython-313.pyc
│  │     │  │  │  ├─ benchmark
│  │     │  │  │  │  ├─ benchmark_utils.py
│  │     │  │  │  │  ├─ vision
│  │     │  │  │  │  │  ├─ benchmark.py
│  │     │  │  │  │  │  ├─ core
│  │     │  │  │  │  │  │  ├─ base_vision_benchmark_api.py
│  │     │  │  │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  │  │  └─ __pycache__
│  │     │  │  │  │  │  │     ├─ base_vision_benchmark_api.cpython-313.pyc
│  │     │  │  │  │  │  │     └─ __init__.cpython-313.pyc
│  │     │  │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  │  └─ __pycache__
│  │     │  │  │  │  │     ├─ benchmark.cpython-313.pyc
│  │     │  │  │  │  │     └─ __init__.cpython-313.pyc
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  └─ __pycache__
│  │     │  │  │  │     ├─ benchmark_utils.cpython-313.pyc
│  │     │  │  │  │     └─ __init__.cpython-313.pyc
│  │     │  │  │  ├─ components
│  │     │  │  │  │  ├─ containers
│  │     │  │  │  │  │  ├─ audio_data.py
│  │     │  │  │  │  │  ├─ audio_data_c.py
│  │     │  │  │  │  │  ├─ bounding_box.py
│  │     │  │  │  │  │  ├─ category.py
│  │     │  │  │  │  │  ├─ category_c.py
│  │     │  │  │  │  │  ├─ classification_result.py
│  │     │  │  │  │  │  ├─ classification_result_c.py
│  │     │  │  │  │  │  ├─ detections.py
│  │     │  │  │  │  │  ├─ detections_c.py
│  │     │  │  │  │  │  ├─ embedding_result.py
│  │     │  │  │  │  │  ├─ embedding_result_c.py
│  │     │  │  │  │  │  ├─ keypoint.py
│  │     │  │  │  │  │  ├─ keypoint_c.py
│  │     │  │  │  │  │  ├─ landmark.py
│  │     │  │  │  │  │  ├─ landmark_c.py
│  │     │  │  │  │  │  ├─ landmark_detection_result.py
│  │     │  │  │  │  │  ├─ matrix_c.py
│  │     │  │  │  │  │  ├─ rect.py
│  │     │  │  │  │  │  ├─ rect_c.py
│  │     │  │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  │  └─ __pycache__
│  │     │  │  │  │  │     ├─ audio_data.cpython-313.pyc
│  │     │  │  │  │  │     ├─ audio_data_c.cpython-313.pyc
│  │     │  │  │  │  │     ├─ bounding_box.cpython-313.pyc
│  │     │  │  │  │  │     ├─ category.cpython-313.pyc
│  │     │  │  │  │  │     ├─ category_c.cpython-313.pyc
│  │     │  │  │  │  │     ├─ classification_result.cpython-313.pyc
│  │     │  │  │  │  │     ├─ classification_result_c.cpython-313.pyc
│  │     │  │  │  │  │     ├─ detections.cpython-313.pyc
│  │     │  │  │  │  │     ├─ detections_c.cpython-313.pyc
│  │     │  │  │  │  │     ├─ embedding_result.cpython-313.pyc
│  │     │  │  │  │  │     ├─ embedding_result_c.cpython-313.pyc
│  │     │  │  │  │  │     ├─ keypoint.cpython-313.pyc
│  │     │  │  │  │  │     ├─ keypoint_c.cpython-313.pyc
│  │     │  │  │  │  │     ├─ landmark.cpython-313.pyc
│  │     │  │  │  │  │     ├─ landmark_c.cpython-313.pyc
│  │     │  │  │  │  │     ├─ landmark_detection_result.cpython-313.pyc
│  │     │  │  │  │  │     ├─ matrix_c.cpython-313.pyc
│  │     │  │  │  │  │     ├─ rect.cpython-313.pyc
│  │     │  │  │  │  │     ├─ rect_c.cpython-313.pyc
│  │     │  │  │  │  │     └─ __init__.cpython-313.pyc
│  │     │  │  │  │  ├─ processors
│  │     │  │  │  │  │  ├─ classifier_options.py
│  │     │  │  │  │  │  ├─ classifier_options_c.py
│  │     │  │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  │  └─ __pycache__
│  │     │  │  │  │  │     ├─ classifier_options.cpython-313.pyc
│  │     │  │  │  │  │     ├─ classifier_options_c.cpython-313.pyc
│  │     │  │  │  │  │     └─ __init__.cpython-313.pyc
│  │     │  │  │  │  ├─ utils
│  │     │  │  │  │  │  ├─ cosine_similarity.py
│  │     │  │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  │  └─ __pycache__
│  │     │  │  │  │  │     ├─ cosine_similarity.cpython-313.pyc
│  │     │  │  │  │  │     └─ __init__.cpython-313.pyc
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  └─ __pycache__
│  │     │  │  │  │     └─ __init__.cpython-313.pyc
│  │     │  │  │  ├─ core
│  │     │  │  │  │  ├─ async_result_dispatcher.py
│  │     │  │  │  │  ├─ base_options.py
│  │     │  │  │  │  ├─ base_options_c.py
│  │     │  │  │  │  ├─ mediapipe_c_bindings.py
│  │     │  │  │  │  ├─ mediapipe_c_utils.py
│  │     │  │  │  │  ├─ optional_dependencies.py
│  │     │  │  │  │  ├─ serial_dispatcher.py
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  └─ __pycache__
│  │     │  │  │  │     ├─ async_result_dispatcher.cpython-313.pyc
│  │     │  │  │  │     ├─ base_options.cpython-313.pyc
│  │     │  │  │  │     ├─ base_options_c.cpython-313.pyc
│  │     │  │  │  │     ├─ mediapipe_c_bindings.cpython-313.pyc
│  │     │  │  │  │     ├─ mediapipe_c_utils.cpython-313.pyc
│  │     │  │  │  │     ├─ optional_dependencies.cpython-313.pyc
│  │     │  │  │  │     ├─ serial_dispatcher.cpython-313.pyc
│  │     │  │  │  │     └─ __init__.cpython-313.pyc
│  │     │  │  │  ├─ genai
│  │     │  │  │  │  ├─ bundler
│  │     │  │  │  │  │  ├─ llm_bundler.py
│  │     │  │  │  │  │  ├─ llm_bundler_metadata_options.py
│  │     │  │  │  │  │  ├─ llm_bundler_metadata_options_c.py
│  │     │  │  │  │  │  ├─ llm_bundler_metadata_options_test.py
│  │     │  │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  │  └─ __pycache__
│  │     │  │  │  │  │     ├─ llm_bundler.cpython-313.pyc
│  │     │  │  │  │  │     ├─ llm_bundler_metadata_options.cpython-313.pyc
│  │     │  │  │  │  │     ├─ llm_bundler_metadata_options_c.cpython-313.pyc
│  │     │  │  │  │  │     ├─ llm_bundler_metadata_options_test.cpython-313.pyc
│  │     │  │  │  │  │     └─ __init__.cpython-313.pyc
│  │     │  │  │  │  ├─ converter
│  │     │  │  │  │  │  ├─ converter_base.py
│  │     │  │  │  │  │  ├─ converter_factory.py
│  │     │  │  │  │  │  ├─ external_dependencies.py
│  │     │  │  │  │  │  ├─ llm_converter.py
│  │     │  │  │  │  │  ├─ llm_converter_test.py
│  │     │  │  │  │  │  ├─ pytorch_converter.py
│  │     │  │  │  │  │  ├─ pytorch_converter_test.py
│  │     │  │  │  │  │  ├─ quantization_util.py
│  │     │  │  │  │  │  ├─ quantization_util_test.py
│  │     │  │  │  │  │  ├─ safetensors_converter.py
│  │     │  │  │  │  │  ├─ safetensors_converter_test.py
│  │     │  │  │  │  │  ├─ weight_bins_writer.py
│  │     │  │  │  │  │  ├─ weight_bins_writer_test.py
│  │     │  │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  │  └─ __pycache__
│  │     │  │  │  │  │     ├─ converter_base.cpython-313.pyc
│  │     │  │  │  │  │     ├─ converter_factory.cpython-313.pyc
│  │     │  │  │  │  │     ├─ external_dependencies.cpython-313.pyc
│  │     │  │  │  │  │     ├─ llm_converter.cpython-313.pyc
│  │     │  │  │  │  │     ├─ llm_converter_test.cpython-313.pyc
│  │     │  │  │  │  │     ├─ pytorch_converter.cpython-313.pyc
│  │     │  │  │  │  │     ├─ pytorch_converter_test.cpython-313.pyc
│  │     │  │  │  │  │     ├─ quantization_util.cpython-313.pyc
│  │     │  │  │  │  │     ├─ quantization_util_test.cpython-313.pyc
│  │     │  │  │  │  │     ├─ safetensors_converter.cpython-313.pyc
│  │     │  │  │  │  │     ├─ safetensors_converter_test.cpython-313.pyc
│  │     │  │  │  │  │     ├─ weight_bins_writer.cpython-313.pyc
│  │     │  │  │  │  │     ├─ weight_bins_writer_test.cpython-313.pyc
│  │     │  │  │  │  │     └─ __init__.cpython-313.pyc
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  └─ __pycache__
│  │     │  │  │  │     └─ __init__.cpython-313.pyc
│  │     │  │  │  ├─ metadata
│  │     │  │  │  │  ├─ metadata.py
│  │     │  │  │  │  ├─ metadata_displayer_cli.py
│  │     │  │  │  │  ├─ metadata_writers
│  │     │  │  │  │  │  ├─ image_classifier.py
│  │     │  │  │  │  │  ├─ image_segmenter.py
│  │     │  │  │  │  │  ├─ metadata_info.py
│  │     │  │  │  │  │  ├─ metadata_writer.py
│  │     │  │  │  │  │  ├─ model_asset_bundle_utils.py
│  │     │  │  │  │  │  ├─ object_detector.py
│  │     │  │  │  │  │  ├─ text_classifier.py
│  │     │  │  │  │  │  ├─ writer_utils.py
│  │     │  │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  │  └─ __pycache__
│  │     │  │  │  │  │     ├─ image_classifier.cpython-313.pyc
│  │     │  │  │  │  │     ├─ image_segmenter.cpython-313.pyc
│  │     │  │  │  │  │     ├─ metadata_info.cpython-313.pyc
│  │     │  │  │  │  │     ├─ metadata_writer.cpython-313.pyc
│  │     │  │  │  │  │     ├─ model_asset_bundle_utils.cpython-313.pyc
│  │     │  │  │  │  │     ├─ object_detector.cpython-313.pyc
│  │     │  │  │  │  │     ├─ text_classifier.cpython-313.pyc
│  │     │  │  │  │  │     ├─ writer_utils.cpython-313.pyc
│  │     │  │  │  │  │     └─ __init__.cpython-313.pyc
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  └─ __pycache__
│  │     │  │  │  │     ├─ metadata.cpython-313.pyc
│  │     │  │  │  │     ├─ metadata_displayer_cli.cpython-313.pyc
│  │     │  │  │  │     └─ __init__.cpython-313.pyc
│  │     │  │  │  ├─ test
│  │     │  │  │  │  ├─ audio
│  │     │  │  │  │  │  ├─ audio_classifier_test.py
│  │     │  │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  │  └─ __pycache__
│  │     │  │  │  │  │     ├─ audio_classifier_test.cpython-313.pyc
│  │     │  │  │  │  │     └─ __init__.cpython-313.pyc
│  │     │  │  │  │  ├─ test_utils.py
│  │     │  │  │  │  ├─ text
│  │     │  │  │  │  │  ├─ language_detector_test.py
│  │     │  │  │  │  │  ├─ text_classifier_test.py
│  │     │  │  │  │  │  ├─ text_embedder_test.py
│  │     │  │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  │  └─ __pycache__
│  │     │  │  │  │  │     ├─ language_detector_test.cpython-313.pyc
│  │     │  │  │  │  │     ├─ text_classifier_test.cpython-313.pyc
│  │     │  │  │  │  │     └─ __init__.cpython-313.pyc
│  │     │  │  │  │  ├─ vision
│  │     │  │  │  │  │  ├─ face_detector_test.py
│  │     │  │  │  │  │  ├─ face_landmarker_test.py
│  │     │  │  │  │  │  ├─ hand_landmarker_test.py
│  │     │  │  │  │  │  ├─ holistic_landmarker_test.py
│  │     │  │  │  │  │  ├─ image_classifier_test.py
│  │     │  │  │  │  │  ├─ image_embedder_test.py
│  │     │  │  │  │  │  ├─ image_segmenter_test.py
│  │     │  │  │  │  │  ├─ image_test.py
│  │     │  │  │  │  │  ├─ interactive_segmenter_test.py
│  │     │  │  │  │  │  ├─ object_detector_test.py
│  │     │  │  │  │  │  ├─ pose_landmarker_test.py
│  │     │  │  │  │  │  ├─ proto_utils.py
│  │     │  │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  │  └─ __pycache__
│  │     │  │  │  │  │     ├─ face_detector_test.cpython-313.pyc
│  │     │  │  │  │  │     ├─ face_landmarker_test.cpython-313.pyc
│  │     │  │  │  │  │     ├─ hand_landmarker_test.cpython-313.pyc
│  │     │  │  │  │  │     ├─ holistic_landmarker_test.cpython-313.pyc
│  │     │  │  │  │  │     ├─ image_classifier_test.cpython-313.pyc
│  │     │  │  │  │  │     ├─ image_embedder_test.cpython-313.pyc
│  │     │  │  │  │  │     ├─ image_segmenter_test.cpython-313.pyc
│  │     │  │  │  │  │     ├─ image_test.cpython-313.pyc
│  │     │  │  │  │  │     ├─ interactive_segmenter_test.cpython-313.pyc
│  │     │  │  │  │  │     ├─ object_detector_test.cpython-313.pyc
│  │     │  │  │  │  │     ├─ pose_landmarker_test.cpython-313.pyc
│  │     │  │  │  │  │     ├─ proto_utils.cpython-313.pyc
│  │     │  │  │  │  │     └─ __init__.cpython-313.pyc
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  └─ __pycache__
│  │     │  │  │  │     ├─ test_utils.cpython-313.pyc
│  │     │  │  │  │     └─ __init__.cpython-313.pyc
│  │     │  │  │  ├─ text
│  │     │  │  │  │  ├─ language_detector.py
│  │     │  │  │  │  ├─ text_classifier.py
│  │     │  │  │  │  ├─ text_embedder.py
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  └─ __pycache__
│  │     │  │  │  │     ├─ language_detector.cpython-313.pyc
│  │     │  │  │  │     ├─ text_classifier.cpython-313.pyc
│  │     │  │  │  │     ├─ text_embedder.cpython-313.pyc
│  │     │  │  │  │     └─ __init__.cpython-313.pyc
│  │     │  │  │  ├─ vision
│  │     │  │  │  │  ├─ core
│  │     │  │  │  │  │  ├─ image.py
│  │     │  │  │  │  │  ├─ image_processing_options.py
│  │     │  │  │  │  │  ├─ image_processing_options_c.py
│  │     │  │  │  │  │  ├─ vision_task_running_mode.py
│  │     │  │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  │  └─ __pycache__
│  │     │  │  │  │  │     ├─ image.cpython-313.pyc
│  │     │  │  │  │  │     ├─ image_processing_options.cpython-313.pyc
│  │     │  │  │  │  │     ├─ image_processing_options_c.cpython-313.pyc
│  │     │  │  │  │  │     ├─ vision_task_running_mode.cpython-313.pyc
│  │     │  │  │  │  │     └─ __init__.cpython-313.pyc
│  │     │  │  │  │  ├─ drawing_styles.py
│  │     │  │  │  │  ├─ drawing_utils.py
│  │     │  │  │  │  ├─ face_detector.py
│  │     │  │  │  │  ├─ face_landmarker.py
│  │     │  │  │  │  ├─ gesture_recognizer.py
│  │     │  │  │  │  ├─ gesture_recognizer_result.py
│  │     │  │  │  │  ├─ gesture_recognizer_result_c.py
│  │     │  │  │  │  ├─ hand_landmarker.py
│  │     │  │  │  │  ├─ holistic_landmarker.py
│  │     │  │  │  │  ├─ image_classifier.py
│  │     │  │  │  │  ├─ image_embedder.py
│  │     │  │  │  │  ├─ image_segmenter.py
│  │     │  │  │  │  ├─ interactive_segmenter.py
│  │     │  │  │  │  ├─ object_detector.py
│  │     │  │  │  │  ├─ pose_landmarker.py
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  └─ __pycache__
│  │     │  │  │  │     ├─ drawing_styles.cpython-313.pyc
│  │     │  │  │  │     ├─ drawing_utils.cpython-313.pyc
│  │     │  │  │  │     ├─ face_detector.cpython-313.pyc
│  │     │  │  │  │     ├─ face_landmarker.cpython-313.pyc
│  │     │  │  │  │     ├─ gesture_recognizer.cpython-313.pyc
│  │     │  │  │  │     ├─ gesture_recognizer_result.cpython-313.pyc
│  │     │  │  │  │     ├─ gesture_recognizer_result_c.cpython-313.pyc
│  │     │  │  │  │     ├─ hand_landmarker.cpython-313.pyc
│  │     │  │  │  │     ├─ holistic_landmarker.cpython-313.pyc
│  │     │  │  │  │     ├─ image_classifier.cpython-313.pyc
│  │     │  │  │  │     ├─ image_embedder.cpython-313.pyc
│  │     │  │  │  │     ├─ image_segmenter.cpython-313.pyc
│  │     │  │  │  │     ├─ interactive_segmenter.cpython-313.pyc
│  │     │  │  │  │     ├─ object_detector.cpython-313.pyc
│  │     │  │  │  │     ├─ pose_landmarker.cpython-313.pyc
│  │     │  │  │  │     └─ __init__.cpython-313.pyc
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     └─ __init__.cpython-313.pyc
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     └─ __init__.cpython-313.pyc
│  │     │  ├─ __init__.py
│  │     │  └─ __pycache__
│  │     │     └─ __init__.cpython-313.pyc
│  │     ├─ mediapipe-0.10.33.dist-info
│  │     │  ├─ INSTALLER
│  │     │  ├─ licenses
│  │     │  │  └─ LICENSE
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  ├─ REQUESTED
│  │     │  ├─ top_level.txt
│  │     │  └─ WHEEL
│  │     ├─ mpl_toolkits
│  │     │  ├─ axes_grid1
│  │     │  │  ├─ anchored_artists.py
│  │     │  │  ├─ axes_divider.py
│  │     │  │  ├─ axes_grid.py
│  │     │  │  ├─ axes_rgb.py
│  │     │  │  ├─ axes_size.py
│  │     │  │  ├─ inset_locator.py
│  │     │  │  ├─ mpl_axes.py
│  │     │  │  ├─ parasite_axes.py
│  │     │  │  ├─ tests
│  │     │  │  │  ├─ conftest.py
│  │     │  │  │  ├─ test_axes_grid1.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ conftest.cpython-313.pyc
│  │     │  │  │     ├─ test_axes_grid1.cpython-313.pyc
│  │     │  │  │     └─ __init__.cpython-313.pyc
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ anchored_artists.cpython-313.pyc
│  │     │  │     ├─ axes_divider.cpython-313.pyc
│  │     │  │     ├─ axes_grid.cpython-313.pyc
│  │     │  │     ├─ axes_rgb.cpython-313.pyc
│  │     │  │     ├─ axes_size.cpython-313.pyc
│  │     │  │     ├─ inset_locator.cpython-313.pyc
│  │     │  │     ├─ mpl_axes.cpython-313.pyc
│  │     │  │     ├─ parasite_axes.cpython-313.pyc
│  │     │  │     └─ __init__.cpython-313.pyc
│  │     │  ├─ axisartist
│  │     │  │  ├─ angle_helper.py
│  │     │  │  ├─ axes_divider.py
│  │     │  │  ├─ axislines.py
│  │     │  │  ├─ axisline_style.py
│  │     │  │  ├─ axis_artist.py
│  │     │  │  ├─ floating_axes.py
│  │     │  │  ├─ grid_finder.py
│  │     │  │  ├─ grid_helper_curvelinear.py
│  │     │  │  ├─ parasite_axes.py
│  │     │  │  ├─ tests
│  │     │  │  │  ├─ conftest.py
│  │     │  │  │  ├─ test_angle_helper.py
│  │     │  │  │  ├─ test_axislines.py
│  │     │  │  │  ├─ test_axis_artist.py
│  │     │  │  │  ├─ test_floating_axes.py
│  │     │  │  │  ├─ test_grid_finder.py
│  │     │  │  │  ├─ test_grid_helper_curvelinear.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ conftest.cpython-313.pyc
│  │     │  │  │     ├─ test_angle_helper.cpython-313.pyc
│  │     │  │  │     ├─ test_axislines.cpython-313.pyc
│  │     │  │  │     ├─ test_axis_artist.cpython-313.pyc
│  │     │  │  │     ├─ test_floating_axes.cpython-313.pyc
│  │     │  │  │     ├─ test_grid_finder.cpython-313.pyc
│  │     │  │  │     ├─ test_grid_helper_curvelinear.cpython-313.pyc
│  │     │  │  │     └─ __init__.cpython-313.pyc
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ angle_helper.cpython-313.pyc
│  │     │  │     ├─ axes_divider.cpython-313.pyc
│  │     │  │     ├─ axislines.cpython-313.pyc
│  │     │  │     ├─ axisline_style.cpython-313.pyc
│  │     │  │     ├─ axis_artist.cpython-313.pyc
│  │     │  │     ├─ floating_axes.cpython-313.pyc
│  │     │  │     ├─ grid_finder.cpython-313.pyc
│  │     │  │     ├─ grid_helper_curvelinear.cpython-313.pyc
│  │     │  │     ├─ parasite_axes.cpython-313.pyc
│  │     │  │     └─ __init__.cpython-313.pyc
│  │     │  └─ mplot3d
│  │     │     ├─ art3d.py
│  │     │     ├─ axes3d.py
│  │     │     ├─ axis3d.py
│  │     │     ├─ proj3d.py
│  │     │     ├─ tests
│  │     │     │  ├─ conftest.py
│  │     │     │  ├─ test_art3d.py
│  │     │     │  ├─ test_axes3d.py
│  │     │     │  ├─ test_legend3d.py
│  │     │     │  ├─ __init__.py
│  │     │     │  └─ __pycache__
│  │     │     │     ├─ conftest.cpython-313.pyc
│  │     │     │     ├─ test_art3d.cpython-313.pyc
│  │     │     │     ├─ test_axes3d.cpython-313.pyc
│  │     │     │     ├─ test_legend3d.cpython-313.pyc
│  │     │     │     └─ __init__.cpython-313.pyc
│  │     │     ├─ __init__.py
│  │     │     └─ __pycache__
│  │     │        ├─ art3d.cpython-313.pyc
│  │     │        ├─ axes3d.cpython-313.pyc
│  │     │        ├─ axis3d.cpython-313.pyc
│  │     │        ├─ proj3d.cpython-313.pyc
│  │     │        └─ __init__.cpython-313.pyc
│  │     ├─ multipart
│  │     │  ├─ decoders.py
│  │     │  ├─ exceptions.py
│  │     │  ├─ multipart.py
│  │     │  ├─ __init__.py
│  │     │  └─ __pycache__
│  │     │     ├─ decoders.cpython-313.pyc
│  │     │     ├─ exceptions.cpython-313.pyc
│  │     │     ├─ multipart.cpython-313.pyc
│  │     │     └─ __init__.cpython-313.pyc
│  │     ├─ numpy
│  │     │  ├─ char
│  │     │  │  ├─ __init__.py
│  │     │  │  ├─ __init__.pyi
│  │     │  │  └─ __pycache__
│  │     │  │     └─ __init__.cpython-313.pyc
│  │     │  ├─ compat
│  │     │  │  ├─ py3k.py
│  │     │  │  ├─ tests
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     └─ __init__.cpython-313.pyc
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ py3k.cpython-313.pyc
│  │     │  │     └─ __init__.cpython-313.pyc
│  │     │  ├─ conftest.py
│  │     │  ├─ core
│  │     │  │  ├─ arrayprint.py
│  │     │  │  ├─ defchararray.py
│  │     │  │  ├─ einsumfunc.py
│  │     │  │  ├─ fromnumeric.py
│  │     │  │  ├─ function_base.py
│  │     │  │  ├─ getlimits.py
│  │     │  │  ├─ multiarray.py
│  │     │  │  ├─ numeric.py
│  │     │  │  ├─ numerictypes.py
│  │     │  │  ├─ overrides.py
│  │     │  │  ├─ records.py
│  │     │  │  ├─ shape_base.py
│  │     │  │  ├─ umath.py
│  │     │  │  ├─ _dtype.py
│  │     │  │  ├─ _dtype_ctypes.py
│  │     │  │  ├─ _internal.py
│  │     │  │  ├─ _multiarray_umath.py
│  │     │  │  ├─ _utils.py
│  │     │  │  ├─ __init__.py
│  │     │  │  ├─ __init__.pyi
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ arrayprint.cpython-313.pyc
│  │     │  │     ├─ defchararray.cpython-313.pyc
│  │     │  │     ├─ einsumfunc.cpython-313.pyc
│  │     │  │     ├─ fromnumeric.cpython-313.pyc
│  │     │  │     ├─ function_base.cpython-313.pyc
│  │     │  │     ├─ getlimits.cpython-313.pyc
│  │     │  │     ├─ multiarray.cpython-313.pyc
│  │     │  │     ├─ numeric.cpython-313.pyc
│  │     │  │     ├─ numerictypes.cpython-313.pyc
│  │     │  │     ├─ overrides.cpython-313.pyc
│  │     │  │     ├─ records.cpython-313.pyc
│  │     │  │     ├─ shape_base.cpython-313.pyc
│  │     │  │     ├─ umath.cpython-313.pyc
│  │     │  │     ├─ _dtype.cpython-313.pyc
│  │     │  │     ├─ _dtype_ctypes.cpython-313.pyc
│  │     │  │     ├─ _internal.cpython-313.pyc
│  │     │  │     ├─ _multiarray_umath.cpython-313.pyc
│  │     │  │     ├─ _utils.cpython-313.pyc
│  │     │  │     └─ __init__.cpython-313.pyc
│  │     │  ├─ ctypeslib.py
│  │     │  ├─ ctypeslib.pyi
│  │     │  ├─ doc
│  │     │  │  ├─ ufuncs.py
│  │     │  │  └─ __pycache__
│  │     │  │     └─ ufuncs.cpython-313.pyc
│  │     │  ├─ dtypes.py
│  │     │  ├─ dtypes.pyi
│  │     │  ├─ exceptions.py
│  │     │  ├─ exceptions.pyi
│  │     │  ├─ f2py
│  │     │  │  ├─ auxfuncs.py
│  │     │  │  ├─ capi_maps.py
│  │     │  │  ├─ cb_rules.py
│  │     │  │  ├─ cfuncs.py
│  │     │  │  ├─ common_rules.py
│  │     │  │  ├─ crackfortran.py
│  │     │  │  ├─ diagnose.py
│  │     │  │  ├─ f2py2e.py
│  │     │  │  ├─ f90mod_rules.py
│  │     │  │  ├─ func2subr.py
│  │     │  │  ├─ rules.py
│  │     │  │  ├─ setup.cfg
│  │     │  │  ├─ src
│  │     │  │  │  ├─ fortranobject.c
│  │     │  │  │  └─ fortranobject.h
│  │     │  │  ├─ symbolic.py
│  │     │  │  ├─ tests
│  │     │  │  │  ├─ src
│  │     │  │  │  │  ├─ abstract_interface
│  │     │  │  │  │  │  ├─ foo.f90
│  │     │  │  │  │  │  └─ gh18403_mod.f90
│  │     │  │  │  │  ├─ array_from_pyobj
│  │     │  │  │  │  │  └─ wrapmodule.c
│  │     │  │  │  │  ├─ assumed_shape
│  │     │  │  │  │  │  ├─ .f2py_f2cmap
│  │     │  │  │  │  │  ├─ foo_free.f90
│  │     │  │  │  │  │  ├─ foo_mod.f90
│  │     │  │  │  │  │  ├─ foo_use.f90
│  │     │  │  │  │  │  └─ precision.f90
│  │     │  │  │  │  ├─ block_docstring
│  │     │  │  │  │  │  └─ foo.f
│  │     │  │  │  │  ├─ callback
│  │     │  │  │  │  │  ├─ foo.f
│  │     │  │  │  │  │  ├─ gh17797.f90
│  │     │  │  │  │  │  ├─ gh18335.f90
│  │     │  │  │  │  │  ├─ gh25211.f
│  │     │  │  │  │  │  ├─ gh25211.pyf
│  │     │  │  │  │  │  └─ gh26681.f90
│  │     │  │  │  │  ├─ cli
│  │     │  │  │  │  │  ├─ gh_22819.pyf
│  │     │  │  │  │  │  ├─ hi77.f
│  │     │  │  │  │  │  └─ hiworld.f90
│  │     │  │  │  │  ├─ common
│  │     │  │  │  │  │  ├─ block.f
│  │     │  │  │  │  │  └─ gh19161.f90
│  │     │  │  │  │  ├─ crackfortran
│  │     │  │  │  │  │  ├─ accesstype.f90
│  │     │  │  │  │  │  ├─ data_common.f
│  │     │  │  │  │  │  ├─ data_multiplier.f
│  │     │  │  │  │  │  ├─ data_stmts.f90
│  │     │  │  │  │  │  ├─ data_with_comments.f
│  │     │  │  │  │  │  ├─ foo_deps.f90
│  │     │  │  │  │  │  ├─ gh15035.f
│  │     │  │  │  │  │  ├─ gh17859.f
│  │     │  │  │  │  │  ├─ gh22648.pyf
│  │     │  │  │  │  │  ├─ gh23533.f
│  │     │  │  │  │  │  ├─ gh23598.f90
│  │     │  │  │  │  │  ├─ gh23598Warn.f90
│  │     │  │  │  │  │  ├─ gh23879.f90
│  │     │  │  │  │  │  ├─ gh27697.f90
│  │     │  │  │  │  │  ├─ gh2848.f90
│  │     │  │  │  │  │  ├─ operators.f90
│  │     │  │  │  │  │  ├─ privatemod.f90
│  │     │  │  │  │  │  ├─ publicmod.f90
│  │     │  │  │  │  │  ├─ pubprivmod.f90
│  │     │  │  │  │  │  └─ unicode_comment.f90
│  │     │  │  │  │  ├─ f2cmap
│  │     │  │  │  │  │  ├─ .f2py_f2cmap
│  │     │  │  │  │  │  └─ isoFortranEnvMap.f90
│  │     │  │  │  │  ├─ isocintrin
│  │     │  │  │  │  │  └─ isoCtests.f90
│  │     │  │  │  │  ├─ kind
│  │     │  │  │  │  │  └─ foo.f90
│  │     │  │  │  │  ├─ mixed
│  │     │  │  │  │  │  ├─ foo.f
│  │     │  │  │  │  │  ├─ foo_fixed.f90
│  │     │  │  │  │  │  └─ foo_free.f90
│  │     │  │  │  │  ├─ modules
│  │     │  │  │  │  │  ├─ gh25337
│  │     │  │  │  │  │  │  ├─ data.f90
│  │     │  │  │  │  │  │  └─ use_data.f90
│  │     │  │  │  │  │  ├─ gh26920
│  │     │  │  │  │  │  │  ├─ two_mods_with_no_public_entities.f90
│  │     │  │  │  │  │  │  └─ two_mods_with_one_public_routine.f90
│  │     │  │  │  │  │  ├─ module_data_docstring.f90
│  │     │  │  │  │  │  └─ use_modules.f90
│  │     │  │  │  │  ├─ negative_bounds
│  │     │  │  │  │  │  └─ issue_20853.f90
│  │     │  │  │  │  ├─ parameter
│  │     │  │  │  │  │  ├─ constant_array.f90
│  │     │  │  │  │  │  ├─ constant_both.f90
│  │     │  │  │  │  │  ├─ constant_compound.f90
│  │     │  │  │  │  │  ├─ constant_integer.f90
│  │     │  │  │  │  │  ├─ constant_non_compound.f90
│  │     │  │  │  │  │  └─ constant_real.f90
│  │     │  │  │  │  ├─ quoted_character
│  │     │  │  │  │  │  └─ foo.f
│  │     │  │  │  │  ├─ regression
│  │     │  │  │  │  │  ├─ AB.inc
│  │     │  │  │  │  │  ├─ assignOnlyModule.f90
│  │     │  │  │  │  │  ├─ datonly.f90
│  │     │  │  │  │  │  ├─ f77comments.f
│  │     │  │  │  │  │  ├─ f77fixedform.f95
│  │     │  │  │  │  │  ├─ f90continuation.f90
│  │     │  │  │  │  │  ├─ incfile.f90
│  │     │  │  │  │  │  └─ inout.f90
│  │     │  │  │  │  ├─ return_character
│  │     │  │  │  │  │  ├─ foo77.f
│  │     │  │  │  │  │  └─ foo90.f90
│  │     │  │  │  │  ├─ return_complex
│  │     │  │  │  │  │  ├─ foo77.f
│  │     │  │  │  │  │  └─ foo90.f90
│  │     │  │  │  │  ├─ return_integer
│  │     │  │  │  │  │  ├─ foo77.f
│  │     │  │  │  │  │  └─ foo90.f90
│  │     │  │  │  │  ├─ return_logical
│  │     │  │  │  │  │  ├─ foo77.f
│  │     │  │  │  │  │  └─ foo90.f90
│  │     │  │  │  │  ├─ return_real
│  │     │  │  │  │  │  ├─ foo77.f
│  │     │  │  │  │  │  └─ foo90.f90
│  │     │  │  │  │  ├─ routines
│  │     │  │  │  │  │  ├─ funcfortranname.f
│  │     │  │  │  │  │  ├─ funcfortranname.pyf
│  │     │  │  │  │  │  ├─ subrout.f
│  │     │  │  │  │  │  └─ subrout.pyf
│  │     │  │  │  │  ├─ size
│  │     │  │  │  │  │  └─ foo.f90
│  │     │  │  │  │  ├─ string
│  │     │  │  │  │  │  ├─ char.f90
│  │     │  │  │  │  │  ├─ fixed_string.f90
│  │     │  │  │  │  │  ├─ gh24008.f
│  │     │  │  │  │  │  ├─ gh24662.f90
│  │     │  │  │  │  │  ├─ gh25286.f90
│  │     │  │  │  │  │  ├─ gh25286.pyf
│  │     │  │  │  │  │  ├─ gh25286_bc.pyf
│  │     │  │  │  │  │  ├─ scalar_string.f90
│  │     │  │  │  │  │  └─ string.f
│  │     │  │  │  │  └─ value_attrspec
│  │     │  │  │  │     └─ gh21665.f90
│  │     │  │  │  ├─ test_abstract_interface.py
│  │     │  │  │  ├─ test_array_from_pyobj.py
│  │     │  │  │  ├─ test_assumed_shape.py
│  │     │  │  │  ├─ test_block_docstring.py
│  │     │  │  │  ├─ test_callback.py
│  │     │  │  │  ├─ test_character.py
│  │     │  │  │  ├─ test_common.py
│  │     │  │  │  ├─ test_crackfortran.py
│  │     │  │  │  ├─ test_data.py
│  │     │  │  │  ├─ test_docs.py
│  │     │  │  │  ├─ test_f2cmap.py
│  │     │  │  │  ├─ test_f2py2e.py
│  │     │  │  │  ├─ test_isoc.py
│  │     │  │  │  ├─ test_kind.py
│  │     │  │  │  ├─ test_mixed.py
│  │     │  │  │  ├─ test_modules.py
│  │     │  │  │  ├─ test_parameter.py
│  │     │  │  │  ├─ test_pyf_src.py
│  │     │  │  │  ├─ test_quoted_character.py
│  │     │  │  │  ├─ test_regression.py
│  │     │  │  │  ├─ test_return_character.py
│  │     │  │  │  ├─ test_return_complex.py
│  │     │  │  │  ├─ test_return_integer.py
│  │     │  │  │  ├─ test_return_logical.py
│  │     │  │  │  ├─ test_return_real.py
│  │     │  │  │  ├─ test_routines.py
│  │     │  │  │  ├─ test_semicolon_split.py
│  │     │  │  │  ├─ test_size.py
│  │     │  │  │  ├─ test_string.py
│  │     │  │  │  ├─ test_symbolic.py
│  │     │  │  │  ├─ test_value_attrspec.py
│  │     │  │  │  ├─ util.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ test_abstract_interface.cpython-313.pyc
│  │     │  │  │     ├─ test_array_from_pyobj.cpython-313.pyc
│  │     │  │  │     ├─ test_assumed_shape.cpython-313.pyc
│  │     │  │  │     ├─ test_block_docstring.cpython-313.pyc
│  │     │  │  │     ├─ test_callback.cpython-313.pyc
│  │     │  │  │     ├─ test_character.cpython-313.pyc
│  │     │  │  │     ├─ test_common.cpython-313.pyc
│  │     │  │  │     ├─ test_crackfortran.cpython-313.pyc
│  │     │  │  │     ├─ test_data.cpython-313.pyc
│  │     │  │  │     ├─ test_docs.cpython-313.pyc
│  │     │  │  │     ├─ test_f2cmap.cpython-313.pyc
│  │     │  │  │     ├─ test_f2py2e.cpython-313.pyc
│  │     │  │  │     ├─ test_isoc.cpython-313.pyc
│  │     │  │  │     ├─ test_kind.cpython-313.pyc
│  │     │  │  │     ├─ test_mixed.cpython-313.pyc
│  │     │  │  │     ├─ test_modules.cpython-313.pyc
│  │     │  │  │     ├─ test_parameter.cpython-313.pyc
│  │     │  │  │     ├─ test_pyf_src.cpython-313.pyc
│  │     │  │  │     ├─ test_quoted_character.cpython-313.pyc
│  │     │  │  │     ├─ test_regression.cpython-313.pyc
│  │     │  │  │     ├─ test_return_character.cpython-313.pyc
│  │     │  │  │     ├─ test_return_complex.cpython-313.pyc
│  │     │  │  │     ├─ test_return_integer.cpython-313.pyc
│  │     │  │  │     ├─ test_return_logical.cpython-313.pyc
│  │     │  │  │     ├─ test_return_real.cpython-313.pyc
│  │     │  │  │     ├─ test_routines.cpython-313.pyc
│  │     │  │  │     ├─ test_semicolon_split.cpython-313.pyc
│  │     │  │  │     ├─ test_size.cpython-313.pyc
│  │     │  │  │     ├─ test_string.cpython-313.pyc
│  │     │  │  │     ├─ test_symbolic.cpython-313.pyc
│  │     │  │  │     ├─ test_value_attrspec.cpython-313.pyc
│  │     │  │  │     ├─ util.cpython-313.pyc
│  │     │  │  │     └─ __init__.cpython-313.pyc
│  │     │  │  ├─ use_rules.py
│  │     │  │  ├─ _backends
│  │     │  │  │  ├─ meson.build.template
│  │     │  │  │  ├─ _backend.py
│  │     │  │  │  ├─ _distutils.py
│  │     │  │  │  ├─ _meson.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ _backend.cpython-313.pyc
│  │     │  │  │     ├─ _distutils.cpython-313.pyc
│  │     │  │  │     ├─ _meson.cpython-313.pyc
│  │     │  │  │     └─ __init__.cpython-313.pyc
│  │     │  │  ├─ _isocbind.py
│  │     │  │  ├─ _src_pyf.py
│  │     │  │  ├─ __init__.py
│  │     │  │  ├─ __init__.pyi
│  │     │  │  ├─ __main__.py
│  │     │  │  ├─ __pycache__
│  │     │  │  │  ├─ auxfuncs.cpython-313.pyc
│  │     │  │  │  ├─ capi_maps.cpython-313.pyc
│  │     │  │  │  ├─ cb_rules.cpython-313.pyc
│  │     │  │  │  ├─ cfuncs.cpython-313.pyc
│  │     │  │  │  ├─ common_rules.cpython-313.pyc
│  │     │  │  │  ├─ crackfortran.cpython-313.pyc
│  │     │  │  │  ├─ diagnose.cpython-313.pyc
│  │     │  │  │  ├─ f2py2e.cpython-313.pyc
│  │     │  │  │  ├─ f90mod_rules.cpython-313.pyc
│  │     │  │  │  ├─ func2subr.cpython-313.pyc
│  │     │  │  │  ├─ rules.cpython-313.pyc
│  │     │  │  │  ├─ symbolic.cpython-313.pyc
│  │     │  │  │  ├─ use_rules.cpython-313.pyc
│  │     │  │  │  ├─ _isocbind.cpython-313.pyc
│  │     │  │  │  ├─ _src_pyf.cpython-313.pyc
│  │     │  │  │  ├─ __init__.cpython-313.pyc
│  │     │  │  │  ├─ __main__.cpython-313.pyc
│  │     │  │  │  └─ __version__.cpython-313.pyc
│  │     │  │  └─ __version__.py
│  │     │  ├─ fft
│  │     │  │  ├─ helper.py
│  │     │  │  ├─ tests
│  │     │  │  │  ├─ test_helper.py
│  │     │  │  │  ├─ test_pocketfft.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ test_helper.cpython-313.pyc
│  │     │  │  │     ├─ test_pocketfft.cpython-313.pyc
│  │     │  │  │     └─ __init__.cpython-313.pyc
│  │     │  │  ├─ _helper.py
│  │     │  │  ├─ _helper.pyi
│  │     │  │  ├─ _pocketfft.py
│  │     │  │  ├─ _pocketfft.pyi
│  │     │  │  ├─ _pocketfft_umath.cp313-win_amd64.lib
│  │     │  │  ├─ _pocketfft_umath.cp313-win_amd64.pyd
│  │     │  │  ├─ __init__.py
│  │     │  │  ├─ __init__.pyi
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ helper.cpython-313.pyc
│  │     │  │     ├─ _helper.cpython-313.pyc
│  │     │  │     ├─ _pocketfft.cpython-313.pyc
│  │     │  │     └─ __init__.cpython-313.pyc
│  │     │  ├─ lib
│  │     │  │  ├─ array_utils.py
│  │     │  │  ├─ array_utils.pyi
│  │     │  │  ├─ format.py
│  │     │  │  ├─ format.pyi
│  │     │  │  ├─ introspect.py
│  │     │  │  ├─ mixins.py
│  │     │  │  ├─ mixins.pyi
│  │     │  │  ├─ npyio.py
│  │     │  │  ├─ npyio.pyi
│  │     │  │  ├─ recfunctions.py
│  │     │  │  ├─ scimath.py
│  │     │  │  ├─ scimath.pyi
│  │     │  │  ├─ stride_tricks.py
│  │     │  │  ├─ stride_tricks.pyi
│  │     │  │  ├─ tests
│  │     │  │  │  ├─ data
│  │     │  │  │  │  ├─ py2-np0-objarr.npy
│  │     │  │  │  │  ├─ py2-objarr.npy
│  │     │  │  │  │  ├─ py2-objarr.npz
│  │     │  │  │  │  ├─ py3-objarr.npy
│  │     │  │  │  │  ├─ py3-objarr.npz
│  │     │  │  │  │  ├─ python3.npy
│  │     │  │  │  │  └─ win64python2.npy
│  │     │  │  │  ├─ test_arraypad.py
│  │     │  │  │  ├─ test_arraysetops.py
│  │     │  │  │  ├─ test_arrayterator.py
│  │     │  │  │  ├─ test_array_utils.py
│  │     │  │  │  ├─ test_format.py
│  │     │  │  │  ├─ test_function_base.py
│  │     │  │  │  ├─ test_histograms.py
│  │     │  │  │  ├─ test_index_tricks.py
│  │     │  │  │  ├─ test_io.py
│  │     │  │  │  ├─ test_loadtxt.py
│  │     │  │  │  ├─ test_mixins.py
│  │     │  │  │  ├─ test_nanfunctions.py
│  │     │  │  │  ├─ test_packbits.py
│  │     │  │  │  ├─ test_polynomial.py
│  │     │  │  │  ├─ test_recfunctions.py
│  │     │  │  │  ├─ test_regression.py
│  │     │  │  │  ├─ test_shape_base.py
│  │     │  │  │  ├─ test_stride_tricks.py
│  │     │  │  │  ├─ test_twodim_base.py
│  │     │  │  │  ├─ test_type_check.py
│  │     │  │  │  ├─ test_ufunclike.py
│  │     │  │  │  ├─ test_utils.py
│  │     │  │  │  ├─ test__datasource.py
│  │     │  │  │  ├─ test__iotools.py
│  │     │  │  │  ├─ test__version.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ test_arraypad.cpython-313.pyc
│  │     │  │  │     ├─ test_arraysetops.cpython-313.pyc
│  │     │  │  │     ├─ test_arrayterator.cpython-313.pyc
│  │     │  │  │     ├─ test_array_utils.cpython-313.pyc
│  │     │  │  │     ├─ test_format.cpython-313.pyc
│  │     │  │  │     ├─ test_function_base.cpython-313.pyc
│  │     │  │  │     ├─ test_histograms.cpython-313.pyc
│  │     │  │  │     ├─ test_index_tricks.cpython-313.pyc
│  │     │  │  │     ├─ test_io.cpython-313.pyc
│  │     │  │  │     ├─ test_loadtxt.cpython-313.pyc
│  │     │  │  │     ├─ test_mixins.cpython-313.pyc
│  │     │  │  │     ├─ test_nanfunctions.cpython-313.pyc
│  │     │  │  │     ├─ test_packbits.cpython-313.pyc
│  │     │  │  │     ├─ test_polynomial.cpython-313.pyc
│  │     │  │  │     ├─ test_recfunctions.cpython-313.pyc
│  │     │  │  │     ├─ test_regression.cpython-313.pyc
│  │     │  │  │     ├─ test_shape_base.cpython-313.pyc
│  │     │  │  │     ├─ test_stride_tricks.cpython-313.pyc
│  │     │  │  │     ├─ test_twodim_base.cpython-313.pyc
│  │     │  │  │     ├─ test_type_check.cpython-313.pyc
│  │     │  │  │     ├─ test_ufunclike.cpython-313.pyc
│  │     │  │  │     ├─ test_utils.cpython-313.pyc
│  │     │  │  │     ├─ test__datasource.cpython-313.pyc
│  │     │  │  │     ├─ test__iotools.cpython-313.pyc
│  │     │  │  │     ├─ test__version.cpython-313.pyc
│  │     │  │  │     └─ __init__.cpython-313.pyc
│  │     │  │  ├─ user_array.py
│  │     │  │  ├─ _arraypad_impl.py
│  │     │  │  ├─ _arraypad_impl.pyi
│  │     │  │  ├─ _arraysetops_impl.py
│  │     │  │  ├─ _arraysetops_impl.pyi
│  │     │  │  ├─ _arrayterator_impl.py
│  │     │  │  ├─ _arrayterator_impl.pyi
│  │     │  │  ├─ _array_utils_impl.py
│  │     │  │  ├─ _array_utils_impl.pyi
│  │     │  │  ├─ _datasource.py
│  │     │  │  ├─ _function_base_impl.py
│  │     │  │  ├─ _function_base_impl.pyi
│  │     │  │  ├─ _histograms_impl.py
│  │     │  │  ├─ _histograms_impl.pyi
│  │     │  │  ├─ _index_tricks_impl.py
│  │     │  │  ├─ _index_tricks_impl.pyi
│  │     │  │  ├─ _iotools.py
│  │     │  │  ├─ _nanfunctions_impl.py
│  │     │  │  ├─ _nanfunctions_impl.pyi
│  │     │  │  ├─ _npyio_impl.py
│  │     │  │  ├─ _npyio_impl.pyi
│  │     │  │  ├─ _polynomial_impl.py
│  │     │  │  ├─ _polynomial_impl.pyi
│  │     │  │  ├─ _scimath_impl.py
│  │     │  │  ├─ _scimath_impl.pyi
│  │     │  │  ├─ _shape_base_impl.py
│  │     │  │  ├─ _shape_base_impl.pyi
│  │     │  │  ├─ _stride_tricks_impl.py
│  │     │  │  ├─ _stride_tricks_impl.pyi
│  │     │  │  ├─ _twodim_base_impl.py
│  │     │  │  ├─ _twodim_base_impl.pyi
│  │     │  │  ├─ _type_check_impl.py
│  │     │  │  ├─ _type_check_impl.pyi
│  │     │  │  ├─ _ufunclike_impl.py
│  │     │  │  ├─ _ufunclike_impl.pyi
│  │     │  │  ├─ _user_array_impl.py
│  │     │  │  ├─ _utils_impl.py
│  │     │  │  ├─ _utils_impl.pyi
│  │     │  │  ├─ _version.py
│  │     │  │  ├─ _version.pyi
│  │     │  │  ├─ __init__.py
│  │     │  │  ├─ __init__.pyi
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ array_utils.cpython-313.pyc
│  │     │  │     ├─ format.cpython-313.pyc
│  │     │  │     ├─ introspect.cpython-313.pyc
│  │     │  │     ├─ mixins.cpython-313.pyc
│  │     │  │     ├─ npyio.cpython-313.pyc
│  │     │  │     ├─ recfunctions.cpython-313.pyc
│  │     │  │     ├─ scimath.cpython-313.pyc
│  │     │  │     ├─ stride_tricks.cpython-313.pyc
│  │     │  │     ├─ user_array.cpython-313.pyc
│  │     │  │     ├─ _arraypad_impl.cpython-313.pyc
│  │     │  │     ├─ _arraysetops_impl.cpython-313.pyc
│  │     │  │     ├─ _arrayterator_impl.cpython-313.pyc
│  │     │  │     ├─ _array_utils_impl.cpython-313.pyc
│  │     │  │     ├─ _datasource.cpython-313.pyc
│  │     │  │     ├─ _function_base_impl.cpython-313.pyc
│  │     │  │     ├─ _histograms_impl.cpython-313.pyc
│  │     │  │     ├─ _index_tricks_impl.cpython-313.pyc
│  │     │  │     ├─ _iotools.cpython-313.pyc
│  │     │  │     ├─ _nanfunctions_impl.cpython-313.pyc
│  │     │  │     ├─ _npyio_impl.cpython-313.pyc
│  │     │  │     ├─ _polynomial_impl.cpython-313.pyc
│  │     │  │     ├─ _scimath_impl.cpython-313.pyc
│  │     │  │     ├─ _shape_base_impl.cpython-313.pyc
│  │     │  │     ├─ _stride_tricks_impl.cpython-313.pyc
│  │     │  │     ├─ _twodim_base_impl.cpython-313.pyc
│  │     │  │     ├─ _type_check_impl.cpython-313.pyc
│  │     │  │     ├─ _ufunclike_impl.cpython-313.pyc
│  │     │  │     ├─ _user_array_impl.cpython-313.pyc
│  │     │  │     ├─ _utils_impl.cpython-313.pyc
│  │     │  │     ├─ _version.cpython-313.pyc
│  │     │  │     └─ __init__.cpython-313.pyc
│  │     │  ├─ linalg
│  │     │  │  ├─ lapack_lite.cp313-win_amd64.lib
│  │     │  │  ├─ lapack_lite.cp313-win_amd64.pyd
│  │     │  │  ├─ linalg.py
│  │     │  │  ├─ tests
│  │     │  │  │  ├─ test_deprecations.py
│  │     │  │  │  ├─ test_linalg.py
│  │     │  │  │  ├─ test_regression.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ test_deprecations.cpython-313.pyc
│  │     │  │  │     ├─ test_linalg.cpython-313.pyc
│  │     │  │  │     ├─ test_regression.cpython-313.pyc
│  │     │  │  │     └─ __init__.cpython-313.pyc
│  │     │  │  ├─ _linalg.py
│  │     │  │  ├─ _linalg.pyi
│  │     │  │  ├─ _umath_linalg.cp313-win_amd64.lib
│  │     │  │  ├─ _umath_linalg.cp313-win_amd64.pyd
│  │     │  │  ├─ __init__.py
│  │     │  │  ├─ __init__.pyi
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ linalg.cpython-313.pyc
│  │     │  │     ├─ _linalg.cpython-313.pyc
│  │     │  │     └─ __init__.cpython-313.pyc
│  │     │  ├─ ma
│  │     │  │  ├─ API_CHANGES.txt
│  │     │  │  ├─ core.py
│  │     │  │  ├─ core.pyi
│  │     │  │  ├─ extras.py
│  │     │  │  ├─ extras.pyi
│  │     │  │  ├─ LICENSE
│  │     │  │  ├─ mrecords.py
│  │     │  │  ├─ mrecords.pyi
│  │     │  │  ├─ README.rst
│  │     │  │  ├─ tests
│  │     │  │  │  ├─ test_arrayobject.py
│  │     │  │  │  ├─ test_core.py
│  │     │  │  │  ├─ test_deprecations.py
│  │     │  │  │  ├─ test_extras.py
│  │     │  │  │  ├─ test_mrecords.py
│  │     │  │  │  ├─ test_old_ma.py
│  │     │  │  │  ├─ test_regression.py
│  │     │  │  │  ├─ test_subclassing.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ test_arrayobject.cpython-313.pyc
│  │     │  │  │     ├─ test_core.cpython-313.pyc
│  │     │  │  │     ├─ test_deprecations.cpython-313.pyc
│  │     │  │  │     ├─ test_extras.cpython-313.pyc
│  │     │  │  │     ├─ test_mrecords.cpython-313.pyc
│  │     │  │  │     ├─ test_old_ma.cpython-313.pyc
│  │     │  │  │     ├─ test_regression.cpython-313.pyc
│  │     │  │  │     ├─ test_subclassing.cpython-313.pyc
│  │     │  │  │     └─ __init__.cpython-313.pyc
│  │     │  │  ├─ testutils.py
│  │     │  │  ├─ timer_comparison.py
│  │     │  │  ├─ __init__.py
│  │     │  │  ├─ __init__.pyi
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ core.cpython-313.pyc
│  │     │  │     ├─ extras.cpython-313.pyc
│  │     │  │     ├─ mrecords.cpython-313.pyc
│  │     │  │     ├─ testutils.cpython-313.pyc
│  │     │  │     ├─ timer_comparison.cpython-313.pyc
│  │     │  │     └─ __init__.cpython-313.pyc
│  │     │  ├─ matlib.py
│  │     │  ├─ matrixlib
│  │     │  │  ├─ defmatrix.py
│  │     │  │  ├─ defmatrix.pyi
│  │     │  │  ├─ tests
│  │     │  │  │  ├─ test_defmatrix.py
│  │     │  │  │  ├─ test_interaction.py
│  │     │  │  │  ├─ test_masked_matrix.py
│  │     │  │  │  ├─ test_matrix_linalg.py
│  │     │  │  │  ├─ test_multiarray.py
│  │     │  │  │  ├─ test_numeric.py
│  │     │  │  │  ├─ test_regression.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ test_defmatrix.cpython-313.pyc
│  │     │  │  │     ├─ test_interaction.cpython-313.pyc
│  │     │  │  │     ├─ test_masked_matrix.cpython-313.pyc
│  │     │  │  │     ├─ test_matrix_linalg.cpython-313.pyc
│  │     │  │  │     ├─ test_multiarray.cpython-313.pyc
│  │     │  │  │     ├─ test_numeric.cpython-313.pyc
│  │     │  │  │     ├─ test_regression.cpython-313.pyc
│  │     │  │  │     └─ __init__.cpython-313.pyc
│  │     │  │  ├─ __init__.py
│  │     │  │  ├─ __init__.pyi
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ defmatrix.cpython-313.pyc
│  │     │  │     └─ __init__.cpython-313.pyc
│  │     │  ├─ polynomial
│  │     │  │  ├─ chebyshev.py
│  │     │  │  ├─ chebyshev.pyi
│  │     │  │  ├─ hermite.py
│  │     │  │  ├─ hermite.pyi
│  │     │  │  ├─ hermite_e.py
│  │     │  │  ├─ hermite_e.pyi
│  │     │  │  ├─ laguerre.py
│  │     │  │  ├─ laguerre.pyi
│  │     │  │  ├─ legendre.py
│  │     │  │  ├─ legendre.pyi
│  │     │  │  ├─ polynomial.py
│  │     │  │  ├─ polynomial.pyi
│  │     │  │  ├─ polyutils.py
│  │     │  │  ├─ polyutils.pyi
│  │     │  │  ├─ tests
│  │     │  │  │  ├─ test_chebyshev.py
│  │     │  │  │  ├─ test_classes.py
│  │     │  │  │  ├─ test_hermite.py
│  │     │  │  │  ├─ test_hermite_e.py
│  │     │  │  │  ├─ test_laguerre.py
│  │     │  │  │  ├─ test_legendre.py
│  │     │  │  │  ├─ test_polynomial.py
│  │     │  │  │  ├─ test_polyutils.py
│  │     │  │  │  ├─ test_printing.py
│  │     │  │  │  ├─ test_symbol.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ test_chebyshev.cpython-313.pyc
│  │     │  │  │     ├─ test_classes.cpython-313.pyc
│  │     │  │  │     ├─ test_hermite.cpython-313.pyc
│  │     │  │  │     ├─ test_hermite_e.cpython-313.pyc
│  │     │  │  │     ├─ test_laguerre.cpython-313.pyc
│  │     │  │  │     ├─ test_legendre.cpython-313.pyc
│  │     │  │  │     ├─ test_polynomial.cpython-313.pyc
│  │     │  │  │     ├─ test_polyutils.cpython-313.pyc
│  │     │  │  │     ├─ test_printing.cpython-313.pyc
│  │     │  │  │     ├─ test_symbol.cpython-313.pyc
│  │     │  │  │     └─ __init__.cpython-313.pyc
│  │     │  │  ├─ _polybase.py
│  │     │  │  ├─ _polybase.pyi
│  │     │  │  ├─ _polytypes.pyi
│  │     │  │  ├─ __init__.py
│  │     │  │  ├─ __init__.pyi
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ chebyshev.cpython-313.pyc
│  │     │  │     ├─ hermite.cpython-313.pyc
│  │     │  │     ├─ hermite_e.cpython-313.pyc
│  │     │  │     ├─ laguerre.cpython-313.pyc
│  │     │  │     ├─ legendre.cpython-313.pyc
│  │     │  │     ├─ polynomial.cpython-313.pyc
│  │     │  │     ├─ polyutils.cpython-313.pyc
│  │     │  │     ├─ _polybase.cpython-313.pyc
│  │     │  │     └─ __init__.cpython-313.pyc
│  │     │  ├─ py.typed
│  │     │  ├─ random
│  │     │  │  ├─ bit_generator.cp313-win_amd64.lib
│  │     │  │  ├─ bit_generator.cp313-win_amd64.pyd
│  │     │  │  ├─ bit_generator.pxd
│  │     │  │  ├─ bit_generator.pyi
│  │     │  │  ├─ c_distributions.pxd
│  │     │  │  ├─ lib
│  │     │  │  │  └─ npyrandom.lib
│  │     │  │  ├─ LICENSE.md
│  │     │  │  ├─ mtrand.cp313-win_amd64.lib
│  │     │  │  ├─ mtrand.cp313-win_amd64.pyd
│  │     │  │  ├─ mtrand.pyi
│  │     │  │  ├─ tests
│  │     │  │  │  ├─ data
│  │     │  │  │  │  ├─ generator_pcg64_np121.pkl.gz
│  │     │  │  │  │  ├─ generator_pcg64_np126.pkl.gz
│  │     │  │  │  │  ├─ mt19937-testset-1.csv
│  │     │  │  │  │  ├─ mt19937-testset-2.csv
│  │     │  │  │  │  ├─ pcg64-testset-1.csv
│  │     │  │  │  │  ├─ pcg64-testset-2.csv
│  │     │  │  │  │  ├─ pcg64dxsm-testset-1.csv
│  │     │  │  │  │  ├─ pcg64dxsm-testset-2.csv
│  │     │  │  │  │  ├─ philox-testset-1.csv
│  │     │  │  │  │  ├─ philox-testset-2.csv
│  │     │  │  │  │  ├─ sfc64-testset-1.csv
│  │     │  │  │  │  ├─ sfc64-testset-2.csv
│  │     │  │  │  │  ├─ sfc64_np126.pkl.gz
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  └─ __pycache__
│  │     │  │  │  │     └─ __init__.cpython-313.pyc
│  │     │  │  │  ├─ test_direct.py
│  │     │  │  │  ├─ test_extending.py
│  │     │  │  │  ├─ test_generator_mt19937.py
│  │     │  │  │  ├─ test_generator_mt19937_regressions.py
│  │     │  │  │  ├─ test_random.py
│  │     │  │  │  ├─ test_randomstate.py
│  │     │  │  │  ├─ test_randomstate_regression.py
│  │     │  │  │  ├─ test_regression.py
│  │     │  │  │  ├─ test_seed_sequence.py
│  │     │  │  │  ├─ test_smoke.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ test_direct.cpython-313.pyc
│  │     │  │  │     ├─ test_extending.cpython-313.pyc
│  │     │  │  │     ├─ test_generator_mt19937.cpython-313.pyc
│  │     │  │  │     ├─ test_generator_mt19937_regressions.cpython-313.pyc
│  │     │  │  │     ├─ test_random.cpython-313.pyc
│  │     │  │  │     ├─ test_randomstate.cpython-313.pyc
│  │     │  │  │     ├─ test_randomstate_regression.cpython-313.pyc
│  │     │  │  │     ├─ test_regression.cpython-313.pyc
│  │     │  │  │     ├─ test_seed_sequence.cpython-313.pyc
│  │     │  │  │     ├─ test_smoke.cpython-313.pyc
│  │     │  │  │     └─ __init__.cpython-313.pyc
│  │     │  │  ├─ _bounded_integers.cp313-win_amd64.lib
│  │     │  │  ├─ _bounded_integers.cp313-win_amd64.pyd
│  │     │  │  ├─ _bounded_integers.pxd
│  │     │  │  ├─ _common.cp313-win_amd64.lib
│  │     │  │  ├─ _common.cp313-win_amd64.pyd
│  │     │  │  ├─ _common.pxd
│  │     │  │  ├─ _examples
│  │     │  │  │  ├─ cffi
│  │     │  │  │  │  ├─ extending.py
│  │     │  │  │  │  ├─ parse.py
│  │     │  │  │  │  └─ __pycache__
│  │     │  │  │  │     ├─ extending.cpython-313.pyc
│  │     │  │  │  │     └─ parse.cpython-313.pyc
│  │     │  │  │  ├─ cython
│  │     │  │  │  │  ├─ extending.pyx
│  │     │  │  │  │  ├─ extending_distributions.pyx
│  │     │  │  │  │  └─ meson.build
│  │     │  │  │  └─ numba
│  │     │  │  │     ├─ extending.py
│  │     │  │  │     ├─ extending_distributions.py
│  │     │  │  │     └─ __pycache__
│  │     │  │  │        ├─ extending.cpython-313.pyc
│  │     │  │  │        └─ extending_distributions.cpython-313.pyc
│  │     │  │  ├─ _generator.cp313-win_amd64.lib
│  │     │  │  ├─ _generator.cp313-win_amd64.pyd
│  │     │  │  ├─ _generator.pyi
│  │     │  │  ├─ _mt19937.cp313-win_amd64.lib
│  │     │  │  ├─ _mt19937.cp313-win_amd64.pyd
│  │     │  │  ├─ _mt19937.pyi
│  │     │  │  ├─ _pcg64.cp313-win_amd64.lib
│  │     │  │  ├─ _pcg64.cp313-win_amd64.pyd
│  │     │  │  ├─ _pcg64.pyi
│  │     │  │  ├─ _philox.cp313-win_amd64.lib
│  │     │  │  ├─ _philox.cp313-win_amd64.pyd
│  │     │  │  ├─ _philox.pyi
│  │     │  │  ├─ _pickle.py
│  │     │  │  ├─ _sfc64.cp313-win_amd64.lib
│  │     │  │  ├─ _sfc64.cp313-win_amd64.pyd
│  │     │  │  ├─ _sfc64.pyi
│  │     │  │  ├─ __init__.pxd
│  │     │  │  ├─ __init__.py
│  │     │  │  ├─ __init__.pyi
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ _pickle.cpython-313.pyc
│  │     │  │     └─ __init__.cpython-313.pyc
│  │     │  ├─ rec
│  │     │  │  ├─ __init__.py
│  │     │  │  ├─ __init__.pyi
│  │     │  │  └─ __pycache__
│  │     │  │     └─ __init__.cpython-313.pyc
│  │     │  ├─ strings
│  │     │  │  ├─ __init__.py
│  │     │  │  ├─ __init__.pyi
│  │     │  │  └─ __pycache__
│  │     │  │     └─ __init__.cpython-313.pyc
│  │     │  ├─ testing
│  │     │  │  ├─ overrides.py
│  │     │  │  ├─ print_coercion_tables.py
│  │     │  │  ├─ tests
│  │     │  │  │  ├─ test_utils.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ test_utils.cpython-313.pyc
│  │     │  │  │     └─ __init__.cpython-313.pyc
│  │     │  │  ├─ _private
│  │     │  │  │  ├─ extbuild.py
│  │     │  │  │  ├─ utils.py
│  │     │  │  │  ├─ utils.pyi
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ extbuild.cpython-313.pyc
│  │     │  │  │     ├─ utils.cpython-313.pyc
│  │     │  │  │     └─ __init__.cpython-313.pyc
│  │     │  │  ├─ __init__.py
│  │     │  │  ├─ __init__.pyi
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ overrides.cpython-313.pyc
│  │     │  │     ├─ print_coercion_tables.cpython-313.pyc
│  │     │  │     └─ __init__.cpython-313.pyc
│  │     │  ├─ tests
│  │     │  │  ├─ test_configtool.py
│  │     │  │  ├─ test_ctypeslib.py
│  │     │  │  ├─ test_lazyloading.py
│  │     │  │  ├─ test_matlib.py
│  │     │  │  ├─ test_numpy_config.py
│  │     │  │  ├─ test_numpy_version.py
│  │     │  │  ├─ test_public_api.py
│  │     │  │  ├─ test_reloading.py
│  │     │  │  ├─ test_scripts.py
│  │     │  │  ├─ test_warnings.py
│  │     │  │  ├─ test__all__.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ test_configtool.cpython-313.pyc
│  │     │  │     ├─ test_ctypeslib.cpython-313.pyc
│  │     │  │     ├─ test_lazyloading.cpython-313.pyc
│  │     │  │     ├─ test_matlib.cpython-313.pyc
│  │     │  │     ├─ test_numpy_config.cpython-313.pyc
│  │     │  │     ├─ test_numpy_version.cpython-313.pyc
│  │     │  │     ├─ test_public_api.cpython-313.pyc
│  │     │  │     ├─ test_reloading.cpython-313.pyc
│  │     │  │     ├─ test_scripts.cpython-313.pyc
│  │     │  │     ├─ test_warnings.cpython-313.pyc
│  │     │  │     ├─ test__all__.cpython-313.pyc
│  │     │  │     └─ __init__.cpython-313.pyc
│  │     │  ├─ typing
│  │     │  │  ├─ mypy_plugin.py
│  │     │  │  ├─ tests
│  │     │  │  │  ├─ data
│  │     │  │  │  │  ├─ fail
│  │     │  │  │  │  │  ├─ arithmetic.pyi
│  │     │  │  │  │  │  ├─ arrayprint.pyi
│  │     │  │  │  │  │  ├─ arrayterator.pyi
│  │     │  │  │  │  │  ├─ array_constructors.pyi
│  │     │  │  │  │  │  ├─ array_like.pyi
│  │     │  │  │  │  │  ├─ array_pad.pyi
│  │     │  │  │  │  │  ├─ bitwise_ops.pyi
│  │     │  │  │  │  │  ├─ char.pyi
│  │     │  │  │  │  │  ├─ chararray.pyi
│  │     │  │  │  │  │  ├─ comparisons.pyi
│  │     │  │  │  │  │  ├─ constants.pyi
│  │     │  │  │  │  │  ├─ datasource.pyi
│  │     │  │  │  │  │  ├─ dtype.pyi
│  │     │  │  │  │  │  ├─ einsumfunc.pyi
│  │     │  │  │  │  │  ├─ flatiter.pyi
│  │     │  │  │  │  │  ├─ fromnumeric.pyi
│  │     │  │  │  │  │  ├─ histograms.pyi
│  │     │  │  │  │  │  ├─ index_tricks.pyi
│  │     │  │  │  │  │  ├─ lib_function_base.pyi
│  │     │  │  │  │  │  ├─ lib_polynomial.pyi
│  │     │  │  │  │  │  ├─ lib_utils.pyi
│  │     │  │  │  │  │  ├─ lib_version.pyi
│  │     │  │  │  │  │  ├─ linalg.pyi
│  │     │  │  │  │  │  ├─ memmap.pyi
│  │     │  │  │  │  │  ├─ modules.pyi
│  │     │  │  │  │  │  ├─ multiarray.pyi
│  │     │  │  │  │  │  ├─ ndarray.pyi
│  │     │  │  │  │  │  ├─ ndarray_misc.pyi
│  │     │  │  │  │  │  ├─ nditer.pyi
│  │     │  │  │  │  │  ├─ nested_sequence.pyi
│  │     │  │  │  │  │  ├─ npyio.pyi
│  │     │  │  │  │  │  ├─ numerictypes.pyi
│  │     │  │  │  │  │  ├─ random.pyi
│  │     │  │  │  │  │  ├─ rec.pyi
│  │     │  │  │  │  │  ├─ scalars.pyi
│  │     │  │  │  │  │  ├─ shape.pyi
│  │     │  │  │  │  │  ├─ shape_base.pyi
│  │     │  │  │  │  │  ├─ stride_tricks.pyi
│  │     │  │  │  │  │  ├─ strings.pyi
│  │     │  │  │  │  │  ├─ testing.pyi
│  │     │  │  │  │  │  ├─ twodim_base.pyi
│  │     │  │  │  │  │  ├─ type_check.pyi
│  │     │  │  │  │  │  ├─ ufunclike.pyi
│  │     │  │  │  │  │  ├─ ufuncs.pyi
│  │     │  │  │  │  │  ├─ ufunc_config.pyi
│  │     │  │  │  │  │  └─ warnings_and_errors.pyi
│  │     │  │  │  │  ├─ misc
│  │     │  │  │  │  │  └─ extended_precision.pyi
│  │     │  │  │  │  ├─ mypy.ini
│  │     │  │  │  │  ├─ pass
│  │     │  │  │  │  │  ├─ arithmetic.py
│  │     │  │  │  │  │  ├─ arrayprint.py
│  │     │  │  │  │  │  ├─ arrayterator.py
│  │     │  │  │  │  │  ├─ array_constructors.py
│  │     │  │  │  │  │  ├─ array_like.py
│  │     │  │  │  │  │  ├─ bitwise_ops.py
│  │     │  │  │  │  │  ├─ comparisons.py
│  │     │  │  │  │  │  ├─ dtype.py
│  │     │  │  │  │  │  ├─ einsumfunc.py
│  │     │  │  │  │  │  ├─ flatiter.py
│  │     │  │  │  │  │  ├─ fromnumeric.py
│  │     │  │  │  │  │  ├─ index_tricks.py
│  │     │  │  │  │  │  ├─ lib_utils.py
│  │     │  │  │  │  │  ├─ lib_version.py
│  │     │  │  │  │  │  ├─ literal.py
│  │     │  │  │  │  │  ├─ ma.py
│  │     │  │  │  │  │  ├─ mod.py
│  │     │  │  │  │  │  ├─ modules.py
│  │     │  │  │  │  │  ├─ multiarray.py
│  │     │  │  │  │  │  ├─ ndarray_conversion.py
│  │     │  │  │  │  │  ├─ ndarray_misc.py
│  │     │  │  │  │  │  ├─ ndarray_shape_manipulation.py
│  │     │  │  │  │  │  ├─ nditer.py
│  │     │  │  │  │  │  ├─ numeric.py
│  │     │  │  │  │  │  ├─ numerictypes.py
│  │     │  │  │  │  │  ├─ random.py
│  │     │  │  │  │  │  ├─ scalars.py
│  │     │  │  │  │  │  ├─ shape.py
│  │     │  │  │  │  │  ├─ simple.py
│  │     │  │  │  │  │  ├─ simple_py3.py
│  │     │  │  │  │  │  ├─ ufunclike.py
│  │     │  │  │  │  │  ├─ ufuncs.py
│  │     │  │  │  │  │  ├─ ufunc_config.py
│  │     │  │  │  │  │  ├─ warnings_and_errors.py
│  │     │  │  │  │  │  └─ __pycache__
│  │     │  │  │  │  │     ├─ arithmetic.cpython-313.pyc
│  │     │  │  │  │  │     ├─ arrayprint.cpython-313.pyc
│  │     │  │  │  │  │     ├─ arrayterator.cpython-313.pyc
│  │     │  │  │  │  │     ├─ array_constructors.cpython-313.pyc
│  │     │  │  │  │  │     ├─ array_like.cpython-313.pyc
│  │     │  │  │  │  │     ├─ bitwise_ops.cpython-313.pyc
│  │     │  │  │  │  │     ├─ comparisons.cpython-313.pyc
│  │     │  │  │  │  │     ├─ dtype.cpython-313.pyc
│  │     │  │  │  │  │     ├─ einsumfunc.cpython-313.pyc
│  │     │  │  │  │  │     ├─ flatiter.cpython-313.pyc
│  │     │  │  │  │  │     ├─ fromnumeric.cpython-313.pyc
│  │     │  │  │  │  │     ├─ index_tricks.cpython-313.pyc
│  │     │  │  │  │  │     ├─ lib_utils.cpython-313.pyc
│  │     │  │  │  │  │     ├─ lib_version.cpython-313.pyc
│  │     │  │  │  │  │     ├─ literal.cpython-313.pyc
│  │     │  │  │  │  │     ├─ ma.cpython-313.pyc
│  │     │  │  │  │  │     ├─ mod.cpython-313.pyc
│  │     │  │  │  │  │     ├─ modules.cpython-313.pyc
│  │     │  │  │  │  │     ├─ multiarray.cpython-313.pyc
│  │     │  │  │  │  │     ├─ ndarray_conversion.cpython-313.pyc
│  │     │  │  │  │  │     ├─ ndarray_misc.cpython-313.pyc
│  │     │  │  │  │  │     ├─ ndarray_shape_manipulation.cpython-313.pyc
│  │     │  │  │  │  │     ├─ nditer.cpython-313.pyc
│  │     │  │  │  │  │     ├─ numeric.cpython-313.pyc
│  │     │  │  │  │  │     ├─ numerictypes.cpython-313.pyc
│  │     │  │  │  │  │     ├─ random.cpython-313.pyc
│  │     │  │  │  │  │     ├─ scalars.cpython-313.pyc
│  │     │  │  │  │  │     ├─ shape.cpython-313.pyc
│  │     │  │  │  │  │     ├─ simple.cpython-313.pyc
│  │     │  │  │  │  │     ├─ simple_py3.cpython-313.pyc
│  │     │  │  │  │  │     ├─ ufunclike.cpython-313.pyc
│  │     │  │  │  │  │     ├─ ufuncs.cpython-313.pyc
│  │     │  │  │  │  │     ├─ ufunc_config.cpython-313.pyc
│  │     │  │  │  │  │     └─ warnings_and_errors.cpython-313.pyc
│  │     │  │  │  │  └─ reveal
│  │     │  │  │  │     ├─ arithmetic.pyi
│  │     │  │  │  │     ├─ arraypad.pyi
│  │     │  │  │  │     ├─ arrayprint.pyi
│  │     │  │  │  │     ├─ arraysetops.pyi
│  │     │  │  │  │     ├─ arrayterator.pyi
│  │     │  │  │  │     ├─ array_api_info.pyi
│  │     │  │  │  │     ├─ array_constructors.pyi
│  │     │  │  │  │     ├─ bitwise_ops.pyi
│  │     │  │  │  │     ├─ char.pyi
│  │     │  │  │  │     ├─ chararray.pyi
│  │     │  │  │  │     ├─ comparisons.pyi
│  │     │  │  │  │     ├─ constants.pyi
│  │     │  │  │  │     ├─ ctypeslib.pyi
│  │     │  │  │  │     ├─ datasource.pyi
│  │     │  │  │  │     ├─ dtype.pyi
│  │     │  │  │  │     ├─ einsumfunc.pyi
│  │     │  │  │  │     ├─ emath.pyi
│  │     │  │  │  │     ├─ false_positives.pyi
│  │     │  │  │  │     ├─ fft.pyi
│  │     │  │  │  │     ├─ flatiter.pyi
│  │     │  │  │  │     ├─ fromnumeric.pyi
│  │     │  │  │  │     ├─ getlimits.pyi
│  │     │  │  │  │     ├─ histograms.pyi
│  │     │  │  │  │     ├─ index_tricks.pyi
│  │     │  │  │  │     ├─ lib_function_base.pyi
│  │     │  │  │  │     ├─ lib_polynomial.pyi
│  │     │  │  │  │     ├─ lib_utils.pyi
│  │     │  │  │  │     ├─ lib_version.pyi
│  │     │  │  │  │     ├─ linalg.pyi
│  │     │  │  │  │     ├─ matrix.pyi
│  │     │  │  │  │     ├─ memmap.pyi
│  │     │  │  │  │     ├─ mod.pyi
│  │     │  │  │  │     ├─ modules.pyi
│  │     │  │  │  │     ├─ multiarray.pyi
│  │     │  │  │  │     ├─ nbit_base_example.pyi
│  │     │  │  │  │     ├─ ndarray_assignability.pyi
│  │     │  │  │  │     ├─ ndarray_conversion.pyi
│  │     │  │  │  │     ├─ ndarray_misc.pyi
│  │     │  │  │  │     ├─ ndarray_shape_manipulation.pyi
│  │     │  │  │  │     ├─ nditer.pyi
│  │     │  │  │  │     ├─ nested_sequence.pyi
│  │     │  │  │  │     ├─ npyio.pyi
│  │     │  │  │  │     ├─ numeric.pyi
│  │     │  │  │  │     ├─ numerictypes.pyi
│  │     │  │  │  │     ├─ polynomial_polybase.pyi
│  │     │  │  │  │     ├─ polynomial_polyutils.pyi
│  │     │  │  │  │     ├─ polynomial_series.pyi
│  │     │  │  │  │     ├─ random.pyi
│  │     │  │  │  │     ├─ rec.pyi
│  │     │  │  │  │     ├─ scalars.pyi
│  │     │  │  │  │     ├─ shape.pyi
│  │     │  │  │  │     ├─ shape_base.pyi
│  │     │  │  │  │     ├─ stride_tricks.pyi
│  │     │  │  │  │     ├─ strings.pyi
│  │     │  │  │  │     ├─ testing.pyi
│  │     │  │  │  │     ├─ twodim_base.pyi
│  │     │  │  │  │     ├─ type_check.pyi
│  │     │  │  │  │     ├─ ufunclike.pyi
│  │     │  │  │  │     ├─ ufuncs.pyi
│  │     │  │  │  │     ├─ ufunc_config.pyi
│  │     │  │  │  │     └─ warnings_and_errors.pyi
│  │     │  │  │  ├─ test_isfile.py
│  │     │  │  │  ├─ test_runtime.py
│  │     │  │  │  ├─ test_typing.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ test_isfile.cpython-313.pyc
│  │     │  │  │     ├─ test_runtime.cpython-313.pyc
│  │     │  │  │     ├─ test_typing.cpython-313.pyc
│  │     │  │  │     └─ __init__.cpython-313.pyc
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ mypy_plugin.cpython-313.pyc
│  │     │  │     └─ __init__.cpython-313.pyc
│  │     │  ├─ version.py
│  │     │  ├─ version.pyi
│  │     │  ├─ _array_api_info.py
│  │     │  ├─ _array_api_info.pyi
│  │     │  ├─ _configtool.py
│  │     │  ├─ _core
│  │     │  │  ├─ arrayprint.py
│  │     │  │  ├─ arrayprint.pyi
│  │     │  │  ├─ cversions.py
│  │     │  │  ├─ defchararray.py
│  │     │  │  ├─ defchararray.pyi
│  │     │  │  ├─ einsumfunc.py
│  │     │  │  ├─ einsumfunc.pyi
│  │     │  │  ├─ fromnumeric.py
│  │     │  │  ├─ fromnumeric.pyi
│  │     │  │  ├─ function_base.py
│  │     │  │  ├─ function_base.pyi
│  │     │  │  ├─ getlimits.py
│  │     │  │  ├─ getlimits.pyi
│  │     │  │  ├─ include
│  │     │  │  │  └─ numpy
│  │     │  │  │     ├─ arrayobject.h
│  │     │  │  │     ├─ arrayscalars.h
│  │     │  │  │     ├─ dtype_api.h
│  │     │  │  │     ├─ halffloat.h
│  │     │  │  │     ├─ ndarrayobject.h
│  │     │  │  │     ├─ ndarraytypes.h
│  │     │  │  │     ├─ npy_1_7_deprecated_api.h
│  │     │  │  │     ├─ npy_2_compat.h
│  │     │  │  │     ├─ npy_2_complexcompat.h
│  │     │  │  │     ├─ npy_3kcompat.h
│  │     │  │  │     ├─ npy_common.h
│  │     │  │  │     ├─ npy_cpu.h
│  │     │  │  │     ├─ npy_endian.h
│  │     │  │  │     ├─ npy_math.h
│  │     │  │  │     ├─ npy_no_deprecated_api.h
│  │     │  │  │     ├─ npy_os.h
│  │     │  │  │     ├─ numpyconfig.h
│  │     │  │  │     ├─ random
│  │     │  │  │     │  ├─ bitgen.h
│  │     │  │  │     │  ├─ distributions.h
│  │     │  │  │     │  ├─ libdivide.h
│  │     │  │  │     │  └─ LICENSE.txt
│  │     │  │  │     ├─ ufuncobject.h
│  │     │  │  │     ├─ utils.h
│  │     │  │  │     ├─ _neighborhood_iterator_imp.h
│  │     │  │  │     ├─ _numpyconfig.h
│  │     │  │  │     ├─ _public_dtype_api_table.h
│  │     │  │  │     ├─ __multiarray_api.c
│  │     │  │  │     ├─ __multiarray_api.h
│  │     │  │  │     ├─ __ufunc_api.c
│  │     │  │  │     └─ __ufunc_api.h
│  │     │  │  ├─ lib
│  │     │  │  │  ├─ npy-pkg-config
│  │     │  │  │  │  ├─ mlib.ini
│  │     │  │  │  │  └─ npymath.ini
│  │     │  │  │  ├─ npymath.lib
│  │     │  │  │  └─ pkgconfig
│  │     │  │  │     └─ numpy.pc
│  │     │  │  ├─ memmap.py
│  │     │  │  ├─ memmap.pyi
│  │     │  │  ├─ multiarray.py
│  │     │  │  ├─ multiarray.pyi
│  │     │  │  ├─ numeric.py
│  │     │  │  ├─ numeric.pyi
│  │     │  │  ├─ numerictypes.py
│  │     │  │  ├─ numerictypes.pyi
│  │     │  │  ├─ overrides.py
│  │     │  │  ├─ printoptions.py
│  │     │  │  ├─ records.py
│  │     │  │  ├─ records.pyi
│  │     │  │  ├─ shape_base.py
│  │     │  │  ├─ shape_base.pyi
│  │     │  │  ├─ strings.py
│  │     │  │  ├─ strings.pyi
│  │     │  │  ├─ tests
│  │     │  │  │  ├─ data
│  │     │  │  │  │  ├─ astype_copy.pkl
│  │     │  │  │  │  ├─ generate_umath_validation_data.cpp
│  │     │  │  │  │  ├─ recarray_from_file.fits
│  │     │  │  │  │  ├─ umath-validation-set-arccos.csv
│  │     │  │  │  │  ├─ umath-validation-set-arccosh.csv
│  │     │  │  │  │  ├─ umath-validation-set-arcsin.csv
│  │     │  │  │  │  ├─ umath-validation-set-arcsinh.csv
│  │     │  │  │  │  ├─ umath-validation-set-arctan.csv
│  │     │  │  │  │  ├─ umath-validation-set-arctanh.csv
│  │     │  │  │  │  ├─ umath-validation-set-cbrt.csv
│  │     │  │  │  │  ├─ umath-validation-set-cos.csv
│  │     │  │  │  │  ├─ umath-validation-set-cosh.csv
│  │     │  │  │  │  ├─ umath-validation-set-exp.csv
│  │     │  │  │  │  ├─ umath-validation-set-exp2.csv
│  │     │  │  │  │  ├─ umath-validation-set-expm1.csv
│  │     │  │  │  │  ├─ umath-validation-set-log.csv
│  │     │  │  │  │  ├─ umath-validation-set-log10.csv
│  │     │  │  │  │  ├─ umath-validation-set-log1p.csv
│  │     │  │  │  │  ├─ umath-validation-set-log2.csv
│  │     │  │  │  │  ├─ umath-validation-set-README.txt
│  │     │  │  │  │  ├─ umath-validation-set-sin.csv
│  │     │  │  │  │  ├─ umath-validation-set-sinh.csv
│  │     │  │  │  │  ├─ umath-validation-set-tan.csv
│  │     │  │  │  │  └─ umath-validation-set-tanh.csv
│  │     │  │  │  ├─ examples
│  │     │  │  │  │  ├─ cython
│  │     │  │  │  │  │  ├─ checks.pyx
│  │     │  │  │  │  │  ├─ meson.build
│  │     │  │  │  │  │  ├─ setup.py
│  │     │  │  │  │  │  └─ __pycache__
│  │     │  │  │  │  │     └─ setup.cpython-313.pyc
│  │     │  │  │  │  └─ limited_api
│  │     │  │  │  │     ├─ limited_api1.c
│  │     │  │  │  │     ├─ limited_api2.pyx
│  │     │  │  │  │     ├─ limited_api_latest.c
│  │     │  │  │  │     ├─ meson.build
│  │     │  │  │  │     ├─ setup.py
│  │     │  │  │  │     └─ __pycache__
│  │     │  │  │  │        └─ setup.cpython-313.pyc
│  │     │  │  │  ├─ test_abc.py
│  │     │  │  │  ├─ test_api.py
│  │     │  │  │  ├─ test_argparse.py
│  │     │  │  │  ├─ test_arraymethod.py
│  │     │  │  │  ├─ test_arrayobject.py
│  │     │  │  │  ├─ test_arrayprint.py
│  │     │  │  │  ├─ test_array_api_info.py
│  │     │  │  │  ├─ test_array_coercion.py
│  │     │  │  │  ├─ test_array_interface.py
│  │     │  │  │  ├─ test_casting_floatingpoint_errors.py
│  │     │  │  │  ├─ test_casting_unittests.py
│  │     │  │  │  ├─ test_conversion_utils.py
│  │     │  │  │  ├─ test_cpu_dispatcher.py
│  │     │  │  │  ├─ test_cpu_features.py
│  │     │  │  │  ├─ test_custom_dtypes.py
│  │     │  │  │  ├─ test_cython.py
│  │     │  │  │  ├─ test_datetime.py
│  │     │  │  │  ├─ test_defchararray.py
│  │     │  │  │  ├─ test_deprecations.py
│  │     │  │  │  ├─ test_dlpack.py
│  │     │  │  │  ├─ test_dtype.py
│  │     │  │  │  ├─ test_einsum.py
│  │     │  │  │  ├─ test_errstate.py
│  │     │  │  │  ├─ test_extint128.py
│  │     │  │  │  ├─ test_function_base.py
│  │     │  │  │  ├─ test_getlimits.py
│  │     │  │  │  ├─ test_half.py
│  │     │  │  │  ├─ test_hashtable.py
│  │     │  │  │  ├─ test_indexerrors.py
│  │     │  │  │  ├─ test_indexing.py
│  │     │  │  │  ├─ test_item_selection.py
│  │     │  │  │  ├─ test_limited_api.py
│  │     │  │  │  ├─ test_longdouble.py
│  │     │  │  │  ├─ test_machar.py
│  │     │  │  │  ├─ test_memmap.py
│  │     │  │  │  ├─ test_mem_overlap.py
│  │     │  │  │  ├─ test_mem_policy.py
│  │     │  │  │  ├─ test_multiarray.py
│  │     │  │  │  ├─ test_multithreading.py
│  │     │  │  │  ├─ test_nditer.py
│  │     │  │  │  ├─ test_nep50_promotions.py
│  │     │  │  │  ├─ test_numeric.py
│  │     │  │  │  ├─ test_numerictypes.py
│  │     │  │  │  ├─ test_overrides.py
│  │     │  │  │  ├─ test_print.py
│  │     │  │  │  ├─ test_protocols.py
│  │     │  │  │  ├─ test_records.py
│  │     │  │  │  ├─ test_regression.py
│  │     │  │  │  ├─ test_scalarbuffer.py
│  │     │  │  │  ├─ test_scalarinherit.py
│  │     │  │  │  ├─ test_scalarmath.py
│  │     │  │  │  ├─ test_scalarprint.py
│  │     │  │  │  ├─ test_scalar_ctors.py
│  │     │  │  │  ├─ test_scalar_methods.py
│  │     │  │  │  ├─ test_shape_base.py
│  │     │  │  │  ├─ test_simd.py
│  │     │  │  │  ├─ test_simd_module.py
│  │     │  │  │  ├─ test_stringdtype.py
│  │     │  │  │  ├─ test_strings.py
│  │     │  │  │  ├─ test_ufunc.py
│  │     │  │  │  ├─ test_umath.py
│  │     │  │  │  ├─ test_umath_accuracy.py
│  │     │  │  │  ├─ test_umath_complex.py
│  │     │  │  │  ├─ test_unicode.py
│  │     │  │  │  ├─ test__exceptions.py
│  │     │  │  │  ├─ _locales.py
│  │     │  │  │  ├─ _natype.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ test_abc.cpython-313.pyc
│  │     │  │  │     ├─ test_api.cpython-313.pyc
│  │     │  │  │     ├─ test_argparse.cpython-313.pyc
│  │     │  │  │     ├─ test_arraymethod.cpython-313.pyc
│  │     │  │  │     ├─ test_arrayobject.cpython-313.pyc
│  │     │  │  │     ├─ test_arrayprint.cpython-313.pyc
│  │     │  │  │     ├─ test_array_api_info.cpython-313.pyc
│  │     │  │  │     ├─ test_array_coercion.cpython-313.pyc
│  │     │  │  │     ├─ test_array_interface.cpython-313.pyc
│  │     │  │  │     ├─ test_casting_floatingpoint_errors.cpython-313.pyc
│  │     │  │  │     ├─ test_casting_unittests.cpython-313.pyc
│  │     │  │  │     ├─ test_conversion_utils.cpython-313.pyc
│  │     │  │  │     ├─ test_cpu_dispatcher.cpython-313.pyc
│  │     │  │  │     ├─ test_cpu_features.cpython-313.pyc
│  │     │  │  │     ├─ test_custom_dtypes.cpython-313.pyc
│  │     │  │  │     ├─ test_cython.cpython-313.pyc
│  │     │  │  │     ├─ test_datetime.cpython-313.pyc
│  │     │  │  │     ├─ test_defchararray.cpython-313.pyc
│  │     │  │  │     ├─ test_deprecations.cpython-313.pyc
│  │     │  │  │     ├─ test_dlpack.cpython-313.pyc
│  │     │  │  │     ├─ test_dtype.cpython-313.pyc
│  │     │  │  │     ├─ test_einsum.cpython-313.pyc
│  │     │  │  │     ├─ test_errstate.cpython-313.pyc
│  │     │  │  │     ├─ test_extint128.cpython-313.pyc
│  │     │  │  │     ├─ test_function_base.cpython-313.pyc
│  │     │  │  │     ├─ test_getlimits.cpython-313.pyc
│  │     │  │  │     ├─ test_half.cpython-313.pyc
│  │     │  │  │     ├─ test_hashtable.cpython-313.pyc
│  │     │  │  │     ├─ test_indexerrors.cpython-313.pyc
│  │     │  │  │     ├─ test_indexing.cpython-313.pyc
│  │     │  │  │     ├─ test_item_selection.cpython-313.pyc
│  │     │  │  │     ├─ test_limited_api.cpython-313.pyc
│  │     │  │  │     ├─ test_longdouble.cpython-313.pyc
│  │     │  │  │     ├─ test_machar.cpython-313.pyc
│  │     │  │  │     ├─ test_memmap.cpython-313.pyc
│  │     │  │  │     ├─ test_mem_overlap.cpython-313.pyc
│  │     │  │  │     ├─ test_mem_policy.cpython-313.pyc
│  │     │  │  │     ├─ test_multiarray.cpython-313.pyc
│  │     │  │  │     ├─ test_multithreading.cpython-313.pyc
│  │     │  │  │     ├─ test_nditer.cpython-313.pyc
│  │     │  │  │     ├─ test_nep50_promotions.cpython-313.pyc
│  │     │  │  │     ├─ test_numeric.cpython-313.pyc
│  │     │  │  │     ├─ test_numerictypes.cpython-313.pyc
│  │     │  │  │     ├─ test_overrides.cpython-313.pyc
│  │     │  │  │     ├─ test_print.cpython-313.pyc
│  │     │  │  │     ├─ test_protocols.cpython-313.pyc
│  │     │  │  │     ├─ test_records.cpython-313.pyc
│  │     │  │  │     ├─ test_regression.cpython-313.pyc
│  │     │  │  │     ├─ test_scalarbuffer.cpython-313.pyc
│  │     │  │  │     ├─ test_scalarinherit.cpython-313.pyc
│  │     │  │  │     ├─ test_scalarmath.cpython-313.pyc
│  │     │  │  │     ├─ test_scalarprint.cpython-313.pyc
│  │     │  │  │     ├─ test_scalar_ctors.cpython-313.pyc
│  │     │  │  │     ├─ test_scalar_methods.cpython-313.pyc
│  │     │  │  │     ├─ test_shape_base.cpython-313.pyc
│  │     │  │  │     ├─ test_simd.cpython-313.pyc
│  │     │  │  │     ├─ test_simd_module.cpython-313.pyc
│  │     │  │  │     ├─ test_stringdtype.cpython-313.pyc
│  │     │  │  │     ├─ test_strings.cpython-313.pyc
│  │     │  │  │     ├─ test_ufunc.cpython-313.pyc
│  │     │  │  │     ├─ test_umath.cpython-313.pyc
│  │     │  │  │     ├─ test_umath_accuracy.cpython-313.pyc
│  │     │  │  │     ├─ test_umath_complex.cpython-313.pyc
│  │     │  │  │     ├─ test_unicode.cpython-313.pyc
│  │     │  │  │     ├─ test__exceptions.cpython-313.pyc
│  │     │  │  │     ├─ _locales.cpython-313.pyc
│  │     │  │  │     └─ _natype.cpython-313.pyc
│  │     │  │  ├─ umath.py
│  │     │  │  ├─ _add_newdocs.py
│  │     │  │  ├─ _add_newdocs_scalars.py
│  │     │  │  ├─ _asarray.py
│  │     │  │  ├─ _asarray.pyi
│  │     │  │  ├─ _dtype.py
│  │     │  │  ├─ _dtype_ctypes.py
│  │     │  │  ├─ _exceptions.py
│  │     │  │  ├─ _internal.py
│  │     │  │  ├─ _internal.pyi
│  │     │  │  ├─ _machar.py
│  │     │  │  ├─ _methods.py
│  │     │  │  ├─ _multiarray_tests.cp313-win_amd64.lib
│  │     │  │  ├─ _multiarray_tests.cp313-win_amd64.pyd
│  │     │  │  ├─ _multiarray_umath.cp313-win_amd64.lib
│  │     │  │  ├─ _multiarray_umath.cp313-win_amd64.pyd
│  │     │  │  ├─ _operand_flag_tests.cp313-win_amd64.lib
│  │     │  │  ├─ _operand_flag_tests.cp313-win_amd64.pyd
│  │     │  │  ├─ _rational_tests.cp313-win_amd64.lib
│  │     │  │  ├─ _rational_tests.cp313-win_amd64.pyd
│  │     │  │  ├─ _simd.cp313-win_amd64.lib
│  │     │  │  ├─ _simd.cp313-win_amd64.pyd
│  │     │  │  ├─ _string_helpers.py
│  │     │  │  ├─ _struct_ufunc_tests.cp313-win_amd64.lib
│  │     │  │  ├─ _struct_ufunc_tests.cp313-win_amd64.pyd
│  │     │  │  ├─ _type_aliases.py
│  │     │  │  ├─ _type_aliases.pyi
│  │     │  │  ├─ _ufunc_config.py
│  │     │  │  ├─ _ufunc_config.pyi
│  │     │  │  ├─ _umath_tests.cp313-win_amd64.lib
│  │     │  │  ├─ _umath_tests.cp313-win_amd64.pyd
│  │     │  │  ├─ __init__.py
│  │     │  │  ├─ __init__.pyi
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ arrayprint.cpython-313.pyc
│  │     │  │     ├─ cversions.cpython-313.pyc
│  │     │  │     ├─ defchararray.cpython-313.pyc
│  │     │  │     ├─ einsumfunc.cpython-313.pyc
│  │     │  │     ├─ fromnumeric.cpython-313.pyc
│  │     │  │     ├─ function_base.cpython-313.pyc
│  │     │  │     ├─ getlimits.cpython-313.pyc
│  │     │  │     ├─ memmap.cpython-313.pyc
│  │     │  │     ├─ multiarray.cpython-313.pyc
│  │     │  │     ├─ numeric.cpython-313.pyc
│  │     │  │     ├─ numerictypes.cpython-313.pyc
│  │     │  │     ├─ overrides.cpython-313.pyc
│  │     │  │     ├─ printoptions.cpython-313.pyc
│  │     │  │     ├─ records.cpython-313.pyc
│  │     │  │     ├─ shape_base.cpython-313.pyc
│  │     │  │     ├─ strings.cpython-313.pyc
│  │     │  │     ├─ umath.cpython-313.pyc
│  │     │  │     ├─ _add_newdocs.cpython-313.pyc
│  │     │  │     ├─ _add_newdocs_scalars.cpython-313.pyc
│  │     │  │     ├─ _asarray.cpython-313.pyc
│  │     │  │     ├─ _dtype.cpython-313.pyc
│  │     │  │     ├─ _dtype_ctypes.cpython-313.pyc
│  │     │  │     ├─ _exceptions.cpython-313.pyc
│  │     │  │     ├─ _internal.cpython-313.pyc
│  │     │  │     ├─ _machar.cpython-313.pyc
│  │     │  │     ├─ _methods.cpython-313.pyc
│  │     │  │     ├─ _string_helpers.cpython-313.pyc
│  │     │  │     ├─ _type_aliases.cpython-313.pyc
│  │     │  │     ├─ _ufunc_config.cpython-313.pyc
│  │     │  │     └─ __init__.cpython-313.pyc
│  │     │  ├─ _distributor_init.py
│  │     │  ├─ _expired_attrs_2_0.py
│  │     │  ├─ _globals.py
│  │     │  ├─ _pyinstaller
│  │     │  │  ├─ hook-numpy.py
│  │     │  │  ├─ tests
│  │     │  │  │  ├─ pyinstaller-smoke.py
│  │     │  │  │  ├─ test_pyinstaller.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ pyinstaller-smoke.cpython-313.pyc
│  │     │  │  │     ├─ test_pyinstaller.cpython-313.pyc
│  │     │  │  │     └─ __init__.cpython-313.pyc
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ hook-numpy.cpython-313.pyc
│  │     │  │     └─ __init__.cpython-313.pyc
│  │     │  ├─ _pytesttester.py
│  │     │  ├─ _pytesttester.pyi
│  │     │  ├─ _typing
│  │     │  │  ├─ _add_docstring.py
│  │     │  │  ├─ _array_like.py
│  │     │  │  ├─ _callable.pyi
│  │     │  │  ├─ _char_codes.py
│  │     │  │  ├─ _dtype_like.py
│  │     │  │  ├─ _extended_precision.py
│  │     │  │  ├─ _nbit.py
│  │     │  │  ├─ _nbit_base.py
│  │     │  │  ├─ _nested_sequence.py
│  │     │  │  ├─ _scalars.py
│  │     │  │  ├─ _shape.py
│  │     │  │  ├─ _ufunc.py
│  │     │  │  ├─ _ufunc.pyi
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ _add_docstring.cpython-313.pyc
│  │     │  │     ├─ _array_like.cpython-313.pyc
│  │     │  │     ├─ _char_codes.cpython-313.pyc
│  │     │  │     ├─ _dtype_like.cpython-313.pyc
│  │     │  │     ├─ _extended_precision.cpython-313.pyc
│  │     │  │     ├─ _nbit.cpython-313.pyc
│  │     │  │     ├─ _nbit_base.cpython-313.pyc
│  │     │  │     ├─ _nested_sequence.cpython-313.pyc
│  │     │  │     ├─ _scalars.cpython-313.pyc
│  │     │  │     ├─ _shape.cpython-313.pyc
│  │     │  │     ├─ _ufunc.cpython-313.pyc
│  │     │  │     └─ __init__.cpython-313.pyc
│  │     │  ├─ _utils
│  │     │  │  ├─ _convertions.py
│  │     │  │  ├─ _inspect.py
│  │     │  │  ├─ _pep440.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ _convertions.cpython-313.pyc
│  │     │  │     ├─ _inspect.cpython-313.pyc
│  │     │  │     ├─ _pep440.cpython-313.pyc
│  │     │  │     └─ __init__.cpython-313.pyc
│  │     │  ├─ __config__.py
│  │     │  ├─ __config__.pyi
│  │     │  ├─ __init__.cython-30.pxd
│  │     │  ├─ __init__.pxd
│  │     │  ├─ __init__.py
│  │     │  ├─ __init__.pyi
│  │     │  └─ __pycache__
│  │     │     ├─ conftest.cpython-313.pyc
│  │     │     ├─ ctypeslib.cpython-313.pyc
│  │     │     ├─ dtypes.cpython-313.pyc
│  │     │     ├─ exceptions.cpython-313.pyc
│  │     │     ├─ matlib.cpython-313.pyc
│  │     │     ├─ version.cpython-313.pyc
│  │     │     ├─ _array_api_info.cpython-313.pyc
│  │     │     ├─ _configtool.cpython-313.pyc
│  │     │     ├─ _distributor_init.cpython-313.pyc
│  │     │     ├─ _expired_attrs_2_0.cpython-313.pyc
│  │     │     ├─ _globals.cpython-313.pyc
│  │     │     ├─ _pytesttester.cpython-313.pyc
│  │     │     ├─ __config__.cpython-313.pyc
│  │     │     └─ __init__.cpython-313.pyc
│  │     ├─ numpy-2.2.1-cp313-cp313-win_amd64.whl
│  │     ├─ numpy-2.2.1.dist-info
│  │     │  ├─ DELVEWHEEL
│  │     │  ├─ entry_points.txt
│  │     │  ├─ INSTALLER
│  │     │  ├─ LICENSE.txt
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  ├─ REQUESTED
│  │     │  └─ WHEEL
│  │     ├─ numpy.libs
│  │     │  ├─ libscipy_openblas64_-43e11ff0749b8cbe0a615c9cf6737e0e.dll
│  │     │  └─ msvcp140-d64049c6e3865410a7dda6a7e9f0c575.dll
│  │     ├─ opencv_contrib_python-4.13.0.92.dist-info
│  │     │  ├─ INSTALLER
│  │     │  ├─ LICENSE-3RD-PARTY.txt
│  │     │  ├─ LICENSE.txt
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  ├─ top_level.txt
│  │     │  └─ WHEEL
│  │     ├─ opencv_python_headless-4.10.0.84.dist-info
│  │     │  ├─ INSTALLER
│  │     │  ├─ LICENSE-3RD-PARTY.txt
│  │     │  ├─ LICENSE.txt
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  ├─ REQUESTED
│  │     │  ├─ top_level.txt
│  │     │  └─ WHEEL
│  │     ├─ packaging
│  │     │  ├─ licenses
│  │     │  │  ├─ _spdx.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ _spdx.cpython-313.pyc
│  │     │  │     └─ __init__.cpython-313.pyc
│  │     │  ├─ markers.py
│  │     │  ├─ metadata.py
│  │     │  ├─ py.typed
│  │     │  ├─ pylock.py
│  │     │  ├─ requirements.py
│  │     │  ├─ specifiers.py
│  │     │  ├─ tags.py
│  │     │  ├─ utils.py
│  │     │  ├─ version.py
│  │     │  ├─ _elffile.py
│  │     │  ├─ _manylinux.py
│  │     │  ├─ _musllinux.py
│  │     │  ├─ _parser.py
│  │     │  ├─ _structures.py
│  │     │  ├─ _tokenizer.py
│  │     │  ├─ __init__.py
│  │     │  └─ __pycache__
│  │     │     ├─ markers.cpython-313.pyc
│  │     │     ├─ metadata.cpython-313.pyc
│  │     │     ├─ pylock.cpython-313.pyc
│  │     │     ├─ requirements.cpython-313.pyc
│  │     │     ├─ specifiers.cpython-313.pyc
│  │     │     ├─ tags.cpython-313.pyc
│  │     │     ├─ utils.cpython-313.pyc
│  │     │     ├─ version.cpython-313.pyc
│  │     │     ├─ _elffile.cpython-313.pyc
│  │     │     ├─ _manylinux.cpython-313.pyc
│  │     │     ├─ _musllinux.cpython-313.pyc
│  │     │     ├─ _parser.cpython-313.pyc
│  │     │     ├─ _structures.cpython-313.pyc
│  │     │     ├─ _tokenizer.cpython-313.pyc
│  │     │     └─ __init__.cpython-313.pyc
│  │     ├─ packaging-26.0.dist-info
│  │     │  ├─ INSTALLER
│  │     │  ├─ licenses
│  │     │  │  ├─ LICENSE
│  │     │  │  ├─ LICENSE.APACHE
│  │     │  │  └─ LICENSE.BSD
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  └─ WHEEL
│  │     ├─ past
│  │     │  ├─ builtins
│  │     │  │  ├─ misc.py
│  │     │  │  ├─ noniterators.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ misc.cpython-313.pyc
│  │     │  │     ├─ noniterators.cpython-313.pyc
│  │     │  │     └─ __init__.cpython-313.pyc
│  │     │  ├─ translation
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     └─ __init__.cpython-313.pyc
│  │     │  ├─ types
│  │     │  │  ├─ basestring.py
│  │     │  │  ├─ olddict.py
│  │     │  │  ├─ oldstr.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ basestring.cpython-313.pyc
│  │     │  │     ├─ olddict.cpython-313.pyc
│  │     │  │     ├─ oldstr.cpython-313.pyc
│  │     │  │     └─ __init__.cpython-313.pyc
│  │     │  ├─ utils
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     └─ __init__.cpython-313.pyc
│  │     │  ├─ __init__.py
│  │     │  └─ __pycache__
│  │     │     └─ __init__.cpython-313.pyc
│  │     ├─ pgvector
│  │     │  ├─ asyncpg
│  │     │  │  ├─ register.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ register.cpython-313.pyc
│  │     │  │     └─ __init__.cpython-313.pyc
│  │     │  ├─ django
│  │     │  │  ├─ bit.py
│  │     │  │  ├─ extensions.py
│  │     │  │  ├─ functions.py
│  │     │  │  ├─ halfvec.py
│  │     │  │  ├─ indexes.py
│  │     │  │  ├─ sparsevec.py
│  │     │  │  ├─ vector.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ bit.cpython-313.pyc
│  │     │  │     ├─ extensions.cpython-313.pyc
│  │     │  │     ├─ functions.cpython-313.pyc
│  │     │  │     ├─ halfvec.cpython-313.pyc
│  │     │  │     ├─ indexes.cpython-313.pyc
│  │     │  │     ├─ sparsevec.cpython-313.pyc
│  │     │  │     ├─ vector.cpython-313.pyc
│  │     │  │     └─ __init__.cpython-313.pyc
│  │     │  ├─ peewee
│  │     │  │  ├─ bit.py
│  │     │  │  ├─ halfvec.py
│  │     │  │  ├─ sparsevec.py
│  │     │  │  ├─ vector.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ bit.cpython-313.pyc
│  │     │  │     ├─ halfvec.cpython-313.pyc
│  │     │  │     ├─ sparsevec.cpython-313.pyc
│  │     │  │     ├─ vector.cpython-313.pyc
│  │     │  │     └─ __init__.cpython-313.pyc
│  │     │  ├─ psycopg
│  │     │  │  ├─ bit.py
│  │     │  │  ├─ halfvec.py
│  │     │  │  ├─ register.py
│  │     │  │  ├─ sparsevec.py
│  │     │  │  ├─ vector.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ bit.cpython-313.pyc
│  │     │  │     ├─ halfvec.cpython-313.pyc
│  │     │  │     ├─ register.cpython-313.pyc
│  │     │  │     ├─ sparsevec.cpython-313.pyc
│  │     │  │     ├─ vector.cpython-313.pyc
│  │     │  │     └─ __init__.cpython-313.pyc
│  │     │  ├─ psycopg2
│  │     │  │  ├─ halfvec.py
│  │     │  │  ├─ register.py
│  │     │  │  ├─ sparsevec.py
│  │     │  │  ├─ vector.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ halfvec.cpython-313.pyc
│  │     │  │     ├─ register.cpython-313.pyc
│  │     │  │     ├─ sparsevec.cpython-313.pyc
│  │     │  │     ├─ vector.cpython-313.pyc
│  │     │  │     └─ __init__.cpython-313.pyc
│  │     │  ├─ sqlalchemy
│  │     │  │  ├─ bit.py
│  │     │  │  ├─ functions.py
│  │     │  │  ├─ halfvec.py
│  │     │  │  ├─ sparsevec.py
│  │     │  │  ├─ vector.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ bit.cpython-313.pyc
│  │     │  │     ├─ functions.cpython-313.pyc
│  │     │  │     ├─ halfvec.cpython-313.pyc
│  │     │  │     ├─ sparsevec.cpython-313.pyc
│  │     │  │     ├─ vector.cpython-313.pyc
│  │     │  │     └─ __init__.cpython-313.pyc
│  │     │  └─ utils
│  │     │     ├─ bit.py
│  │     │     ├─ halfvec.py
│  │     │     ├─ sparsevec.py
│  │     │     ├─ vector.py
│  │     │     ├─ __init__.py
│  │     │     └─ __pycache__
│  │     │        ├─ bit.cpython-313.pyc
│  │     │        ├─ halfvec.cpython-313.pyc
│  │     │        ├─ sparsevec.cpython-313.pyc
│  │     │        ├─ vector.cpython-313.pyc
│  │     │        └─ __init__.cpython-313.pyc
│  │     ├─ pgvector-0.3.6.dist-info
│  │     │  ├─ INSTALLER
│  │     │  ├─ LICENSE.txt
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  ├─ REQUESTED
│  │     │  ├─ top_level.txt
│  │     │  └─ WHEEL
│  │     ├─ PIL
│  │     │  ├─ BdfFontFile.py
│  │     │  ├─ BlpImagePlugin.py
│  │     │  ├─ BmpImagePlugin.py
│  │     │  ├─ BufrStubImagePlugin.py
│  │     │  ├─ ContainerIO.py
│  │     │  ├─ CurImagePlugin.py
│  │     │  ├─ DcxImagePlugin.py
│  │     │  ├─ DdsImagePlugin.py
│  │     │  ├─ EpsImagePlugin.py
│  │     │  ├─ ExifTags.py
│  │     │  ├─ features.py
│  │     │  ├─ FitsImagePlugin.py
│  │     │  ├─ FliImagePlugin.py
│  │     │  ├─ FontFile.py
│  │     │  ├─ FpxImagePlugin.py
│  │     │  ├─ FtexImagePlugin.py
│  │     │  ├─ GbrImagePlugin.py
│  │     │  ├─ GdImageFile.py
│  │     │  ├─ GifImagePlugin.py
│  │     │  ├─ GimpGradientFile.py
│  │     │  ├─ GimpPaletteFile.py
│  │     │  ├─ GribStubImagePlugin.py
│  │     │  ├─ Hdf5StubImagePlugin.py
│  │     │  ├─ IcnsImagePlugin.py
│  │     │  ├─ IcoImagePlugin.py
│  │     │  ├─ Image.py
│  │     │  ├─ ImageChops.py
│  │     │  ├─ ImageCms.py
│  │     │  ├─ ImageColor.py
│  │     │  ├─ ImageDraw.py
│  │     │  ├─ ImageDraw2.py
│  │     │  ├─ ImageEnhance.py
│  │     │  ├─ ImageFile.py
│  │     │  ├─ ImageFilter.py
│  │     │  ├─ ImageFont.py
│  │     │  ├─ ImageGrab.py
│  │     │  ├─ ImageMath.py
│  │     │  ├─ ImageMode.py
│  │     │  ├─ ImageMorph.py
│  │     │  ├─ ImageOps.py
│  │     │  ├─ ImagePalette.py
│  │     │  ├─ ImagePath.py
│  │     │  ├─ ImageQt.py
│  │     │  ├─ ImageSequence.py
│  │     │  ├─ ImageShow.py
│  │     │  ├─ ImageStat.py
│  │     │  ├─ ImageTk.py
│  │     │  ├─ ImageTransform.py
│  │     │  ├─ ImageWin.py
│  │     │  ├─ ImImagePlugin.py
│  │     │  ├─ ImtImagePlugin.py
│  │     │  ├─ IptcImagePlugin.py
│  │     │  ├─ Jpeg2KImagePlugin.py
│  │     │  ├─ JpegImagePlugin.py
│  │     │  ├─ JpegPresets.py
│  │     │  ├─ McIdasImagePlugin.py
│  │     │  ├─ MicImagePlugin.py
│  │     │  ├─ MpegImagePlugin.py
│  │     │  ├─ MpoImagePlugin.py
│  │     │  ├─ MspImagePlugin.py
│  │     │  ├─ PaletteFile.py
│  │     │  ├─ PalmImagePlugin.py
│  │     │  ├─ PcdImagePlugin.py
│  │     │  ├─ PcfFontFile.py
│  │     │  ├─ PcxImagePlugin.py
│  │     │  ├─ PdfImagePlugin.py
│  │     │  ├─ PdfParser.py
│  │     │  ├─ PixarImagePlugin.py
│  │     │  ├─ PngImagePlugin.py
│  │     │  ├─ PpmImagePlugin.py
│  │     │  ├─ PsdImagePlugin.py
│  │     │  ├─ PSDraw.py
│  │     │  ├─ py.typed
│  │     │  ├─ QoiImagePlugin.py
│  │     │  ├─ report.py
│  │     │  ├─ SgiImagePlugin.py
│  │     │  ├─ SpiderImagePlugin.py
│  │     │  ├─ SunImagePlugin.py
│  │     │  ├─ TarIO.py
│  │     │  ├─ TgaImagePlugin.py
│  │     │  ├─ TiffImagePlugin.py
│  │     │  ├─ TiffTags.py
│  │     │  ├─ WalImageFile.py
│  │     │  ├─ WebPImagePlugin.py
│  │     │  ├─ WmfImagePlugin.py
│  │     │  ├─ XbmImagePlugin.py
│  │     │  ├─ XpmImagePlugin.py
│  │     │  ├─ XVThumbImagePlugin.py
│  │     │  ├─ _binary.py
│  │     │  ├─ _deprecate.py
│  │     │  ├─ _imaging.cp313-win_amd64.pyd
│  │     │  ├─ _imaging.pyi
│  │     │  ├─ _imagingcms.cp313-win_amd64.pyd
│  │     │  ├─ _imagingcms.pyi
│  │     │  ├─ _imagingft.cp313-win_amd64.pyd
│  │     │  ├─ _imagingft.pyi
│  │     │  ├─ _imagingmath.cp313-win_amd64.pyd
│  │     │  ├─ _imagingmath.pyi
│  │     │  ├─ _imagingmorph.cp313-win_amd64.pyd
│  │     │  ├─ _imagingmorph.pyi
│  │     │  ├─ _imagingtk.cp313-win_amd64.pyd
│  │     │  ├─ _imagingtk.pyi
│  │     │  ├─ _tkinter_finder.py
│  │     │  ├─ _typing.py
│  │     │  ├─ _util.py
│  │     │  ├─ _version.py
│  │     │  ├─ _webp.cp313-win_amd64.pyd
│  │     │  ├─ _webp.pyi
│  │     │  ├─ __init__.py
│  │     │  ├─ __main__.py
│  │     │  └─ __pycache__
│  │     │     ├─ BdfFontFile.cpython-313.pyc
│  │     │     ├─ BlpImagePlugin.cpython-313.pyc
│  │     │     ├─ BmpImagePlugin.cpython-313.pyc
│  │     │     ├─ BufrStubImagePlugin.cpython-313.pyc
│  │     │     ├─ ContainerIO.cpython-313.pyc
│  │     │     ├─ CurImagePlugin.cpython-313.pyc
│  │     │     ├─ DcxImagePlugin.cpython-313.pyc
│  │     │     ├─ DdsImagePlugin.cpython-313.pyc
│  │     │     ├─ EpsImagePlugin.cpython-313.pyc
│  │     │     ├─ ExifTags.cpython-313.pyc
│  │     │     ├─ features.cpython-313.pyc
│  │     │     ├─ FitsImagePlugin.cpython-313.pyc
│  │     │     ├─ FliImagePlugin.cpython-313.pyc
│  │     │     ├─ FontFile.cpython-313.pyc
│  │     │     ├─ FpxImagePlugin.cpython-313.pyc
│  │     │     ├─ FtexImagePlugin.cpython-313.pyc
│  │     │     ├─ GbrImagePlugin.cpython-313.pyc
│  │     │     ├─ GdImageFile.cpython-313.pyc
│  │     │     ├─ GifImagePlugin.cpython-313.pyc
│  │     │     ├─ GimpGradientFile.cpython-313.pyc
│  │     │     ├─ GimpPaletteFile.cpython-313.pyc
│  │     │     ├─ GribStubImagePlugin.cpython-313.pyc
│  │     │     ├─ Hdf5StubImagePlugin.cpython-313.pyc
│  │     │     ├─ IcnsImagePlugin.cpython-313.pyc
│  │     │     ├─ IcoImagePlugin.cpython-313.pyc
│  │     │     ├─ Image.cpython-313.pyc
│  │     │     ├─ ImageChops.cpython-313.pyc
│  │     │     ├─ ImageCms.cpython-313.pyc
│  │     │     ├─ ImageColor.cpython-313.pyc
│  │     │     ├─ ImageDraw.cpython-313.pyc
│  │     │     ├─ ImageDraw2.cpython-313.pyc
│  │     │     ├─ ImageEnhance.cpython-313.pyc
│  │     │     ├─ ImageFile.cpython-313.pyc
│  │     │     ├─ ImageFilter.cpython-313.pyc
│  │     │     ├─ ImageFont.cpython-313.pyc
│  │     │     ├─ ImageGrab.cpython-313.pyc
│  │     │     ├─ ImageMath.cpython-313.pyc
│  │     │     ├─ ImageMode.cpython-313.pyc
│  │     │     ├─ ImageMorph.cpython-313.pyc
│  │     │     ├─ ImageOps.cpython-313.pyc
│  │     │     ├─ ImagePalette.cpython-313.pyc
│  │     │     ├─ ImagePath.cpython-313.pyc
│  │     │     ├─ ImageQt.cpython-313.pyc
│  │     │     ├─ ImageSequence.cpython-313.pyc
│  │     │     ├─ ImageShow.cpython-313.pyc
│  │     │     ├─ ImageStat.cpython-313.pyc
│  │     │     ├─ ImageTk.cpython-313.pyc
│  │     │     ├─ ImageTransform.cpython-313.pyc
│  │     │     ├─ ImageWin.cpython-313.pyc
│  │     │     ├─ ImImagePlugin.cpython-313.pyc
│  │     │     ├─ ImtImagePlugin.cpython-313.pyc
│  │     │     ├─ IptcImagePlugin.cpython-313.pyc
│  │     │     ├─ Jpeg2KImagePlugin.cpython-313.pyc
│  │     │     ├─ JpegImagePlugin.cpython-313.pyc
│  │     │     ├─ JpegPresets.cpython-313.pyc
│  │     │     ├─ McIdasImagePlugin.cpython-313.pyc
│  │     │     ├─ MicImagePlugin.cpython-313.pyc
│  │     │     ├─ MpegImagePlugin.cpython-313.pyc
│  │     │     ├─ MpoImagePlugin.cpython-313.pyc
│  │     │     ├─ MspImagePlugin.cpython-313.pyc
│  │     │     ├─ PaletteFile.cpython-313.pyc
│  │     │     ├─ PalmImagePlugin.cpython-313.pyc
│  │     │     ├─ PcdImagePlugin.cpython-313.pyc
│  │     │     ├─ PcfFontFile.cpython-313.pyc
│  │     │     ├─ PcxImagePlugin.cpython-313.pyc
│  │     │     ├─ PdfImagePlugin.cpython-313.pyc
│  │     │     ├─ PdfParser.cpython-313.pyc
│  │     │     ├─ PixarImagePlugin.cpython-313.pyc
│  │     │     ├─ PngImagePlugin.cpython-313.pyc
│  │     │     ├─ PpmImagePlugin.cpython-313.pyc
│  │     │     ├─ PsdImagePlugin.cpython-313.pyc
│  │     │     ├─ PSDraw.cpython-313.pyc
│  │     │     ├─ QoiImagePlugin.cpython-313.pyc
│  │     │     ├─ report.cpython-313.pyc
│  │     │     ├─ SgiImagePlugin.cpython-313.pyc
│  │     │     ├─ SpiderImagePlugin.cpython-313.pyc
│  │     │     ├─ SunImagePlugin.cpython-313.pyc
│  │     │     ├─ TarIO.cpython-313.pyc
│  │     │     ├─ TgaImagePlugin.cpython-313.pyc
│  │     │     ├─ TiffImagePlugin.cpython-313.pyc
│  │     │     ├─ TiffTags.cpython-313.pyc
│  │     │     ├─ WalImageFile.cpython-313.pyc
│  │     │     ├─ WebPImagePlugin.cpython-313.pyc
│  │     │     ├─ WmfImagePlugin.cpython-313.pyc
│  │     │     ├─ XbmImagePlugin.cpython-313.pyc
│  │     │     ├─ XpmImagePlugin.cpython-313.pyc
│  │     │     ├─ XVThumbImagePlugin.cpython-313.pyc
│  │     │     ├─ _binary.cpython-313.pyc
│  │     │     ├─ _deprecate.cpython-313.pyc
│  │     │     ├─ _tkinter_finder.cpython-313.pyc
│  │     │     ├─ _typing.cpython-313.pyc
│  │     │     ├─ _util.cpython-313.pyc
│  │     │     ├─ _version.cpython-313.pyc
│  │     │     ├─ __init__.cpython-313.pyc
│  │     │     └─ __main__.cpython-313.pyc
│  │     ├─ pillow-11.1.0.dist-info
│  │     │  ├─ INSTALLER
│  │     │  ├─ LICENSE
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  ├─ REQUESTED
│  │     │  ├─ top_level.txt
│  │     │  ├─ WHEEL
│  │     │  └─ zip-safe
│  │     ├─ pip
│  │     │  ├─ py.typed
│  │     │  ├─ _internal
│  │     │  │  ├─ build_env.py
│  │     │  │  ├─ cache.py
│  │     │  │  ├─ cli
│  │     │  │  │  ├─ autocompletion.py
│  │     │  │  │  ├─ base_command.py
│  │     │  │  │  ├─ cmdoptions.py
│  │     │  │  │  ├─ command_context.py
│  │     │  │  │  ├─ index_command.py
│  │     │  │  │  ├─ main.py
│  │     │  │  │  ├─ main_parser.py
│  │     │  │  │  ├─ parser.py
│  │     │  │  │  ├─ progress_bars.py
│  │     │  │  │  ├─ req_command.py
│  │     │  │  │  ├─ spinners.py
│  │     │  │  │  ├─ status_codes.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ autocompletion.cpython-313.pyc
│  │     │  │  │     ├─ base_command.cpython-313.pyc
│  │     │  │  │     ├─ cmdoptions.cpython-313.pyc
│  │     │  │  │     ├─ command_context.cpython-313.pyc
│  │     │  │  │     ├─ index_command.cpython-313.pyc
│  │     │  │  │     ├─ main.cpython-313.pyc
│  │     │  │  │     ├─ main_parser.cpython-313.pyc
│  │     │  │  │     ├─ parser.cpython-313.pyc
│  │     │  │  │     ├─ progress_bars.cpython-313.pyc
│  │     │  │  │     ├─ req_command.cpython-313.pyc
│  │     │  │  │     ├─ spinners.cpython-313.pyc
│  │     │  │  │     ├─ status_codes.cpython-313.pyc
│  │     │  │  │     └─ __init__.cpython-313.pyc
│  │     │  │  ├─ commands
│  │     │  │  │  ├─ cache.py
│  │     │  │  │  ├─ check.py
│  │     │  │  │  ├─ completion.py
│  │     │  │  │  ├─ configuration.py
│  │     │  │  │  ├─ debug.py
│  │     │  │  │  ├─ download.py
│  │     │  │  │  ├─ freeze.py
│  │     │  │  │  ├─ hash.py
│  │     │  │  │  ├─ help.py
│  │     │  │  │  ├─ index.py
│  │     │  │  │  ├─ inspect.py
│  │     │  │  │  ├─ install.py
│  │     │  │  │  ├─ list.py
│  │     │  │  │  ├─ search.py
│  │     │  │  │  ├─ show.py
│  │     │  │  │  ├─ uninstall.py
│  │     │  │  │  ├─ wheel.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ cache.cpython-313.pyc
│  │     │  │  │     ├─ check.cpython-313.pyc
│  │     │  │  │     ├─ completion.cpython-313.pyc
│  │     │  │  │     ├─ configuration.cpython-313.pyc
│  │     │  │  │     ├─ debug.cpython-313.pyc
│  │     │  │  │     ├─ download.cpython-313.pyc
│  │     │  │  │     ├─ freeze.cpython-313.pyc
│  │     │  │  │     ├─ hash.cpython-313.pyc
│  │     │  │  │     ├─ help.cpython-313.pyc
│  │     │  │  │     ├─ index.cpython-313.pyc
│  │     │  │  │     ├─ inspect.cpython-313.pyc
│  │     │  │  │     ├─ install.cpython-313.pyc
│  │     │  │  │     ├─ list.cpython-313.pyc
│  │     │  │  │     ├─ search.cpython-313.pyc
│  │     │  │  │     ├─ show.cpython-313.pyc
│  │     │  │  │     ├─ uninstall.cpython-313.pyc
│  │     │  │  │     ├─ wheel.cpython-313.pyc
│  │     │  │  │     └─ __init__.cpython-313.pyc
│  │     │  │  ├─ configuration.py
│  │     │  │  ├─ distributions
│  │     │  │  │  ├─ base.py
│  │     │  │  │  ├─ installed.py
│  │     │  │  │  ├─ sdist.py
│  │     │  │  │  ├─ wheel.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ base.cpython-313.pyc
│  │     │  │  │     ├─ installed.cpython-313.pyc
│  │     │  │  │     ├─ sdist.cpython-313.pyc
│  │     │  │  │     ├─ wheel.cpython-313.pyc
│  │     │  │  │     └─ __init__.cpython-313.pyc
│  │     │  │  ├─ exceptions.py
│  │     │  │  ├─ index
│  │     │  │  │  ├─ collector.py
│  │     │  │  │  ├─ package_finder.py
│  │     │  │  │  ├─ sources.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ collector.cpython-313.pyc
│  │     │  │  │     ├─ package_finder.cpython-313.pyc
│  │     │  │  │     ├─ sources.cpython-313.pyc
│  │     │  │  │     └─ __init__.cpython-313.pyc
│  │     │  │  ├─ locations
│  │     │  │  │  ├─ base.py
│  │     │  │  │  ├─ _distutils.py
│  │     │  │  │  ├─ _sysconfig.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ base.cpython-313.pyc
│  │     │  │  │     ├─ _distutils.cpython-313.pyc
│  │     │  │  │     ├─ _sysconfig.cpython-313.pyc
│  │     │  │  │     └─ __init__.cpython-313.pyc
│  │     │  │  ├─ main.py
│  │     │  │  ├─ metadata
│  │     │  │  │  ├─ base.py
│  │     │  │  │  ├─ importlib
│  │     │  │  │  │  ├─ _compat.py
│  │     │  │  │  │  ├─ _dists.py
│  │     │  │  │  │  ├─ _envs.py
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  └─ __pycache__
│  │     │  │  │  │     ├─ _compat.cpython-313.pyc
│  │     │  │  │  │     ├─ _dists.cpython-313.pyc
│  │     │  │  │  │     ├─ _envs.cpython-313.pyc
│  │     │  │  │  │     └─ __init__.cpython-313.pyc
│  │     │  │  │  ├─ pkg_resources.py
│  │     │  │  │  ├─ _json.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ base.cpython-313.pyc
│  │     │  │  │     ├─ pkg_resources.cpython-313.pyc
│  │     │  │  │     ├─ _json.cpython-313.pyc
│  │     │  │  │     └─ __init__.cpython-313.pyc
│  │     │  │  ├─ models
│  │     │  │  │  ├─ candidate.py
│  │     │  │  │  ├─ direct_url.py
│  │     │  │  │  ├─ format_control.py
│  │     │  │  │  ├─ index.py
│  │     │  │  │  ├─ installation_report.py
│  │     │  │  │  ├─ link.py
│  │     │  │  │  ├─ scheme.py
│  │     │  │  │  ├─ search_scope.py
│  │     │  │  │  ├─ selection_prefs.py
│  │     │  │  │  ├─ target_python.py
│  │     │  │  │  ├─ wheel.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ candidate.cpython-313.pyc
│  │     │  │  │     ├─ direct_url.cpython-313.pyc
│  │     │  │  │     ├─ format_control.cpython-313.pyc
│  │     │  │  │     ├─ index.cpython-313.pyc
│  │     │  │  │     ├─ installation_report.cpython-313.pyc
│  │     │  │  │     ├─ link.cpython-313.pyc
│  │     │  │  │     ├─ scheme.cpython-313.pyc
│  │     │  │  │     ├─ search_scope.cpython-313.pyc
│  │     │  │  │     ├─ selection_prefs.cpython-313.pyc
│  │     │  │  │     ├─ target_python.cpython-313.pyc
│  │     │  │  │     ├─ wheel.cpython-313.pyc
│  │     │  │  │     └─ __init__.cpython-313.pyc
│  │     │  │  ├─ network
│  │     │  │  │  ├─ auth.py
│  │     │  │  │  ├─ cache.py
│  │     │  │  │  ├─ download.py
│  │     │  │  │  ├─ lazy_wheel.py
│  │     │  │  │  ├─ session.py
│  │     │  │  │  ├─ utils.py
│  │     │  │  │  ├─ xmlrpc.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ auth.cpython-313.pyc
│  │     │  │  │     ├─ cache.cpython-313.pyc
│  │     │  │  │     ├─ download.cpython-313.pyc
│  │     │  │  │     ├─ lazy_wheel.cpython-313.pyc
│  │     │  │  │     ├─ session.cpython-313.pyc
│  │     │  │  │     ├─ utils.cpython-313.pyc
│  │     │  │  │     ├─ xmlrpc.cpython-313.pyc
│  │     │  │  │     └─ __init__.cpython-313.pyc
│  │     │  │  ├─ operations
│  │     │  │  │  ├─ build
│  │     │  │  │  │  ├─ build_tracker.py
│  │     │  │  │  │  ├─ metadata.py
│  │     │  │  │  │  ├─ metadata_editable.py
│  │     │  │  │  │  ├─ metadata_legacy.py
│  │     │  │  │  │  ├─ wheel.py
│  │     │  │  │  │  ├─ wheel_editable.py
│  │     │  │  │  │  ├─ wheel_legacy.py
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  └─ __pycache__
│  │     │  │  │  │     ├─ build_tracker.cpython-313.pyc
│  │     │  │  │  │     ├─ metadata.cpython-313.pyc
│  │     │  │  │  │     ├─ metadata_editable.cpython-313.pyc
│  │     │  │  │  │     ├─ metadata_legacy.cpython-313.pyc
│  │     │  │  │  │     ├─ wheel.cpython-313.pyc
│  │     │  │  │  │     ├─ wheel_editable.cpython-313.pyc
│  │     │  │  │  │     ├─ wheel_legacy.cpython-313.pyc
│  │     │  │  │  │     └─ __init__.cpython-313.pyc
│  │     │  │  │  ├─ check.py
│  │     │  │  │  ├─ freeze.py
│  │     │  │  │  ├─ install
│  │     │  │  │  │  ├─ editable_legacy.py
│  │     │  │  │  │  ├─ wheel.py
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  └─ __pycache__
│  │     │  │  │  │     ├─ editable_legacy.cpython-313.pyc
│  │     │  │  │  │     ├─ wheel.cpython-313.pyc
│  │     │  │  │  │     └─ __init__.cpython-313.pyc
│  │     │  │  │  ├─ prepare.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ check.cpython-313.pyc
│  │     │  │  │     ├─ freeze.cpython-313.pyc
│  │     │  │  │     ├─ prepare.cpython-313.pyc
│  │     │  │  │     └─ __init__.cpython-313.pyc
│  │     │  │  ├─ pyproject.py
│  │     │  │  ├─ req
│  │     │  │  │  ├─ constructors.py
│  │     │  │  │  ├─ req_file.py
│  │     │  │  │  ├─ req_install.py
│  │     │  │  │  ├─ req_set.py
│  │     │  │  │  ├─ req_uninstall.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ constructors.cpython-313.pyc
│  │     │  │  │     ├─ req_file.cpython-313.pyc
│  │     │  │  │     ├─ req_install.cpython-313.pyc
│  │     │  │  │     ├─ req_set.cpython-313.pyc
│  │     │  │  │     ├─ req_uninstall.cpython-313.pyc
│  │     │  │  │     └─ __init__.cpython-313.pyc
│  │     │  │  ├─ resolution
│  │     │  │  │  ├─ base.py
│  │     │  │  │  ├─ legacy
│  │     │  │  │  │  ├─ resolver.py
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  └─ __pycache__
│  │     │  │  │  │     ├─ resolver.cpython-313.pyc
│  │     │  │  │  │     └─ __init__.cpython-313.pyc
│  │     │  │  │  ├─ resolvelib
│  │     │  │  │  │  ├─ base.py
│  │     │  │  │  │  ├─ candidates.py
│  │     │  │  │  │  ├─ factory.py
│  │     │  │  │  │  ├─ found_candidates.py
│  │     │  │  │  │  ├─ provider.py
│  │     │  │  │  │  ├─ reporter.py
│  │     │  │  │  │  ├─ requirements.py
│  │     │  │  │  │  ├─ resolver.py
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  └─ __pycache__
│  │     │  │  │  │     ├─ base.cpython-313.pyc
│  │     │  │  │  │     ├─ candidates.cpython-313.pyc
│  │     │  │  │  │     ├─ factory.cpython-313.pyc
│  │     │  │  │  │     ├─ found_candidates.cpython-313.pyc
│  │     │  │  │  │     ├─ provider.cpython-313.pyc
│  │     │  │  │  │     ├─ reporter.cpython-313.pyc
│  │     │  │  │  │     ├─ requirements.cpython-313.pyc
│  │     │  │  │  │     ├─ resolver.cpython-313.pyc
│  │     │  │  │  │     └─ __init__.cpython-313.pyc
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ base.cpython-313.pyc
│  │     │  │  │     └─ __init__.cpython-313.pyc
│  │     │  │  ├─ self_outdated_check.py
│  │     │  │  ├─ utils
│  │     │  │  │  ├─ appdirs.py
│  │     │  │  │  ├─ compat.py
│  │     │  │  │  ├─ compatibility_tags.py
│  │     │  │  │  ├─ datetime.py
│  │     │  │  │  ├─ deprecation.py
│  │     │  │  │  ├─ direct_url_helpers.py
│  │     │  │  │  ├─ egg_link.py
│  │     │  │  │  ├─ encoding.py
│  │     │  │  │  ├─ entrypoints.py
│  │     │  │  │  ├─ filesystem.py
│  │     │  │  │  ├─ filetypes.py
│  │     │  │  │  ├─ glibc.py
│  │     │  │  │  ├─ hashes.py
│  │     │  │  │  ├─ logging.py
│  │     │  │  │  ├─ misc.py
│  │     │  │  │  ├─ packaging.py
│  │     │  │  │  ├─ retry.py
│  │     │  │  │  ├─ setuptools_build.py
│  │     │  │  │  ├─ subprocess.py
│  │     │  │  │  ├─ temp_dir.py
│  │     │  │  │  ├─ unpacking.py
│  │     │  │  │  ├─ urls.py
│  │     │  │  │  ├─ virtualenv.py
│  │     │  │  │  ├─ wheel.py
│  │     │  │  │  ├─ _jaraco_text.py
│  │     │  │  │  ├─ _log.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ appdirs.cpython-313.pyc
│  │     │  │  │     ├─ compat.cpython-313.pyc
│  │     │  │  │     ├─ compatibility_tags.cpython-313.pyc
│  │     │  │  │     ├─ datetime.cpython-313.pyc
│  │     │  │  │     ├─ deprecation.cpython-313.pyc
│  │     │  │  │     ├─ direct_url_helpers.cpython-313.pyc
│  │     │  │  │     ├─ egg_link.cpython-313.pyc
│  │     │  │  │     ├─ encoding.cpython-313.pyc
│  │     │  │  │     ├─ entrypoints.cpython-313.pyc
│  │     │  │  │     ├─ filesystem.cpython-313.pyc
│  │     │  │  │     ├─ filetypes.cpython-313.pyc
│  │     │  │  │     ├─ glibc.cpython-313.pyc
│  │     │  │  │     ├─ hashes.cpython-313.pyc
│  │     │  │  │     ├─ logging.cpython-313.pyc
│  │     │  │  │     ├─ misc.cpython-313.pyc
│  │     │  │  │     ├─ packaging.cpython-313.pyc
│  │     │  │  │     ├─ retry.cpython-313.pyc
│  │     │  │  │     ├─ setuptools_build.cpython-313.pyc
│  │     │  │  │     ├─ subprocess.cpython-313.pyc
│  │     │  │  │     ├─ temp_dir.cpython-313.pyc
│  │     │  │  │     ├─ unpacking.cpython-313.pyc
│  │     │  │  │     ├─ urls.cpython-313.pyc
│  │     │  │  │     ├─ virtualenv.cpython-313.pyc
│  │     │  │  │     ├─ wheel.cpython-313.pyc
│  │     │  │  │     ├─ _jaraco_text.cpython-313.pyc
│  │     │  │  │     ├─ _log.cpython-313.pyc
│  │     │  │  │     └─ __init__.cpython-313.pyc
│  │     │  │  ├─ vcs
│  │     │  │  │  ├─ bazaar.py
│  │     │  │  │  ├─ git.py
│  │     │  │  │  ├─ mercurial.py
│  │     │  │  │  ├─ subversion.py
│  │     │  │  │  ├─ versioncontrol.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ bazaar.cpython-313.pyc
│  │     │  │  │     ├─ git.cpython-313.pyc
│  │     │  │  │     ├─ mercurial.cpython-313.pyc
│  │     │  │  │     ├─ subversion.cpython-313.pyc
│  │     │  │  │     ├─ versioncontrol.cpython-313.pyc
│  │     │  │  │     └─ __init__.cpython-313.pyc
│  │     │  │  ├─ wheel_builder.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ build_env.cpython-313.pyc
│  │     │  │     ├─ cache.cpython-313.pyc
│  │     │  │     ├─ configuration.cpython-313.pyc
│  │     │  │     ├─ exceptions.cpython-313.pyc
│  │     │  │     ├─ main.cpython-313.pyc
│  │     │  │     ├─ pyproject.cpython-313.pyc
│  │     │  │     ├─ self_outdated_check.cpython-313.pyc
│  │     │  │     ├─ wheel_builder.cpython-313.pyc
│  │     │  │     └─ __init__.cpython-313.pyc
│  │     │  ├─ _vendor
│  │     │  │  ├─ cachecontrol
│  │     │  │  │  ├─ adapter.py
│  │     │  │  │  ├─ cache.py
│  │     │  │  │  ├─ caches
│  │     │  │  │  │  ├─ file_cache.py
│  │     │  │  │  │  ├─ redis_cache.py
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  └─ __pycache__
│  │     │  │  │  │     ├─ file_cache.cpython-313.pyc
│  │     │  │  │  │     ├─ redis_cache.cpython-313.pyc
│  │     │  │  │  │     └─ __init__.cpython-313.pyc
│  │     │  │  │  ├─ controller.py
│  │     │  │  │  ├─ filewrapper.py
│  │     │  │  │  ├─ heuristics.py
│  │     │  │  │  ├─ py.typed
│  │     │  │  │  ├─ serialize.py
│  │     │  │  │  ├─ wrapper.py
│  │     │  │  │  ├─ _cmd.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ adapter.cpython-313.pyc
│  │     │  │  │     ├─ cache.cpython-313.pyc
│  │     │  │  │     ├─ controller.cpython-313.pyc
│  │     │  │  │     ├─ filewrapper.cpython-313.pyc
│  │     │  │  │     ├─ heuristics.cpython-313.pyc
│  │     │  │  │     ├─ serialize.cpython-313.pyc
│  │     │  │  │     ├─ wrapper.cpython-313.pyc
│  │     │  │  │     ├─ _cmd.cpython-313.pyc
│  │     │  │  │     └─ __init__.cpython-313.pyc
│  │     │  │  ├─ certifi
│  │     │  │  │  ├─ cacert.pem
│  │     │  │  │  ├─ core.py
│  │     │  │  │  ├─ py.typed
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  ├─ __main__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ core.cpython-313.pyc
│  │     │  │  │     ├─ __init__.cpython-313.pyc
│  │     │  │  │     └─ __main__.cpython-313.pyc
│  │     │  │  ├─ distlib
│  │     │  │  │  ├─ compat.py
│  │     │  │  │  ├─ database.py
│  │     │  │  │  ├─ index.py
│  │     │  │  │  ├─ locators.py
│  │     │  │  │  ├─ manifest.py
│  │     │  │  │  ├─ markers.py
│  │     │  │  │  ├─ metadata.py
│  │     │  │  │  ├─ resources.py
│  │     │  │  │  ├─ scripts.py
│  │     │  │  │  ├─ t32.exe
│  │     │  │  │  ├─ t64-arm.exe
│  │     │  │  │  ├─ t64.exe
│  │     │  │  │  ├─ util.py
│  │     │  │  │  ├─ version.py
│  │     │  │  │  ├─ w32.exe
│  │     │  │  │  ├─ w64-arm.exe
│  │     │  │  │  ├─ w64.exe
│  │     │  │  │  ├─ wheel.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ compat.cpython-313.pyc
│  │     │  │  │     ├─ database.cpython-313.pyc
│  │     │  │  │     ├─ index.cpython-313.pyc
│  │     │  │  │     ├─ locators.cpython-313.pyc
│  │     │  │  │     ├─ manifest.cpython-313.pyc
│  │     │  │  │     ├─ markers.cpython-313.pyc
│  │     │  │  │     ├─ metadata.cpython-313.pyc
│  │     │  │  │     ├─ resources.cpython-313.pyc
│  │     │  │  │     ├─ scripts.cpython-313.pyc
│  │     │  │  │     ├─ util.cpython-313.pyc
│  │     │  │  │     ├─ version.cpython-313.pyc
│  │     │  │  │     ├─ wheel.cpython-313.pyc
│  │     │  │  │     └─ __init__.cpython-313.pyc
│  │     │  │  ├─ distro
│  │     │  │  │  ├─ distro.py
│  │     │  │  │  ├─ py.typed
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  ├─ __main__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ distro.cpython-313.pyc
│  │     │  │  │     ├─ __init__.cpython-313.pyc
│  │     │  │  │     └─ __main__.cpython-313.pyc
│  │     │  │  ├─ idna
│  │     │  │  │  ├─ codec.py
│  │     │  │  │  ├─ compat.py
│  │     │  │  │  ├─ core.py
│  │     │  │  │  ├─ idnadata.py
│  │     │  │  │  ├─ intranges.py
│  │     │  │  │  ├─ package_data.py
│  │     │  │  │  ├─ py.typed
│  │     │  │  │  ├─ uts46data.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ codec.cpython-313.pyc
│  │     │  │  │     ├─ compat.cpython-313.pyc
│  │     │  │  │     ├─ core.cpython-313.pyc
│  │     │  │  │     ├─ idnadata.cpython-313.pyc
│  │     │  │  │     ├─ intranges.cpython-313.pyc
│  │     │  │  │     ├─ package_data.cpython-313.pyc
│  │     │  │  │     ├─ uts46data.cpython-313.pyc
│  │     │  │  │     └─ __init__.cpython-313.pyc
│  │     │  │  ├─ msgpack
│  │     │  │  │  ├─ exceptions.py
│  │     │  │  │  ├─ ext.py
│  │     │  │  │  ├─ fallback.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ exceptions.cpython-313.pyc
│  │     │  │  │     ├─ ext.cpython-313.pyc
│  │     │  │  │     ├─ fallback.cpython-313.pyc
│  │     │  │  │     └─ __init__.cpython-313.pyc
│  │     │  │  ├─ packaging
│  │     │  │  │  ├─ markers.py
│  │     │  │  │  ├─ metadata.py
│  │     │  │  │  ├─ py.typed
│  │     │  │  │  ├─ requirements.py
│  │     │  │  │  ├─ specifiers.py
│  │     │  │  │  ├─ tags.py
│  │     │  │  │  ├─ utils.py
│  │     │  │  │  ├─ version.py
│  │     │  │  │  ├─ _elffile.py
│  │     │  │  │  ├─ _manylinux.py
│  │     │  │  │  ├─ _musllinux.py
│  │     │  │  │  ├─ _parser.py
│  │     │  │  │  ├─ _structures.py
│  │     │  │  │  ├─ _tokenizer.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ markers.cpython-313.pyc
│  │     │  │  │     ├─ metadata.cpython-313.pyc
│  │     │  │  │     ├─ requirements.cpython-313.pyc
│  │     │  │  │     ├─ specifiers.cpython-313.pyc
│  │     │  │  │     ├─ tags.cpython-313.pyc
│  │     │  │  │     ├─ utils.cpython-313.pyc
│  │     │  │  │     ├─ version.cpython-313.pyc
│  │     │  │  │     ├─ _elffile.cpython-313.pyc
│  │     │  │  │     ├─ _manylinux.cpython-313.pyc
│  │     │  │  │     ├─ _musllinux.cpython-313.pyc
│  │     │  │  │     ├─ _parser.cpython-313.pyc
│  │     │  │  │     ├─ _structures.cpython-313.pyc
│  │     │  │  │     ├─ _tokenizer.cpython-313.pyc
│  │     │  │  │     └─ __init__.cpython-313.pyc
│  │     │  │  ├─ pkg_resources
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     └─ __init__.cpython-313.pyc
│  │     │  │  ├─ platformdirs
│  │     │  │  │  ├─ android.py
│  │     │  │  │  ├─ api.py
│  │     │  │  │  ├─ macos.py
│  │     │  │  │  ├─ py.typed
│  │     │  │  │  ├─ unix.py
│  │     │  │  │  ├─ version.py
│  │     │  │  │  ├─ windows.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  ├─ __main__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ android.cpython-313.pyc
│  │     │  │  │     ├─ api.cpython-313.pyc
│  │     │  │  │     ├─ macos.cpython-313.pyc
│  │     │  │  │     ├─ unix.cpython-313.pyc
│  │     │  │  │     ├─ version.cpython-313.pyc
│  │     │  │  │     ├─ windows.cpython-313.pyc
│  │     │  │  │     ├─ __init__.cpython-313.pyc
│  │     │  │  │     └─ __main__.cpython-313.pyc
│  │     │  │  ├─ pygments
│  │     │  │  │  ├─ cmdline.py
│  │     │  │  │  ├─ console.py
│  │     │  │  │  ├─ filter.py
│  │     │  │  │  ├─ filters
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  └─ __pycache__
│  │     │  │  │  │     └─ __init__.cpython-313.pyc
│  │     │  │  │  ├─ formatter.py
│  │     │  │  │  ├─ formatters
│  │     │  │  │  │  ├─ bbcode.py
│  │     │  │  │  │  ├─ groff.py
│  │     │  │  │  │  ├─ html.py
│  │     │  │  │  │  ├─ img.py
│  │     │  │  │  │  ├─ irc.py
│  │     │  │  │  │  ├─ latex.py
│  │     │  │  │  │  ├─ other.py
│  │     │  │  │  │  ├─ pangomarkup.py
│  │     │  │  │  │  ├─ rtf.py
│  │     │  │  │  │  ├─ svg.py
│  │     │  │  │  │  ├─ terminal.py
│  │     │  │  │  │  ├─ terminal256.py
│  │     │  │  │  │  ├─ _mapping.py
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  └─ __pycache__
│  │     │  │  │  │     ├─ bbcode.cpython-313.pyc
│  │     │  │  │  │     ├─ groff.cpython-313.pyc
│  │     │  │  │  │     ├─ html.cpython-313.pyc
│  │     │  │  │  │     ├─ img.cpython-313.pyc
│  │     │  │  │  │     ├─ irc.cpython-313.pyc
│  │     │  │  │  │     ├─ latex.cpython-313.pyc
│  │     │  │  │  │     ├─ other.cpython-313.pyc
│  │     │  │  │  │     ├─ pangomarkup.cpython-313.pyc
│  │     │  │  │  │     ├─ rtf.cpython-313.pyc
│  │     │  │  │  │     ├─ svg.cpython-313.pyc
│  │     │  │  │  │     ├─ terminal.cpython-313.pyc
│  │     │  │  │  │     ├─ terminal256.cpython-313.pyc
│  │     │  │  │  │     ├─ _mapping.cpython-313.pyc
│  │     │  │  │  │     └─ __init__.cpython-313.pyc
│  │     │  │  │  ├─ lexer.py
│  │     │  │  │  ├─ lexers
│  │     │  │  │  │  ├─ python.py
│  │     │  │  │  │  ├─ _mapping.py
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  └─ __pycache__
│  │     │  │  │  │     ├─ python.cpython-313.pyc
│  │     │  │  │  │     ├─ _mapping.cpython-313.pyc
│  │     │  │  │  │     └─ __init__.cpython-313.pyc
│  │     │  │  │  ├─ modeline.py
│  │     │  │  │  ├─ plugin.py
│  │     │  │  │  ├─ regexopt.py
│  │     │  │  │  ├─ scanner.py
│  │     │  │  │  ├─ sphinxext.py
│  │     │  │  │  ├─ style.py
│  │     │  │  │  ├─ styles
│  │     │  │  │  │  ├─ _mapping.py
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  └─ __pycache__
│  │     │  │  │  │     ├─ _mapping.cpython-313.pyc
│  │     │  │  │  │     └─ __init__.cpython-313.pyc
│  │     │  │  │  ├─ token.py
│  │     │  │  │  ├─ unistring.py
│  │     │  │  │  ├─ util.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  ├─ __main__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ cmdline.cpython-313.pyc
│  │     │  │  │     ├─ console.cpython-313.pyc
│  │     │  │  │     ├─ filter.cpython-313.pyc
│  │     │  │  │     ├─ formatter.cpython-313.pyc
│  │     │  │  │     ├─ lexer.cpython-313.pyc
│  │     │  │  │     ├─ modeline.cpython-313.pyc
│  │     │  │  │     ├─ plugin.cpython-313.pyc
│  │     │  │  │     ├─ regexopt.cpython-313.pyc
│  │     │  │  │     ├─ scanner.cpython-313.pyc
│  │     │  │  │     ├─ sphinxext.cpython-313.pyc
│  │     │  │  │     ├─ style.cpython-313.pyc
│  │     │  │  │     ├─ token.cpython-313.pyc
│  │     │  │  │     ├─ unistring.cpython-313.pyc
│  │     │  │  │     ├─ util.cpython-313.pyc
│  │     │  │  │     ├─ __init__.cpython-313.pyc
│  │     │  │  │     └─ __main__.cpython-313.pyc
│  │     │  │  ├─ pyproject_hooks
│  │     │  │  │  ├─ _compat.py
│  │     │  │  │  ├─ _impl.py
│  │     │  │  │  ├─ _in_process
│  │     │  │  │  │  ├─ _in_process.py
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  └─ __pycache__
│  │     │  │  │  │     ├─ _in_process.cpython-313.pyc
│  │     │  │  │  │     └─ __init__.cpython-313.pyc
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ _compat.cpython-313.pyc
│  │     │  │  │     ├─ _impl.cpython-313.pyc
│  │     │  │  │     └─ __init__.cpython-313.pyc
│  │     │  │  ├─ requests
│  │     │  │  │  ├─ adapters.py
│  │     │  │  │  ├─ api.py
│  │     │  │  │  ├─ auth.py
│  │     │  │  │  ├─ certs.py
│  │     │  │  │  ├─ compat.py
│  │     │  │  │  ├─ cookies.py
│  │     │  │  │  ├─ exceptions.py
│  │     │  │  │  ├─ help.py
│  │     │  │  │  ├─ hooks.py
│  │     │  │  │  ├─ models.py
│  │     │  │  │  ├─ packages.py
│  │     │  │  │  ├─ sessions.py
│  │     │  │  │  ├─ status_codes.py
│  │     │  │  │  ├─ structures.py
│  │     │  │  │  ├─ utils.py
│  │     │  │  │  ├─ _internal_utils.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  ├─ __pycache__
│  │     │  │  │  │  ├─ adapters.cpython-313.pyc
│  │     │  │  │  │  ├─ api.cpython-313.pyc
│  │     │  │  │  │  ├─ auth.cpython-313.pyc
│  │     │  │  │  │  ├─ certs.cpython-313.pyc
│  │     │  │  │  │  ├─ compat.cpython-313.pyc
│  │     │  │  │  │  ├─ cookies.cpython-313.pyc
│  │     │  │  │  │  ├─ exceptions.cpython-313.pyc
│  │     │  │  │  │  ├─ help.cpython-313.pyc
│  │     │  │  │  │  ├─ hooks.cpython-313.pyc
│  │     │  │  │  │  ├─ models.cpython-313.pyc
│  │     │  │  │  │  ├─ packages.cpython-313.pyc
│  │     │  │  │  │  ├─ sessions.cpython-313.pyc
│  │     │  │  │  │  ├─ status_codes.cpython-313.pyc
│  │     │  │  │  │  ├─ structures.cpython-313.pyc
│  │     │  │  │  │  ├─ utils.cpython-313.pyc
│  │     │  │  │  │  ├─ _internal_utils.cpython-313.pyc
│  │     │  │  │  │  ├─ __init__.cpython-313.pyc
│  │     │  │  │  │  └─ __version__.cpython-313.pyc
│  │     │  │  │  └─ __version__.py
│  │     │  │  ├─ resolvelib
│  │     │  │  │  ├─ compat
│  │     │  │  │  │  ├─ collections_abc.py
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  └─ __pycache__
│  │     │  │  │  │     ├─ collections_abc.cpython-313.pyc
│  │     │  │  │  │     └─ __init__.cpython-313.pyc
│  │     │  │  │  ├─ providers.py
│  │     │  │  │  ├─ py.typed
│  │     │  │  │  ├─ reporters.py
│  │     │  │  │  ├─ resolvers.py
│  │     │  │  │  ├─ structs.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ providers.cpython-313.pyc
│  │     │  │  │     ├─ reporters.cpython-313.pyc
│  │     │  │  │     ├─ resolvers.cpython-313.pyc
│  │     │  │  │     ├─ structs.cpython-313.pyc
│  │     │  │  │     └─ __init__.cpython-313.pyc
│  │     │  │  ├─ rich
│  │     │  │  │  ├─ abc.py
│  │     │  │  │  ├─ align.py
│  │     │  │  │  ├─ ansi.py
│  │     │  │  │  ├─ bar.py
│  │     │  │  │  ├─ box.py
│  │     │  │  │  ├─ cells.py
│  │     │  │  │  ├─ color.py
│  │     │  │  │  ├─ color_triplet.py
│  │     │  │  │  ├─ columns.py
│  │     │  │  │  ├─ console.py
│  │     │  │  │  ├─ constrain.py
│  │     │  │  │  ├─ containers.py
│  │     │  │  │  ├─ control.py
│  │     │  │  │  ├─ default_styles.py
│  │     │  │  │  ├─ diagnose.py
│  │     │  │  │  ├─ emoji.py
│  │     │  │  │  ├─ errors.py
│  │     │  │  │  ├─ filesize.py
│  │     │  │  │  ├─ file_proxy.py
│  │     │  │  │  ├─ highlighter.py
│  │     │  │  │  ├─ json.py
│  │     │  │  │  ├─ jupyter.py
│  │     │  │  │  ├─ layout.py
│  │     │  │  │  ├─ live.py
│  │     │  │  │  ├─ live_render.py
│  │     │  │  │  ├─ logging.py
│  │     │  │  │  ├─ markup.py
│  │     │  │  │  ├─ measure.py
│  │     │  │  │  ├─ padding.py
│  │     │  │  │  ├─ pager.py
│  │     │  │  │  ├─ palette.py
│  │     │  │  │  ├─ panel.py
│  │     │  │  │  ├─ pretty.py
│  │     │  │  │  ├─ progress.py
│  │     │  │  │  ├─ progress_bar.py
│  │     │  │  │  ├─ prompt.py
│  │     │  │  │  ├─ protocol.py
│  │     │  │  │  ├─ py.typed
│  │     │  │  │  ├─ region.py
│  │     │  │  │  ├─ repr.py
│  │     │  │  │  ├─ rule.py
│  │     │  │  │  ├─ scope.py
│  │     │  │  │  ├─ screen.py
│  │     │  │  │  ├─ segment.py
│  │     │  │  │  ├─ spinner.py
│  │     │  │  │  ├─ status.py
│  │     │  │  │  ├─ style.py
│  │     │  │  │  ├─ styled.py
│  │     │  │  │  ├─ syntax.py
│  │     │  │  │  ├─ table.py
│  │     │  │  │  ├─ terminal_theme.py
│  │     │  │  │  ├─ text.py
│  │     │  │  │  ├─ theme.py
│  │     │  │  │  ├─ themes.py
│  │     │  │  │  ├─ traceback.py
│  │     │  │  │  ├─ tree.py
│  │     │  │  │  ├─ _cell_widths.py
│  │     │  │  │  ├─ _emoji_codes.py
│  │     │  │  │  ├─ _emoji_replace.py
│  │     │  │  │  ├─ _export_format.py
│  │     │  │  │  ├─ _extension.py
│  │     │  │  │  ├─ _fileno.py
│  │     │  │  │  ├─ _inspect.py
│  │     │  │  │  ├─ _log_render.py
│  │     │  │  │  ├─ _loop.py
│  │     │  │  │  ├─ _null_file.py
│  │     │  │  │  ├─ _palettes.py
│  │     │  │  │  ├─ _pick.py
│  │     │  │  │  ├─ _ratio.py
│  │     │  │  │  ├─ _spinners.py
│  │     │  │  │  ├─ _stack.py
│  │     │  │  │  ├─ _timer.py
│  │     │  │  │  ├─ _win32_console.py
│  │     │  │  │  ├─ _windows.py
│  │     │  │  │  ├─ _windows_renderer.py
│  │     │  │  │  ├─ _wrap.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  ├─ __main__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ abc.cpython-313.pyc
│  │     │  │  │     ├─ align.cpython-313.pyc
│  │     │  │  │     ├─ ansi.cpython-313.pyc
│  │     │  │  │     ├─ bar.cpython-313.pyc
│  │     │  │  │     ├─ box.cpython-313.pyc
│  │     │  │  │     ├─ cells.cpython-313.pyc
│  │     │  │  │     ├─ color.cpython-313.pyc
│  │     │  │  │     ├─ color_triplet.cpython-313.pyc
│  │     │  │  │     ├─ columns.cpython-313.pyc
│  │     │  │  │     ├─ console.cpython-313.pyc
│  │     │  │  │     ├─ constrain.cpython-313.pyc
│  │     │  │  │     ├─ containers.cpython-313.pyc
│  │     │  │  │     ├─ control.cpython-313.pyc
│  │     │  │  │     ├─ default_styles.cpython-313.pyc
│  │     │  │  │     ├─ diagnose.cpython-313.pyc
│  │     │  │  │     ├─ emoji.cpython-313.pyc
│  │     │  │  │     ├─ errors.cpython-313.pyc
│  │     │  │  │     ├─ filesize.cpython-313.pyc
│  │     │  │  │     ├─ file_proxy.cpython-313.pyc
│  │     │  │  │     ├─ highlighter.cpython-313.pyc
│  │     │  │  │     ├─ json.cpython-313.pyc
│  │     │  │  │     ├─ jupyter.cpython-313.pyc
│  │     │  │  │     ├─ layout.cpython-313.pyc
│  │     │  │  │     ├─ live.cpython-313.pyc
│  │     │  │  │     ├─ live_render.cpython-313.pyc
│  │     │  │  │     ├─ logging.cpython-313.pyc
│  │     │  │  │     ├─ markup.cpython-313.pyc
│  │     │  │  │     ├─ measure.cpython-313.pyc
│  │     │  │  │     ├─ padding.cpython-313.pyc
│  │     │  │  │     ├─ pager.cpython-313.pyc
│  │     │  │  │     ├─ palette.cpython-313.pyc
│  │     │  │  │     ├─ panel.cpython-313.pyc
│  │     │  │  │     ├─ pretty.cpython-313.pyc
│  │     │  │  │     ├─ progress.cpython-313.pyc
│  │     │  │  │     ├─ progress_bar.cpython-313.pyc
│  │     │  │  │     ├─ prompt.cpython-313.pyc
│  │     │  │  │     ├─ protocol.cpython-313.pyc
│  │     │  │  │     ├─ region.cpython-313.pyc
│  │     │  │  │     ├─ repr.cpython-313.pyc
│  │     │  │  │     ├─ rule.cpython-313.pyc
│  │     │  │  │     ├─ scope.cpython-313.pyc
│  │     │  │  │     ├─ screen.cpython-313.pyc
│  │     │  │  │     ├─ segment.cpython-313.pyc
│  │     │  │  │     ├─ spinner.cpython-313.pyc
│  │     │  │  │     ├─ status.cpython-313.pyc
│  │     │  │  │     ├─ style.cpython-313.pyc
│  │     │  │  │     ├─ styled.cpython-313.pyc
│  │     │  │  │     ├─ syntax.cpython-313.pyc
│  │     │  │  │     ├─ table.cpython-313.pyc
│  │     │  │  │     ├─ terminal_theme.cpython-313.pyc
│  │     │  │  │     ├─ text.cpython-313.pyc
│  │     │  │  │     ├─ theme.cpython-313.pyc
│  │     │  │  │     ├─ themes.cpython-313.pyc
│  │     │  │  │     ├─ traceback.cpython-313.pyc
│  │     │  │  │     ├─ tree.cpython-313.pyc
│  │     │  │  │     ├─ _cell_widths.cpython-313.pyc
│  │     │  │  │     ├─ _emoji_codes.cpython-313.pyc
│  │     │  │  │     ├─ _emoji_replace.cpython-313.pyc
│  │     │  │  │     ├─ _export_format.cpython-313.pyc
│  │     │  │  │     ├─ _extension.cpython-313.pyc
│  │     │  │  │     ├─ _fileno.cpython-313.pyc
│  │     │  │  │     ├─ _inspect.cpython-313.pyc
│  │     │  │  │     ├─ _log_render.cpython-313.pyc
│  │     │  │  │     ├─ _loop.cpython-313.pyc
│  │     │  │  │     ├─ _null_file.cpython-313.pyc
│  │     │  │  │     ├─ _palettes.cpython-313.pyc
│  │     │  │  │     ├─ _pick.cpython-313.pyc
│  │     │  │  │     ├─ _ratio.cpython-313.pyc
│  │     │  │  │     ├─ _spinners.cpython-313.pyc
│  │     │  │  │     ├─ _stack.cpython-313.pyc
│  │     │  │  │     ├─ _timer.cpython-313.pyc
│  │     │  │  │     ├─ _win32_console.cpython-313.pyc
│  │     │  │  │     ├─ _windows.cpython-313.pyc
│  │     │  │  │     ├─ _windows_renderer.cpython-313.pyc
│  │     │  │  │     ├─ _wrap.cpython-313.pyc
│  │     │  │  │     ├─ __init__.cpython-313.pyc
│  │     │  │  │     └─ __main__.cpython-313.pyc
│  │     │  │  ├─ tomli
│  │     │  │  │  ├─ py.typed
│  │     │  │  │  ├─ _parser.py
│  │     │  │  │  ├─ _re.py
│  │     │  │  │  ├─ _types.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ _parser.cpython-313.pyc
│  │     │  │  │     ├─ _re.cpython-313.pyc
│  │     │  │  │     ├─ _types.cpython-313.pyc
│  │     │  │  │     └─ __init__.cpython-313.pyc
│  │     │  │  ├─ truststore
│  │     │  │  │  ├─ py.typed
│  │     │  │  │  ├─ _api.py
│  │     │  │  │  ├─ _macos.py
│  │     │  │  │  ├─ _openssl.py
│  │     │  │  │  ├─ _ssl_constants.py
│  │     │  │  │  ├─ _windows.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ _api.cpython-313.pyc
│  │     │  │  │     ├─ _macos.cpython-313.pyc
│  │     │  │  │     ├─ _openssl.cpython-313.pyc
│  │     │  │  │     ├─ _ssl_constants.cpython-313.pyc
│  │     │  │  │     ├─ _windows.cpython-313.pyc
│  │     │  │  │     └─ __init__.cpython-313.pyc
│  │     │  │  ├─ typing_extensions.py
│  │     │  │  ├─ urllib3
│  │     │  │  │  ├─ connection.py
│  │     │  │  │  ├─ connectionpool.py
│  │     │  │  │  ├─ contrib
│  │     │  │  │  │  ├─ appengine.py
│  │     │  │  │  │  ├─ ntlmpool.py
│  │     │  │  │  │  ├─ pyopenssl.py
│  │     │  │  │  │  ├─ securetransport.py
│  │     │  │  │  │  ├─ socks.py
│  │     │  │  │  │  ├─ _appengine_environ.py
│  │     │  │  │  │  ├─ _securetransport
│  │     │  │  │  │  │  ├─ bindings.py
│  │     │  │  │  │  │  ├─ low_level.py
│  │     │  │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  │  └─ __pycache__
│  │     │  │  │  │  │     ├─ bindings.cpython-313.pyc
│  │     │  │  │  │  │     ├─ low_level.cpython-313.pyc
│  │     │  │  │  │  │     └─ __init__.cpython-313.pyc
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  └─ __pycache__
│  │     │  │  │  │     ├─ appengine.cpython-313.pyc
│  │     │  │  │  │     ├─ ntlmpool.cpython-313.pyc
│  │     │  │  │  │     ├─ pyopenssl.cpython-313.pyc
│  │     │  │  │  │     ├─ securetransport.cpython-313.pyc
│  │     │  │  │  │     ├─ socks.cpython-313.pyc
│  │     │  │  │  │     ├─ _appengine_environ.cpython-313.pyc
│  │     │  │  │  │     └─ __init__.cpython-313.pyc
│  │     │  │  │  ├─ exceptions.py
│  │     │  │  │  ├─ fields.py
│  │     │  │  │  ├─ filepost.py
│  │     │  │  │  ├─ packages
│  │     │  │  │  │  ├─ backports
│  │     │  │  │  │  │  ├─ makefile.py
│  │     │  │  │  │  │  ├─ weakref_finalize.py
│  │     │  │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  │  └─ __pycache__
│  │     │  │  │  │  │     ├─ makefile.cpython-313.pyc
│  │     │  │  │  │  │     ├─ weakref_finalize.cpython-313.pyc
│  │     │  │  │  │  │     └─ __init__.cpython-313.pyc
│  │     │  │  │  │  ├─ six.py
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  └─ __pycache__
│  │     │  │  │  │     ├─ six.cpython-313.pyc
│  │     │  │  │  │     └─ __init__.cpython-313.pyc
│  │     │  │  │  ├─ poolmanager.py
│  │     │  │  │  ├─ request.py
│  │     │  │  │  ├─ response.py
│  │     │  │  │  ├─ util
│  │     │  │  │  │  ├─ connection.py
│  │     │  │  │  │  ├─ proxy.py
│  │     │  │  │  │  ├─ queue.py
│  │     │  │  │  │  ├─ request.py
│  │     │  │  │  │  ├─ response.py
│  │     │  │  │  │  ├─ retry.py
│  │     │  │  │  │  ├─ ssltransport.py
│  │     │  │  │  │  ├─ ssl_.py
│  │     │  │  │  │  ├─ ssl_match_hostname.py
│  │     │  │  │  │  ├─ timeout.py
│  │     │  │  │  │  ├─ url.py
│  │     │  │  │  │  ├─ wait.py
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  └─ __pycache__
│  │     │  │  │  │     ├─ connection.cpython-313.pyc
│  │     │  │  │  │     ├─ proxy.cpython-313.pyc
│  │     │  │  │  │     ├─ queue.cpython-313.pyc
│  │     │  │  │  │     ├─ request.cpython-313.pyc
│  │     │  │  │  │     ├─ response.cpython-313.pyc
│  │     │  │  │  │     ├─ retry.cpython-313.pyc
│  │     │  │  │  │     ├─ ssltransport.cpython-313.pyc
│  │     │  │  │  │     ├─ ssl_.cpython-313.pyc
│  │     │  │  │  │     ├─ ssl_match_hostname.cpython-313.pyc
│  │     │  │  │  │     ├─ timeout.cpython-313.pyc
│  │     │  │  │  │     ├─ url.cpython-313.pyc
│  │     │  │  │  │     ├─ wait.cpython-313.pyc
│  │     │  │  │  │     └─ __init__.cpython-313.pyc
│  │     │  │  │  ├─ _collections.py
│  │     │  │  │  ├─ _version.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ connection.cpython-313.pyc
│  │     │  │  │     ├─ connectionpool.cpython-313.pyc
│  │     │  │  │     ├─ exceptions.cpython-313.pyc
│  │     │  │  │     ├─ fields.cpython-313.pyc
│  │     │  │  │     ├─ filepost.cpython-313.pyc
│  │     │  │  │     ├─ poolmanager.cpython-313.pyc
│  │     │  │  │     ├─ request.cpython-313.pyc
│  │     │  │  │     ├─ response.cpython-313.pyc
│  │     │  │  │     ├─ _collections.cpython-313.pyc
│  │     │  │  │     ├─ _version.cpython-313.pyc
│  │     │  │  │     └─ __init__.cpython-313.pyc
│  │     │  │  ├─ vendor.txt
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ typing_extensions.cpython-313.pyc
│  │     │  │     └─ __init__.cpython-313.pyc
│  │     │  ├─ __init__.py
│  │     │  ├─ __main__.py
│  │     │  ├─ __pip-runner__.py
│  │     │  └─ __pycache__
│  │     │     ├─ __init__.cpython-313.pyc
│  │     │     ├─ __main__.cpython-313.pyc
│  │     │     └─ __pip-runner__.cpython-313.pyc
│  │     ├─ pip-24.3.1.dist-info
│  │     │  ├─ AUTHORS.txt
│  │     │  ├─ entry_points.txt
│  │     │  ├─ INSTALLER
│  │     │  ├─ LICENSE.txt
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  ├─ REQUESTED
│  │     │  ├─ top_level.txt
│  │     │  └─ WHEEL
│  │     ├─ psycopg2
│  │     │  ├─ errorcodes.py
│  │     │  ├─ errors.py
│  │     │  ├─ extensions.py
│  │     │  ├─ extras.py
│  │     │  ├─ pool.py
│  │     │  ├─ sql.py
│  │     │  ├─ tz.py
│  │     │  ├─ _ipaddress.py
│  │     │  ├─ _json.py
│  │     │  ├─ _psycopg.cp313-win_amd64.pyd
│  │     │  ├─ _range.py
│  │     │  ├─ __init__.py
│  │     │  └─ __pycache__
│  │     │     ├─ errorcodes.cpython-313.pyc
│  │     │     ├─ errors.cpython-313.pyc
│  │     │     ├─ extensions.cpython-313.pyc
│  │     │     ├─ extras.cpython-313.pyc
│  │     │     ├─ pool.cpython-313.pyc
│  │     │     ├─ sql.cpython-313.pyc
│  │     │     ├─ tz.cpython-313.pyc
│  │     │     ├─ _ipaddress.cpython-313.pyc
│  │     │     ├─ _json.cpython-313.pyc
│  │     │     ├─ _range.cpython-313.pyc
│  │     │     └─ __init__.cpython-313.pyc
│  │     ├─ psycopg2_binary-2.9.10.dist-info
│  │     │  ├─ DELVEWHEEL
│  │     │  ├─ INSTALLER
│  │     │  ├─ LICENSE
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  ├─ REQUESTED
│  │     │  ├─ top_level.txt
│  │     │  └─ WHEEL
│  │     ├─ psycopg2_binary.libs
│  │     │  ├─ libcrypto-3-x64-e57e1a41cc5d7f9b741c935f04fe4f2f.dll
│  │     │  ├─ libpq-29b01d8382d5824098bc0b4861813b70.dll
│  │     │  └─ libssl-3-x64-6b7807fd98efdd91c677351cd0a9f2d8.dll
│  │     ├─ pyasn1
│  │     │  ├─ codec
│  │     │  │  ├─ ber
│  │     │  │  │  ├─ decoder.py
│  │     │  │  │  ├─ encoder.py
│  │     │  │  │  ├─ eoo.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ decoder.cpython-313.pyc
│  │     │  │  │     ├─ encoder.cpython-313.pyc
│  │     │  │  │     ├─ eoo.cpython-313.pyc
│  │     │  │  │     └─ __init__.cpython-313.pyc
│  │     │  │  ├─ cer
│  │     │  │  │  ├─ decoder.py
│  │     │  │  │  ├─ encoder.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ decoder.cpython-313.pyc
│  │     │  │  │     ├─ encoder.cpython-313.pyc
│  │     │  │  │     └─ __init__.cpython-313.pyc
│  │     │  │  ├─ der
│  │     │  │  │  ├─ decoder.py
│  │     │  │  │  ├─ encoder.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ decoder.cpython-313.pyc
│  │     │  │  │     ├─ encoder.cpython-313.pyc
│  │     │  │  │     └─ __init__.cpython-313.pyc
│  │     │  │  ├─ native
│  │     │  │  │  ├─ decoder.py
│  │     │  │  │  ├─ encoder.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ decoder.cpython-313.pyc
│  │     │  │  │     ├─ encoder.cpython-313.pyc
│  │     │  │  │     └─ __init__.cpython-313.pyc
│  │     │  │  ├─ streaming.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ streaming.cpython-313.pyc
│  │     │  │     └─ __init__.cpython-313.pyc
│  │     │  ├─ compat
│  │     │  │  ├─ integer.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ integer.cpython-313.pyc
│  │     │  │     └─ __init__.cpython-313.pyc
│  │     │  ├─ debug.py
│  │     │  ├─ error.py
│  │     │  ├─ type
│  │     │  │  ├─ base.py
│  │     │  │  ├─ char.py
│  │     │  │  ├─ constraint.py
│  │     │  │  ├─ error.py
│  │     │  │  ├─ namedtype.py
│  │     │  │  ├─ namedval.py
│  │     │  │  ├─ opentype.py
│  │     │  │  ├─ tag.py
│  │     │  │  ├─ tagmap.py
│  │     │  │  ├─ univ.py
│  │     │  │  ├─ useful.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ base.cpython-313.pyc
│  │     │  │     ├─ char.cpython-313.pyc
│  │     │  │     ├─ constraint.cpython-313.pyc
│  │     │  │     ├─ error.cpython-313.pyc
│  │     │  │     ├─ namedtype.cpython-313.pyc
│  │     │  │     ├─ namedval.cpython-313.pyc
│  │     │  │     ├─ opentype.cpython-313.pyc
│  │     │  │     ├─ tag.cpython-313.pyc
│  │     │  │     ├─ tagmap.cpython-313.pyc
│  │     │  │     ├─ univ.cpython-313.pyc
│  │     │  │     ├─ useful.cpython-313.pyc
│  │     │  │     └─ __init__.cpython-313.pyc
│  │     │  ├─ __init__.py
│  │     │  └─ __pycache__
│  │     │     ├─ debug.cpython-313.pyc
│  │     │     ├─ error.cpython-313.pyc
│  │     │     └─ __init__.cpython-313.pyc
│  │     ├─ pyasn1-0.6.3.dist-info
│  │     │  ├─ INSTALLER
│  │     │  ├─ licenses
│  │     │  │  └─ LICENSE.rst
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  ├─ top_level.txt
│  │     │  ├─ WHEEL
│  │     │  └─ zip-safe
│  │     ├─ pyasn1_modules
│  │     │  ├─ pem.py
│  │     │  ├─ rfc1155.py
│  │     │  ├─ rfc1157.py
│  │     │  ├─ rfc1901.py
│  │     │  ├─ rfc1902.py
│  │     │  ├─ rfc1905.py
│  │     │  ├─ rfc2251.py
│  │     │  ├─ rfc2314.py
│  │     │  ├─ rfc2315.py
│  │     │  ├─ rfc2437.py
│  │     │  ├─ rfc2459.py
│  │     │  ├─ rfc2511.py
│  │     │  ├─ rfc2560.py
│  │     │  ├─ rfc2631.py
│  │     │  ├─ rfc2634.py
│  │     │  ├─ rfc2876.py
│  │     │  ├─ rfc2985.py
│  │     │  ├─ rfc2986.py
│  │     │  ├─ rfc3058.py
│  │     │  ├─ rfc3114.py
│  │     │  ├─ rfc3125.py
│  │     │  ├─ rfc3161.py
│  │     │  ├─ rfc3274.py
│  │     │  ├─ rfc3279.py
│  │     │  ├─ rfc3280.py
│  │     │  ├─ rfc3281.py
│  │     │  ├─ rfc3370.py
│  │     │  ├─ rfc3412.py
│  │     │  ├─ rfc3414.py
│  │     │  ├─ rfc3447.py
│  │     │  ├─ rfc3537.py
│  │     │  ├─ rfc3560.py
│  │     │  ├─ rfc3565.py
│  │     │  ├─ rfc3657.py
│  │     │  ├─ rfc3709.py
│  │     │  ├─ rfc3739.py
│  │     │  ├─ rfc3770.py
│  │     │  ├─ rfc3779.py
│  │     │  ├─ rfc3820.py
│  │     │  ├─ rfc3852.py
│  │     │  ├─ rfc4010.py
│  │     │  ├─ rfc4043.py
│  │     │  ├─ rfc4055.py
│  │     │  ├─ rfc4073.py
│  │     │  ├─ rfc4108.py
│  │     │  ├─ rfc4210.py
│  │     │  ├─ rfc4211.py
│  │     │  ├─ rfc4334.py
│  │     │  ├─ rfc4357.py
│  │     │  ├─ rfc4387.py
│  │     │  ├─ rfc4476.py
│  │     │  ├─ rfc4490.py
│  │     │  ├─ rfc4491.py
│  │     │  ├─ rfc4683.py
│  │     │  ├─ rfc4985.py
│  │     │  ├─ rfc5035.py
│  │     │  ├─ rfc5083.py
│  │     │  ├─ rfc5084.py
│  │     │  ├─ rfc5126.py
│  │     │  ├─ rfc5208.py
│  │     │  ├─ rfc5275.py
│  │     │  ├─ rfc5280.py
│  │     │  ├─ rfc5480.py
│  │     │  ├─ rfc5636.py
│  │     │  ├─ rfc5639.py
│  │     │  ├─ rfc5649.py
│  │     │  ├─ rfc5652.py
│  │     │  ├─ rfc5697.py
│  │     │  ├─ rfc5751.py
│  │     │  ├─ rfc5752.py
│  │     │  ├─ rfc5753.py
│  │     │  ├─ rfc5755.py
│  │     │  ├─ rfc5913.py
│  │     │  ├─ rfc5914.py
│  │     │  ├─ rfc5915.py
│  │     │  ├─ rfc5916.py
│  │     │  ├─ rfc5917.py
│  │     │  ├─ rfc5924.py
│  │     │  ├─ rfc5934.py
│  │     │  ├─ rfc5940.py
│  │     │  ├─ rfc5958.py
│  │     │  ├─ rfc5990.py
│  │     │  ├─ rfc6010.py
│  │     │  ├─ rfc6019.py
│  │     │  ├─ rfc6031.py
│  │     │  ├─ rfc6032.py
│  │     │  ├─ rfc6120.py
│  │     │  ├─ rfc6170.py
│  │     │  ├─ rfc6187.py
│  │     │  ├─ rfc6210.py
│  │     │  ├─ rfc6211.py
│  │     │  ├─ rfc6402.py
│  │     │  ├─ rfc6482.py
│  │     │  ├─ rfc6486.py
│  │     │  ├─ rfc6487.py
│  │     │  ├─ rfc6664.py
│  │     │  ├─ rfc6955.py
│  │     │  ├─ rfc6960.py
│  │     │  ├─ rfc7030.py
│  │     │  ├─ rfc7191.py
│  │     │  ├─ rfc7229.py
│  │     │  ├─ rfc7292.py
│  │     │  ├─ rfc7296.py
│  │     │  ├─ rfc7508.py
│  │     │  ├─ rfc7585.py
│  │     │  ├─ rfc7633.py
│  │     │  ├─ rfc7773.py
│  │     │  ├─ rfc7894.py
│  │     │  ├─ rfc7906.py
│  │     │  ├─ rfc7914.py
│  │     │  ├─ rfc8017.py
│  │     │  ├─ rfc8018.py
│  │     │  ├─ rfc8103.py
│  │     │  ├─ rfc8209.py
│  │     │  ├─ rfc8226.py
│  │     │  ├─ rfc8358.py
│  │     │  ├─ rfc8360.py
│  │     │  ├─ rfc8398.py
│  │     │  ├─ rfc8410.py
│  │     │  ├─ rfc8418.py
│  │     │  ├─ rfc8419.py
│  │     │  ├─ rfc8479.py
│  │     │  ├─ rfc8494.py
│  │     │  ├─ rfc8520.py
│  │     │  ├─ rfc8619.py
│  │     │  ├─ rfc8649.py
│  │     │  ├─ rfc8692.py
│  │     │  ├─ rfc8696.py
│  │     │  ├─ rfc8702.py
│  │     │  ├─ rfc8708.py
│  │     │  ├─ rfc8769.py
│  │     │  ├─ __init__.py
│  │     │  └─ __pycache__
│  │     │     ├─ pem.cpython-313.pyc
│  │     │     ├─ rfc1155.cpython-313.pyc
│  │     │     ├─ rfc1157.cpython-313.pyc
│  │     │     ├─ rfc1901.cpython-313.pyc
│  │     │     ├─ rfc1902.cpython-313.pyc
│  │     │     ├─ rfc1905.cpython-313.pyc
│  │     │     ├─ rfc2251.cpython-313.pyc
│  │     │     ├─ rfc2314.cpython-313.pyc
│  │     │     ├─ rfc2315.cpython-313.pyc
│  │     │     ├─ rfc2437.cpython-313.pyc
│  │     │     ├─ rfc2459.cpython-313.pyc
│  │     │     ├─ rfc2511.cpython-313.pyc
│  │     │     ├─ rfc2560.cpython-313.pyc
│  │     │     ├─ rfc2631.cpython-313.pyc
│  │     │     ├─ rfc2634.cpython-313.pyc
│  │     │     ├─ rfc2876.cpython-313.pyc
│  │     │     ├─ rfc2985.cpython-313.pyc
│  │     │     ├─ rfc2986.cpython-313.pyc
│  │     │     ├─ rfc3058.cpython-313.pyc
│  │     │     ├─ rfc3114.cpython-313.pyc
│  │     │     ├─ rfc3125.cpython-313.pyc
│  │     │     ├─ rfc3161.cpython-313.pyc
│  │     │     ├─ rfc3274.cpython-313.pyc
│  │     │     ├─ rfc3279.cpython-313.pyc
│  │     │     ├─ rfc3280.cpython-313.pyc
│  │     │     ├─ rfc3281.cpython-313.pyc
│  │     │     ├─ rfc3370.cpython-313.pyc
│  │     │     ├─ rfc3412.cpython-313.pyc
│  │     │     ├─ rfc3414.cpython-313.pyc
│  │     │     ├─ rfc3447.cpython-313.pyc
│  │     │     ├─ rfc3537.cpython-313.pyc
│  │     │     ├─ rfc3560.cpython-313.pyc
│  │     │     ├─ rfc3565.cpython-313.pyc
│  │     │     ├─ rfc3657.cpython-313.pyc
│  │     │     ├─ rfc3709.cpython-313.pyc
│  │     │     ├─ rfc3739.cpython-313.pyc
│  │     │     ├─ rfc3770.cpython-313.pyc
│  │     │     ├─ rfc3779.cpython-313.pyc
│  │     │     ├─ rfc3820.cpython-313.pyc
│  │     │     ├─ rfc3852.cpython-313.pyc
│  │     │     ├─ rfc4010.cpython-313.pyc
│  │     │     ├─ rfc4043.cpython-313.pyc
│  │     │     ├─ rfc4055.cpython-313.pyc
│  │     │     ├─ rfc4073.cpython-313.pyc
│  │     │     ├─ rfc4108.cpython-313.pyc
│  │     │     ├─ rfc4210.cpython-313.pyc
│  │     │     ├─ rfc4211.cpython-313.pyc
│  │     │     ├─ rfc4334.cpython-313.pyc
│  │     │     ├─ rfc4357.cpython-313.pyc
│  │     │     ├─ rfc4387.cpython-313.pyc
│  │     │     ├─ rfc4476.cpython-313.pyc
│  │     │     ├─ rfc4490.cpython-313.pyc
│  │     │     ├─ rfc4491.cpython-313.pyc
│  │     │     ├─ rfc4683.cpython-313.pyc
│  │     │     ├─ rfc4985.cpython-313.pyc
│  │     │     ├─ rfc5035.cpython-313.pyc
│  │     │     ├─ rfc5083.cpython-313.pyc
│  │     │     ├─ rfc5084.cpython-313.pyc
│  │     │     ├─ rfc5126.cpython-313.pyc
│  │     │     ├─ rfc5208.cpython-313.pyc
│  │     │     ├─ rfc5275.cpython-313.pyc
│  │     │     ├─ rfc5280.cpython-313.pyc
│  │     │     ├─ rfc5480.cpython-313.pyc
│  │     │     ├─ rfc5636.cpython-313.pyc
│  │     │     ├─ rfc5639.cpython-313.pyc
│  │     │     ├─ rfc5649.cpython-313.pyc
│  │     │     ├─ rfc5652.cpython-313.pyc
│  │     │     ├─ rfc5697.cpython-313.pyc
│  │     │     ├─ rfc5751.cpython-313.pyc
│  │     │     ├─ rfc5752.cpython-313.pyc
│  │     │     ├─ rfc5753.cpython-313.pyc
│  │     │     ├─ rfc5755.cpython-313.pyc
│  │     │     ├─ rfc5913.cpython-313.pyc
│  │     │     ├─ rfc5914.cpython-313.pyc
│  │     │     ├─ rfc5915.cpython-313.pyc
│  │     │     ├─ rfc5916.cpython-313.pyc
│  │     │     ├─ rfc5917.cpython-313.pyc
│  │     │     ├─ rfc5924.cpython-313.pyc
│  │     │     ├─ rfc5934.cpython-313.pyc
│  │     │     ├─ rfc5940.cpython-313.pyc
│  │     │     ├─ rfc5958.cpython-313.pyc
│  │     │     ├─ rfc5990.cpython-313.pyc
│  │     │     ├─ rfc6010.cpython-313.pyc
│  │     │     ├─ rfc6019.cpython-313.pyc
│  │     │     ├─ rfc6031.cpython-313.pyc
│  │     │     ├─ rfc6032.cpython-313.pyc
│  │     │     ├─ rfc6120.cpython-313.pyc
│  │     │     ├─ rfc6170.cpython-313.pyc
│  │     │     ├─ rfc6187.cpython-313.pyc
│  │     │     ├─ rfc6210.cpython-313.pyc
│  │     │     ├─ rfc6211.cpython-313.pyc
│  │     │     ├─ rfc6402.cpython-313.pyc
│  │     │     ├─ rfc6482.cpython-313.pyc
│  │     │     ├─ rfc6486.cpython-313.pyc
│  │     │     ├─ rfc6487.cpython-313.pyc
│  │     │     ├─ rfc6664.cpython-313.pyc
│  │     │     ├─ rfc6955.cpython-313.pyc
│  │     │     ├─ rfc6960.cpython-313.pyc
│  │     │     ├─ rfc7030.cpython-313.pyc
│  │     │     ├─ rfc7191.cpython-313.pyc
│  │     │     ├─ rfc7229.cpython-313.pyc
│  │     │     ├─ rfc7292.cpython-313.pyc
│  │     │     ├─ rfc7296.cpython-313.pyc
│  │     │     ├─ rfc7508.cpython-313.pyc
│  │     │     ├─ rfc7585.cpython-313.pyc
│  │     │     ├─ rfc7633.cpython-313.pyc
│  │     │     ├─ rfc7773.cpython-313.pyc
│  │     │     ├─ rfc7894.cpython-313.pyc
│  │     │     ├─ rfc7906.cpython-313.pyc
│  │     │     ├─ rfc7914.cpython-313.pyc
│  │     │     ├─ rfc8017.cpython-313.pyc
│  │     │     ├─ rfc8018.cpython-313.pyc
│  │     │     ├─ rfc8103.cpython-313.pyc
│  │     │     ├─ rfc8209.cpython-313.pyc
│  │     │     ├─ rfc8226.cpython-313.pyc
│  │     │     ├─ rfc8358.cpython-313.pyc
│  │     │     ├─ rfc8360.cpython-313.pyc
│  │     │     ├─ rfc8398.cpython-313.pyc
│  │     │     ├─ rfc8410.cpython-313.pyc
│  │     │     ├─ rfc8418.cpython-313.pyc
│  │     │     ├─ rfc8419.cpython-313.pyc
│  │     │     ├─ rfc8479.cpython-313.pyc
│  │     │     ├─ rfc8494.cpython-313.pyc
│  │     │     ├─ rfc8520.cpython-313.pyc
│  │     │     ├─ rfc8619.cpython-313.pyc
│  │     │     ├─ rfc8649.cpython-313.pyc
│  │     │     ├─ rfc8692.cpython-313.pyc
│  │     │     ├─ rfc8696.cpython-313.pyc
│  │     │     ├─ rfc8702.cpython-313.pyc
│  │     │     ├─ rfc8708.cpython-313.pyc
│  │     │     ├─ rfc8769.cpython-313.pyc
│  │     │     └─ __init__.cpython-313.pyc
│  │     ├─ pyasn1_modules-0.4.2.dist-info
│  │     │  ├─ INSTALLER
│  │     │  ├─ licenses
│  │     │  │  └─ LICENSE.txt
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  ├─ top_level.txt
│  │     │  ├─ WHEEL
│  │     │  └─ zip-safe
│  │     ├─ pycparser
│  │     │  ├─ ast_transforms.py
│  │     │  ├─ c_ast.py
│  │     │  ├─ c_generator.py
│  │     │  ├─ c_lexer.py
│  │     │  ├─ c_parser.py
│  │     │  ├─ _ast_gen.py
│  │     │  ├─ _c_ast.cfg
│  │     │  ├─ __init__.py
│  │     │  └─ __pycache__
│  │     │     ├─ ast_transforms.cpython-313.pyc
│  │     │     ├─ c_ast.cpython-313.pyc
│  │     │     ├─ c_generator.cpython-313.pyc
│  │     │     ├─ c_lexer.cpython-313.pyc
│  │     │     ├─ c_parser.cpython-313.pyc
│  │     │     ├─ _ast_gen.cpython-313.pyc
│  │     │     └─ __init__.cpython-313.pyc
│  │     ├─ pycparser-3.0.dist-info
│  │     │  ├─ INSTALLER
│  │     │  ├─ licenses
│  │     │  │  └─ LICENSE
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  ├─ top_level.txt
│  │     │  └─ WHEEL
│  │     ├─ pydantic
│  │     │  ├─ aliases.py
│  │     │  ├─ alias_generators.py
│  │     │  ├─ annotated_handlers.py
│  │     │  ├─ class_validators.py
│  │     │  ├─ color.py
│  │     │  ├─ config.py
│  │     │  ├─ dataclasses.py
│  │     │  ├─ datetime_parse.py
│  │     │  ├─ decorator.py
│  │     │  ├─ deprecated
│  │     │  │  ├─ class_validators.py
│  │     │  │  ├─ config.py
│  │     │  │  ├─ copy_internals.py
│  │     │  │  ├─ decorator.py
│  │     │  │  ├─ json.py
│  │     │  │  ├─ parse.py
│  │     │  │  ├─ tools.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ class_validators.cpython-313.pyc
│  │     │  │     ├─ config.cpython-313.pyc
│  │     │  │     ├─ copy_internals.cpython-313.pyc
│  │     │  │     ├─ decorator.cpython-313.pyc
│  │     │  │     ├─ json.cpython-313.pyc
│  │     │  │     ├─ parse.cpython-313.pyc
│  │     │  │     ├─ tools.cpython-313.pyc
│  │     │  │     └─ __init__.cpython-313.pyc
│  │     │  ├─ env_settings.py
│  │     │  ├─ errors.py
│  │     │  ├─ error_wrappers.py
│  │     │  ├─ experimental
│  │     │  │  ├─ pipeline.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ pipeline.cpython-313.pyc
│  │     │  │     └─ __init__.cpython-313.pyc
│  │     │  ├─ fields.py
│  │     │  ├─ functional_serializers.py
│  │     │  ├─ functional_validators.py
│  │     │  ├─ generics.py
│  │     │  ├─ json.py
│  │     │  ├─ json_schema.py
│  │     │  ├─ main.py
│  │     │  ├─ mypy.py
│  │     │  ├─ networks.py
│  │     │  ├─ parse.py
│  │     │  ├─ plugin
│  │     │  │  ├─ _loader.py
│  │     │  │  ├─ _schema_validator.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ _loader.cpython-313.pyc
│  │     │  │     ├─ _schema_validator.cpython-313.pyc
│  │     │  │     └─ __init__.cpython-313.pyc
│  │     │  ├─ py.typed
│  │     │  ├─ root_model.py
│  │     │  ├─ schema.py
│  │     │  ├─ tools.py
│  │     │  ├─ types.py
│  │     │  ├─ type_adapter.py
│  │     │  ├─ typing.py
│  │     │  ├─ utils.py
│  │     │  ├─ v1
│  │     │  │  ├─ annotated_types.py
│  │     │  │  ├─ class_validators.py
│  │     │  │  ├─ color.py
│  │     │  │  ├─ config.py
│  │     │  │  ├─ dataclasses.py
│  │     │  │  ├─ datetime_parse.py
│  │     │  │  ├─ decorator.py
│  │     │  │  ├─ env_settings.py
│  │     │  │  ├─ errors.py
│  │     │  │  ├─ error_wrappers.py
│  │     │  │  ├─ fields.py
│  │     │  │  ├─ generics.py
│  │     │  │  ├─ json.py
│  │     │  │  ├─ main.py
│  │     │  │  ├─ mypy.py
│  │     │  │  ├─ networks.py
│  │     │  │  ├─ parse.py
│  │     │  │  ├─ py.typed
│  │     │  │  ├─ schema.py
│  │     │  │  ├─ tools.py
│  │     │  │  ├─ types.py
│  │     │  │  ├─ typing.py
│  │     │  │  ├─ utils.py
│  │     │  │  ├─ validators.py
│  │     │  │  ├─ version.py
│  │     │  │  ├─ _hypothesis_plugin.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ annotated_types.cpython-313.pyc
│  │     │  │     ├─ class_validators.cpython-313.pyc
│  │     │  │     ├─ color.cpython-313.pyc
│  │     │  │     ├─ config.cpython-313.pyc
│  │     │  │     ├─ dataclasses.cpython-313.pyc
│  │     │  │     ├─ datetime_parse.cpython-313.pyc
│  │     │  │     ├─ decorator.cpython-313.pyc
│  │     │  │     ├─ env_settings.cpython-313.pyc
│  │     │  │     ├─ errors.cpython-313.pyc
│  │     │  │     ├─ error_wrappers.cpython-313.pyc
│  │     │  │     ├─ fields.cpython-313.pyc
│  │     │  │     ├─ generics.cpython-313.pyc
│  │     │  │     ├─ json.cpython-313.pyc
│  │     │  │     ├─ main.cpython-313.pyc
│  │     │  │     ├─ mypy.cpython-313.pyc
│  │     │  │     ├─ networks.cpython-313.pyc
│  │     │  │     ├─ parse.cpython-313.pyc
│  │     │  │     ├─ schema.cpython-313.pyc
│  │     │  │     ├─ tools.cpython-313.pyc
│  │     │  │     ├─ types.cpython-313.pyc
│  │     │  │     ├─ typing.cpython-313.pyc
│  │     │  │     ├─ utils.cpython-313.pyc
│  │     │  │     ├─ validators.cpython-313.pyc
│  │     │  │     ├─ version.cpython-313.pyc
│  │     │  │     ├─ _hypothesis_plugin.cpython-313.pyc
│  │     │  │     └─ __init__.cpython-313.pyc
│  │     │  ├─ validate_call_decorator.py
│  │     │  ├─ validators.py
│  │     │  ├─ version.py
│  │     │  ├─ warnings.py
│  │     │  ├─ _internal
│  │     │  │  ├─ _config.py
│  │     │  │  ├─ _core_metadata.py
│  │     │  │  ├─ _core_utils.py
│  │     │  │  ├─ _dataclasses.py
│  │     │  │  ├─ _decorators.py
│  │     │  │  ├─ _decorators_v1.py
│  │     │  │  ├─ _discriminated_union.py
│  │     │  │  ├─ _docs_extraction.py
│  │     │  │  ├─ _fields.py
│  │     │  │  ├─ _forward_ref.py
│  │     │  │  ├─ _generate_schema.py
│  │     │  │  ├─ _generics.py
│  │     │  │  ├─ _git.py
│  │     │  │  ├─ _import_utils.py
│  │     │  │  ├─ _internal_dataclass.py
│  │     │  │  ├─ _known_annotated_metadata.py
│  │     │  │  ├─ _mock_val_ser.py
│  │     │  │  ├─ _model_construction.py
│  │     │  │  ├─ _namespace_utils.py
│  │     │  │  ├─ _repr.py
│  │     │  │  ├─ _schema_generation_shared.py
│  │     │  │  ├─ _serializers.py
│  │     │  │  ├─ _signature.py
│  │     │  │  ├─ _std_types_schema.py
│  │     │  │  ├─ _typing_extra.py
│  │     │  │  ├─ _utils.py
│  │     │  │  ├─ _validate_call.py
│  │     │  │  ├─ _validators.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ _config.cpython-313.pyc
│  │     │  │     ├─ _core_metadata.cpython-313.pyc
│  │     │  │     ├─ _core_utils.cpython-313.pyc
│  │     │  │     ├─ _dataclasses.cpython-313.pyc
│  │     │  │     ├─ _decorators.cpython-313.pyc
│  │     │  │     ├─ _decorators_v1.cpython-313.pyc
│  │     │  │     ├─ _discriminated_union.cpython-313.pyc
│  │     │  │     ├─ _docs_extraction.cpython-313.pyc
│  │     │  │     ├─ _fields.cpython-313.pyc
│  │     │  │     ├─ _forward_ref.cpython-313.pyc
│  │     │  │     ├─ _generate_schema.cpython-313.pyc
│  │     │  │     ├─ _generics.cpython-313.pyc
│  │     │  │     ├─ _git.cpython-313.pyc
│  │     │  │     ├─ _import_utils.cpython-313.pyc
│  │     │  │     ├─ _internal_dataclass.cpython-313.pyc
│  │     │  │     ├─ _known_annotated_metadata.cpython-313.pyc
│  │     │  │     ├─ _mock_val_ser.cpython-313.pyc
│  │     │  │     ├─ _model_construction.cpython-313.pyc
│  │     │  │     ├─ _namespace_utils.cpython-313.pyc
│  │     │  │     ├─ _repr.cpython-313.pyc
│  │     │  │     ├─ _schema_generation_shared.cpython-313.pyc
│  │     │  │     ├─ _serializers.cpython-313.pyc
│  │     │  │     ├─ _signature.cpython-313.pyc
│  │     │  │     ├─ _std_types_schema.cpython-313.pyc
│  │     │  │     ├─ _typing_extra.cpython-313.pyc
│  │     │  │     ├─ _utils.cpython-313.pyc
│  │     │  │     ├─ _validate_call.cpython-313.pyc
│  │     │  │     ├─ _validators.cpython-313.pyc
│  │     │  │     └─ __init__.cpython-313.pyc
│  │     │  ├─ _migration.py
│  │     │  ├─ __init__.py
│  │     │  └─ __pycache__
│  │     │     ├─ aliases.cpython-313.pyc
│  │     │     ├─ alias_generators.cpython-313.pyc
│  │     │     ├─ annotated_handlers.cpython-313.pyc
│  │     │     ├─ class_validators.cpython-313.pyc
│  │     │     ├─ color.cpython-313.pyc
│  │     │     ├─ config.cpython-313.pyc
│  │     │     ├─ dataclasses.cpython-313.pyc
│  │     │     ├─ datetime_parse.cpython-313.pyc
│  │     │     ├─ decorator.cpython-313.pyc
│  │     │     ├─ env_settings.cpython-313.pyc
│  │     │     ├─ errors.cpython-313.pyc
│  │     │     ├─ error_wrappers.cpython-313.pyc
│  │     │     ├─ fields.cpython-313.pyc
│  │     │     ├─ functional_serializers.cpython-313.pyc
│  │     │     ├─ functional_validators.cpython-313.pyc
│  │     │     ├─ generics.cpython-313.pyc
│  │     │     ├─ json.cpython-313.pyc
│  │     │     ├─ json_schema.cpython-313.pyc
│  │     │     ├─ main.cpython-313.pyc
│  │     │     ├─ mypy.cpython-313.pyc
│  │     │     ├─ networks.cpython-313.pyc
│  │     │     ├─ parse.cpython-313.pyc
│  │     │     ├─ root_model.cpython-313.pyc
│  │     │     ├─ schema.cpython-313.pyc
│  │     │     ├─ tools.cpython-313.pyc
│  │     │     ├─ types.cpython-313.pyc
│  │     │     ├─ type_adapter.cpython-313.pyc
│  │     │     ├─ typing.cpython-313.pyc
│  │     │     ├─ utils.cpython-313.pyc
│  │     │     ├─ validate_call_decorator.cpython-313.pyc
│  │     │     ├─ validators.cpython-313.pyc
│  │     │     ├─ version.cpython-313.pyc
│  │     │     ├─ warnings.cpython-313.pyc
│  │     │     ├─ _migration.cpython-313.pyc
│  │     │     └─ __init__.cpython-313.pyc
│  │     ├─ pydantic-2.10.4.dist-info
│  │     │  ├─ INSTALLER
│  │     │  ├─ licenses
│  │     │  │  └─ LICENSE
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  ├─ REQUESTED
│  │     │  └─ WHEEL
│  │     ├─ pydantic_core
│  │     │  ├─ core_schema.py
│  │     │  ├─ py.typed
│  │     │  ├─ _pydantic_core.cp313-win_amd64.pyd
│  │     │  ├─ _pydantic_core.pyi
│  │     │  ├─ __init__.py
│  │     │  └─ __pycache__
│  │     │     ├─ core_schema.cpython-313.pyc
│  │     │     └─ __init__.cpython-313.pyc
│  │     ├─ pydantic_core-2.27.2.dist-info
│  │     │  ├─ INSTALLER
│  │     │  ├─ licenses
│  │     │  │  └─ LICENSE
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  └─ WHEEL
│  │     ├─ pylab.py
│  │     ├─ pyparsing
│  │     │  ├─ actions.py
│  │     │  ├─ ai
│  │     │  │  ├─ best_practices.md
│  │     │  │  ├─ show_best_practices
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  ├─ __main__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ __init__.cpython-313.pyc
│  │     │  │  │     └─ __main__.cpython-313.pyc
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     └─ __init__.cpython-313.pyc
│  │     │  ├─ common.py
│  │     │  ├─ core.py
│  │     │  ├─ diagram
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     └─ __init__.cpython-313.pyc
│  │     │  ├─ exceptions.py
│  │     │  ├─ helpers.py
│  │     │  ├─ py.typed
│  │     │  ├─ results.py
│  │     │  ├─ testing.py
│  │     │  ├─ tools
│  │     │  │  ├─ cvt_pyparsing_pep8_names.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ cvt_pyparsing_pep8_names.cpython-313.pyc
│  │     │  │     └─ __init__.cpython-313.pyc
│  │     │  ├─ unicode.py
│  │     │  ├─ util.py
│  │     │  ├─ warnings.py
│  │     │  ├─ __init__.py
│  │     │  └─ __pycache__
│  │     │     ├─ actions.cpython-313.pyc
│  │     │     ├─ common.cpython-313.pyc
│  │     │     ├─ core.cpython-313.pyc
│  │     │     ├─ exceptions.cpython-313.pyc
│  │     │     ├─ helpers.cpython-313.pyc
│  │     │     ├─ results.cpython-313.pyc
│  │     │     ├─ testing.cpython-313.pyc
│  │     │     ├─ unicode.cpython-313.pyc
│  │     │     ├─ util.cpython-313.pyc
│  │     │     ├─ warnings.cpython-313.pyc
│  │     │     └─ __init__.cpython-313.pyc
│  │     ├─ pyparsing-3.3.2.dist-info
│  │     │  ├─ INSTALLER
│  │     │  ├─ licenses
│  │     │  │  └─ LICENSE
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  └─ WHEEL
│  │     ├─ python_dateutil-2.9.0.post0.dist-info
│  │     │  ├─ INSTALLER
│  │     │  ├─ LICENSE
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  ├─ top_level.txt
│  │     │  ├─ WHEEL
│  │     │  └─ zip-safe
│  │     ├─ python_dotenv-1.0.1.dist-info
│  │     │  ├─ entry_points.txt
│  │     │  ├─ INSTALLER
│  │     │  ├─ LICENSE
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  ├─ REQUESTED
│  │     │  ├─ top_level.txt
│  │     │  └─ WHEEL
│  │     ├─ python_multipart
│  │     │  ├─ decoders.py
│  │     │  ├─ exceptions.py
│  │     │  ├─ multipart.py
│  │     │  ├─ py.typed
│  │     │  ├─ __init__.py
│  │     │  └─ __pycache__
│  │     │     ├─ decoders.cpython-313.pyc
│  │     │     ├─ exceptions.cpython-313.pyc
│  │     │     ├─ multipart.cpython-313.pyc
│  │     │     └─ __init__.cpython-313.pyc
│  │     ├─ python_multipart-0.0.20.dist-info
│  │     │  ├─ INSTALLER
│  │     │  ├─ licenses
│  │     │  │  └─ LICENSE.txt
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  ├─ REQUESTED
│  │     │  └─ WHEEL
│  │     ├─ requests
│  │     │  ├─ adapters.py
│  │     │  ├─ api.py
│  │     │  ├─ auth.py
│  │     │  ├─ certs.py
│  │     │  ├─ compat.py
│  │     │  ├─ cookies.py
│  │     │  ├─ exceptions.py
│  │     │  ├─ help.py
│  │     │  ├─ hooks.py
│  │     │  ├─ models.py
│  │     │  ├─ packages.py
│  │     │  ├─ sessions.py
│  │     │  ├─ status_codes.py
│  │     │  ├─ structures.py
│  │     │  ├─ utils.py
│  │     │  ├─ _internal_utils.py
│  │     │  ├─ __init__.py
│  │     │  ├─ __pycache__
│  │     │  │  ├─ adapters.cpython-313.pyc
│  │     │  │  ├─ api.cpython-313.pyc
│  │     │  │  ├─ auth.cpython-313.pyc
│  │     │  │  ├─ certs.cpython-313.pyc
│  │     │  │  ├─ compat.cpython-313.pyc
│  │     │  │  ├─ cookies.cpython-313.pyc
│  │     │  │  ├─ exceptions.cpython-313.pyc
│  │     │  │  ├─ help.cpython-313.pyc
│  │     │  │  ├─ hooks.cpython-313.pyc
│  │     │  │  ├─ models.cpython-313.pyc
│  │     │  │  ├─ packages.cpython-313.pyc
│  │     │  │  ├─ sessions.cpython-313.pyc
│  │     │  │  ├─ status_codes.cpython-313.pyc
│  │     │  │  ├─ structures.cpython-313.pyc
│  │     │  │  ├─ utils.cpython-313.pyc
│  │     │  │  ├─ _internal_utils.cpython-313.pyc
│  │     │  │  ├─ __init__.cpython-313.pyc
│  │     │  │  └─ __version__.cpython-313.pyc
│  │     │  └─ __version__.py
│  │     ├─ requests-2.32.3.dist-info
│  │     │  ├─ INSTALLER
│  │     │  ├─ LICENSE
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  ├─ REQUESTED
│  │     │  ├─ top_level.txt
│  │     │  └─ WHEEL
│  │     ├─ six-1.17.0.dist-info
│  │     │  ├─ INSTALLER
│  │     │  ├─ LICENSE
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  ├─ top_level.txt
│  │     │  └─ WHEEL
│  │     ├─ six.py
│  │     ├─ sniffio
│  │     │  ├─ py.typed
│  │     │  ├─ _impl.py
│  │     │  ├─ _tests
│  │     │  │  ├─ test_sniffio.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ test_sniffio.cpython-313.pyc
│  │     │  │     └─ __init__.cpython-313.pyc
│  │     │  ├─ _version.py
│  │     │  ├─ __init__.py
│  │     │  └─ __pycache__
│  │     │     ├─ _impl.cpython-313.pyc
│  │     │     ├─ _version.cpython-313.pyc
│  │     │     └─ __init__.cpython-313.pyc
│  │     ├─ sniffio-1.3.1.dist-info
│  │     │  ├─ INSTALLER
│  │     │  ├─ LICENSE
│  │     │  ├─ LICENSE.APACHE2
│  │     │  ├─ LICENSE.MIT
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  ├─ top_level.txt
│  │     │  └─ WHEEL
│  │     ├─ sounddevice-0.5.5.dist-info
│  │     │  ├─ INSTALLER
│  │     │  ├─ licenses
│  │     │  │  └─ LICENSE
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  ├─ top_level.txt
│  │     │  └─ WHEEL
│  │     ├─ sounddevice.py
│  │     ├─ starlette
│  │     │  ├─ applications.py
│  │     │  ├─ authentication.py
│  │     │  ├─ background.py
│  │     │  ├─ concurrency.py
│  │     │  ├─ config.py
│  │     │  ├─ convertors.py
│  │     │  ├─ datastructures.py
│  │     │  ├─ endpoints.py
│  │     │  ├─ exceptions.py
│  │     │  ├─ formparsers.py
│  │     │  ├─ middleware
│  │     │  │  ├─ authentication.py
│  │     │  │  ├─ base.py
│  │     │  │  ├─ cors.py
│  │     │  │  ├─ errors.py
│  │     │  │  ├─ exceptions.py
│  │     │  │  ├─ gzip.py
│  │     │  │  ├─ httpsredirect.py
│  │     │  │  ├─ sessions.py
│  │     │  │  ├─ trustedhost.py
│  │     │  │  ├─ wsgi.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ authentication.cpython-313.pyc
│  │     │  │     ├─ base.cpython-313.pyc
│  │     │  │     ├─ cors.cpython-313.pyc
│  │     │  │     ├─ errors.cpython-313.pyc
│  │     │  │     ├─ exceptions.cpython-313.pyc
│  │     │  │     ├─ gzip.cpython-313.pyc
│  │     │  │     ├─ httpsredirect.cpython-313.pyc
│  │     │  │     ├─ sessions.cpython-313.pyc
│  │     │  │     ├─ trustedhost.cpython-313.pyc
│  │     │  │     ├─ wsgi.cpython-313.pyc
│  │     │  │     └─ __init__.cpython-313.pyc
│  │     │  ├─ py.typed
│  │     │  ├─ requests.py
│  │     │  ├─ responses.py
│  │     │  ├─ routing.py
│  │     │  ├─ schemas.py
│  │     │  ├─ staticfiles.py
│  │     │  ├─ status.py
│  │     │  ├─ templating.py
│  │     │  ├─ testclient.py
│  │     │  ├─ types.py
│  │     │  ├─ websockets.py
│  │     │  ├─ _compat.py
│  │     │  ├─ _exception_handler.py
│  │     │  ├─ _utils.py
│  │     │  ├─ __init__.py
│  │     │  └─ __pycache__
│  │     │     ├─ applications.cpython-313.pyc
│  │     │     ├─ authentication.cpython-313.pyc
│  │     │     ├─ background.cpython-313.pyc
│  │     │     ├─ concurrency.cpython-313.pyc
│  │     │     ├─ config.cpython-313.pyc
│  │     │     ├─ convertors.cpython-313.pyc
│  │     │     ├─ datastructures.cpython-313.pyc
│  │     │     ├─ endpoints.cpython-313.pyc
│  │     │     ├─ exceptions.cpython-313.pyc
│  │     │     ├─ formparsers.cpython-313.pyc
│  │     │     ├─ requests.cpython-313.pyc
│  │     │     ├─ responses.cpython-313.pyc
│  │     │     ├─ routing.cpython-313.pyc
│  │     │     ├─ schemas.cpython-313.pyc
│  │     │     ├─ staticfiles.cpython-313.pyc
│  │     │     ├─ status.cpython-313.pyc
│  │     │     ├─ templating.cpython-313.pyc
│  │     │     ├─ testclient.cpython-313.pyc
│  │     │     ├─ types.cpython-313.pyc
│  │     │     ├─ websockets.cpython-313.pyc
│  │     │     ├─ _compat.cpython-313.pyc
│  │     │     ├─ _exception_handler.cpython-313.pyc
│  │     │     ├─ _utils.cpython-313.pyc
│  │     │     └─ __init__.cpython-313.pyc
│  │     ├─ starlette-0.41.3.dist-info
│  │     │  ├─ INSTALLER
│  │     │  ├─ licenses
│  │     │  │  └─ LICENSE.md
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  └─ WHEEL
│  │     ├─ tenacity
│  │     │  ├─ after.py
│  │     │  ├─ asyncio
│  │     │  │  ├─ retry.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ retry.cpython-313.pyc
│  │     │  │     └─ __init__.cpython-313.pyc
│  │     │  ├─ before.py
│  │     │  ├─ before_sleep.py
│  │     │  ├─ nap.py
│  │     │  ├─ py.typed
│  │     │  ├─ retry.py
│  │     │  ├─ stop.py
│  │     │  ├─ tornadoweb.py
│  │     │  ├─ wait.py
│  │     │  ├─ _utils.py
│  │     │  ├─ __init__.py
│  │     │  └─ __pycache__
│  │     │     ├─ after.cpython-313.pyc
│  │     │     ├─ before.cpython-313.pyc
│  │     │     ├─ before_sleep.cpython-313.pyc
│  │     │     ├─ nap.cpython-313.pyc
│  │     │     ├─ retry.cpython-313.pyc
│  │     │     ├─ stop.cpython-313.pyc
│  │     │     ├─ tornadoweb.cpython-313.pyc
│  │     │     ├─ wait.cpython-313.pyc
│  │     │     ├─ _utils.cpython-313.pyc
│  │     │     └─ __init__.cpython-313.pyc
│  │     ├─ tenacity-9.1.4.dist-info
│  │     │  ├─ INSTALLER
│  │     │  ├─ licenses
│  │     │  │  └─ LICENSE
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  ├─ top_level.txt
│  │     │  └─ WHEEL
│  │     ├─ typing_extensions-4.15.0.dist-info
│  │     │  ├─ INSTALLER
│  │     │  ├─ licenses
│  │     │  │  └─ LICENSE
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  └─ WHEEL
│  │     ├─ typing_extensions.py
│  │     ├─ typing_inspection
│  │     │  ├─ introspection.py
│  │     │  ├─ py.typed
│  │     │  ├─ typing_objects.py
│  │     │  ├─ typing_objects.pyi
│  │     │  ├─ __init__.py
│  │     │  └─ __pycache__
│  │     │     ├─ introspection.cpython-313.pyc
│  │     │     ├─ typing_objects.cpython-313.pyc
│  │     │     └─ __init__.cpython-313.pyc
│  │     ├─ typing_inspection-0.4.2.dist-info
│  │     │  ├─ INSTALLER
│  │     │  ├─ licenses
│  │     │  │  └─ LICENSE
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  └─ WHEEL
│  │     ├─ urllib3
│  │     │  ├─ connection.py
│  │     │  ├─ connectionpool.py
│  │     │  ├─ contrib
│  │     │  │  ├─ emscripten
│  │     │  │  │  ├─ connection.py
│  │     │  │  │  ├─ emscripten_fetch_worker.js
│  │     │  │  │  ├─ fetch.py
│  │     │  │  │  ├─ request.py
│  │     │  │  │  ├─ response.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ connection.cpython-313.pyc
│  │     │  │  │     ├─ fetch.cpython-313.pyc
│  │     │  │  │     ├─ request.cpython-313.pyc
│  │     │  │  │     ├─ response.cpython-313.pyc
│  │     │  │  │     └─ __init__.cpython-313.pyc
│  │     │  │  ├─ pyopenssl.py
│  │     │  │  ├─ socks.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ pyopenssl.cpython-313.pyc
│  │     │  │     ├─ socks.cpython-313.pyc
│  │     │  │     └─ __init__.cpython-313.pyc
│  │     │  ├─ exceptions.py
│  │     │  ├─ fields.py
│  │     │  ├─ filepost.py
│  │     │  ├─ http2
│  │     │  │  ├─ connection.py
│  │     │  │  ├─ probe.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ connection.cpython-313.pyc
│  │     │  │     ├─ probe.cpython-313.pyc
│  │     │  │     └─ __init__.cpython-313.pyc
│  │     │  ├─ poolmanager.py
│  │     │  ├─ py.typed
│  │     │  ├─ response.py
│  │     │  ├─ util
│  │     │  │  ├─ connection.py
│  │     │  │  ├─ proxy.py
│  │     │  │  ├─ request.py
│  │     │  │  ├─ response.py
│  │     │  │  ├─ retry.py
│  │     │  │  ├─ ssltransport.py
│  │     │  │  ├─ ssl_.py
│  │     │  │  ├─ ssl_match_hostname.py
│  │     │  │  ├─ timeout.py
│  │     │  │  ├─ url.py
│  │     │  │  ├─ util.py
│  │     │  │  ├─ wait.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ connection.cpython-313.pyc
│  │     │  │     ├─ proxy.cpython-313.pyc
│  │     │  │     ├─ request.cpython-313.pyc
│  │     │  │     ├─ response.cpython-313.pyc
│  │     │  │     ├─ retry.cpython-313.pyc
│  │     │  │     ├─ ssltransport.cpython-313.pyc
│  │     │  │     ├─ ssl_.cpython-313.pyc
│  │     │  │     ├─ ssl_match_hostname.cpython-313.pyc
│  │     │  │     ├─ timeout.cpython-313.pyc
│  │     │  │     ├─ url.cpython-313.pyc
│  │     │  │     ├─ util.cpython-313.pyc
│  │     │  │     ├─ wait.cpython-313.pyc
│  │     │  │     └─ __init__.cpython-313.pyc
│  │     │  ├─ _base_connection.py
│  │     │  ├─ _collections.py
│  │     │  ├─ _request_methods.py
│  │     │  ├─ _version.py
│  │     │  ├─ __init__.py
│  │     │  └─ __pycache__
│  │     │     ├─ connection.cpython-313.pyc
│  │     │     ├─ connectionpool.cpython-313.pyc
│  │     │     ├─ exceptions.cpython-313.pyc
│  │     │     ├─ fields.cpython-313.pyc
│  │     │     ├─ filepost.cpython-313.pyc
│  │     │     ├─ poolmanager.cpython-313.pyc
│  │     │     ├─ response.cpython-313.pyc
│  │     │     ├─ _base_connection.cpython-313.pyc
│  │     │     ├─ _collections.cpython-313.pyc
│  │     │     ├─ _request_methods.cpython-313.pyc
│  │     │     ├─ _version.cpython-313.pyc
│  │     │     └─ __init__.cpython-313.pyc
│  │     ├─ urllib3-2.6.3.dist-info
│  │     │  ├─ INSTALLER
│  │     │  ├─ licenses
│  │     │  │  └─ LICENSE.txt
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  └─ WHEEL
│  │     ├─ uvicorn
│  │     │  ├─ config.py
│  │     │  ├─ importer.py
│  │     │  ├─ lifespan
│  │     │  │  ├─ off.py
│  │     │  │  ├─ on.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ off.cpython-313.pyc
│  │     │  │     ├─ on.cpython-313.pyc
│  │     │  │     └─ __init__.cpython-313.pyc
│  │     │  ├─ logging.py
│  │     │  ├─ loops
│  │     │  │  ├─ asyncio.py
│  │     │  │  ├─ auto.py
│  │     │  │  ├─ uvloop.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ asyncio.cpython-313.pyc
│  │     │  │     ├─ auto.cpython-313.pyc
│  │     │  │     ├─ uvloop.cpython-313.pyc
│  │     │  │     └─ __init__.cpython-313.pyc
│  │     │  ├─ main.py
│  │     │  ├─ middleware
│  │     │  │  ├─ asgi2.py
│  │     │  │  ├─ message_logger.py
│  │     │  │  ├─ proxy_headers.py
│  │     │  │  ├─ wsgi.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ asgi2.cpython-313.pyc
│  │     │  │     ├─ message_logger.cpython-313.pyc
│  │     │  │     ├─ proxy_headers.cpython-313.pyc
│  │     │  │     ├─ wsgi.cpython-313.pyc
│  │     │  │     └─ __init__.cpython-313.pyc
│  │     │  ├─ protocols
│  │     │  │  ├─ http
│  │     │  │  │  ├─ auto.py
│  │     │  │  │  ├─ flow_control.py
│  │     │  │  │  ├─ h11_impl.py
│  │     │  │  │  ├─ httptools_impl.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ auto.cpython-313.pyc
│  │     │  │  │     ├─ flow_control.cpython-313.pyc
│  │     │  │  │     ├─ h11_impl.cpython-313.pyc
│  │     │  │  │     ├─ httptools_impl.cpython-313.pyc
│  │     │  │  │     └─ __init__.cpython-313.pyc
│  │     │  │  ├─ utils.py
│  │     │  │  ├─ websockets
│  │     │  │  │  ├─ auto.py
│  │     │  │  │  ├─ websockets_impl.py
│  │     │  │  │  ├─ wsproto_impl.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ auto.cpython-313.pyc
│  │     │  │  │     ├─ websockets_impl.cpython-313.pyc
│  │     │  │  │     ├─ wsproto_impl.cpython-313.pyc
│  │     │  │  │     └─ __init__.cpython-313.pyc
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ utils.cpython-313.pyc
│  │     │  │     └─ __init__.cpython-313.pyc
│  │     │  ├─ py.typed
│  │     │  ├─ server.py
│  │     │  ├─ supervisors
│  │     │  │  ├─ basereload.py
│  │     │  │  ├─ multiprocess.py
│  │     │  │  ├─ statreload.py
│  │     │  │  ├─ watchfilesreload.py
│  │     │  │  ├─ watchgodreload.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ basereload.cpython-313.pyc
│  │     │  │     ├─ multiprocess.cpython-313.pyc
│  │     │  │     ├─ statreload.cpython-313.pyc
│  │     │  │     ├─ watchfilesreload.cpython-313.pyc
│  │     │  │     ├─ watchgodreload.cpython-313.pyc
│  │     │  │     └─ __init__.cpython-313.pyc
│  │     │  ├─ workers.py
│  │     │  ├─ _subprocess.py
│  │     │  ├─ _types.py
│  │     │  ├─ __init__.py
│  │     │  ├─ __main__.py
│  │     │  └─ __pycache__
│  │     │     ├─ config.cpython-313.pyc
│  │     │     ├─ importer.cpython-313.pyc
│  │     │     ├─ logging.cpython-313.pyc
│  │     │     ├─ main.cpython-313.pyc
│  │     │     ├─ server.cpython-313.pyc
│  │     │     ├─ workers.cpython-313.pyc
│  │     │     ├─ _subprocess.cpython-313.pyc
│  │     │     ├─ _types.cpython-313.pyc
│  │     │     ├─ __init__.cpython-313.pyc
│  │     │     └─ __main__.cpython-313.pyc
│  │     ├─ uvicorn-0.32.1.dist-info
│  │     │  ├─ entry_points.txt
│  │     │  ├─ INSTALLER
│  │     │  ├─ licenses
│  │     │  │  └─ LICENSE.md
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  ├─ REQUESTED
│  │     │  └─ WHEEL
│  │     ├─ websockets
│  │     │  ├─ asyncio
│  │     │  │  ├─ async_timeout.py
│  │     │  │  ├─ client.py
│  │     │  │  ├─ compatibility.py
│  │     │  │  ├─ connection.py
│  │     │  │  ├─ messages.py
│  │     │  │  ├─ router.py
│  │     │  │  ├─ server.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ async_timeout.cpython-313.pyc
│  │     │  │     ├─ client.cpython-313.pyc
│  │     │  │     ├─ compatibility.cpython-313.pyc
│  │     │  │     ├─ connection.cpython-313.pyc
│  │     │  │     ├─ messages.cpython-313.pyc
│  │     │  │     ├─ router.cpython-313.pyc
│  │     │  │     ├─ server.cpython-313.pyc
│  │     │  │     └─ __init__.cpython-313.pyc
│  │     │  ├─ auth.py
│  │     │  ├─ cli.py
│  │     │  ├─ client.py
│  │     │  ├─ connection.py
│  │     │  ├─ datastructures.py
│  │     │  ├─ exceptions.py
│  │     │  ├─ extensions
│  │     │  │  ├─ base.py
│  │     │  │  ├─ permessage_deflate.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ base.cpython-313.pyc
│  │     │  │     ├─ permessage_deflate.cpython-313.pyc
│  │     │  │     └─ __init__.cpython-313.pyc
│  │     │  ├─ frames.py
│  │     │  ├─ headers.py
│  │     │  ├─ http.py
│  │     │  ├─ http11.py
│  │     │  ├─ imports.py
│  │     │  ├─ legacy
│  │     │  │  ├─ auth.py
│  │     │  │  ├─ client.py
│  │     │  │  ├─ exceptions.py
│  │     │  │  ├─ framing.py
│  │     │  │  ├─ handshake.py
│  │     │  │  ├─ http.py
│  │     │  │  ├─ protocol.py
│  │     │  │  ├─ server.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ auth.cpython-313.pyc
│  │     │  │     ├─ client.cpython-313.pyc
│  │     │  │     ├─ exceptions.cpython-313.pyc
│  │     │  │     ├─ framing.cpython-313.pyc
│  │     │  │     ├─ handshake.cpython-313.pyc
│  │     │  │     ├─ http.cpython-313.pyc
│  │     │  │     ├─ protocol.cpython-313.pyc
│  │     │  │     ├─ server.cpython-313.pyc
│  │     │  │     └─ __init__.cpython-313.pyc
│  │     │  ├─ protocol.py
│  │     │  ├─ py.typed
│  │     │  ├─ server.py
│  │     │  ├─ speedups.c
│  │     │  ├─ speedups.cp313-win_amd64.pyd
│  │     │  ├─ speedups.pyi
│  │     │  ├─ streams.py
│  │     │  ├─ sync
│  │     │  │  ├─ client.py
│  │     │  │  ├─ connection.py
│  │     │  │  ├─ messages.py
│  │     │  │  ├─ router.py
│  │     │  │  ├─ server.py
│  │     │  │  ├─ utils.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ client.cpython-313.pyc
│  │     │  │     ├─ connection.cpython-313.pyc
│  │     │  │     ├─ messages.cpython-313.pyc
│  │     │  │     ├─ router.cpython-313.pyc
│  │     │  │     ├─ server.cpython-313.pyc
│  │     │  │     ├─ utils.cpython-313.pyc
│  │     │  │     └─ __init__.cpython-313.pyc
│  │     │  ├─ typing.py
│  │     │  ├─ uri.py
│  │     │  ├─ utils.py
│  │     │  ├─ version.py
│  │     │  ├─ __init__.py
│  │     │  ├─ __main__.py
│  │     │  └─ __pycache__
│  │     │     ├─ auth.cpython-313.pyc
│  │     │     ├─ cli.cpython-313.pyc
│  │     │     ├─ client.cpython-313.pyc
│  │     │     ├─ connection.cpython-313.pyc
│  │     │     ├─ datastructures.cpython-313.pyc
│  │     │     ├─ exceptions.cpython-313.pyc
│  │     │     ├─ frames.cpython-313.pyc
│  │     │     ├─ headers.cpython-313.pyc
│  │     │     ├─ http.cpython-313.pyc
│  │     │     ├─ http11.cpython-313.pyc
│  │     │     ├─ imports.cpython-313.pyc
│  │     │     ├─ protocol.cpython-313.pyc
│  │     │     ├─ server.cpython-313.pyc
│  │     │     ├─ streams.cpython-313.pyc
│  │     │     ├─ typing.cpython-313.pyc
│  │     │     ├─ uri.cpython-313.pyc
│  │     │     ├─ utils.cpython-313.pyc
│  │     │     ├─ version.cpython-313.pyc
│  │     │     ├─ __init__.cpython-313.pyc
│  │     │     └─ __main__.cpython-313.pyc
│  │     ├─ websockets-15.0.1.dist-info
│  │     │  ├─ entry_points.txt
│  │     │  ├─ INSTALLER
│  │     │  ├─ LICENSE
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  ├─ top_level.txt
│  │     │  └─ WHEEL
│  │     ├─ _cffi_backend.cp313-win_amd64.pyd
│  │     ├─ _sounddevice.py
│  │     ├─ _sounddevice_data
│  │     │  ├─ portaudio-binaries
│  │     │  │  ├─ libportaudio64bit-asio.dll
│  │     │  │  ├─ libportaudio64bit.dll
│  │     │  │  └─ README.md
│  │     │  ├─ __init__.py
│  │     │  └─ __pycache__
│  │     │     └─ __init__.cpython-313.pyc
│  │     ├─ __pycache__
│  │     │  ├─ pylab.cpython-313.pyc
│  │     │  ├─ six.cpython-313.pyc
│  │     │  ├─ sounddevice.cpython-313.pyc
│  │     │  ├─ typing_extensions.cpython-313.pyc
│  │     │  └─ _sounddevice.cpython-313.pyc
│  │     └─ ~ydantic_core
│  │        └─ _pydantic_core.cp313-win_amd64.pyd
│  ├─ pyvenv.cfg
│  ├─ Scripts
│  │  ├─ activate
│  │  ├─ activate.bat
│  │  ├─ activate.fish
│  │  ├─ Activate.ps1
│  │  ├─ deactivate.bat
│  │  ├─ distro.exe
│  │  ├─ dotenv.exe
│  │  ├─ f2py.exe
│  │  ├─ fastapi.exe
│  │  ├─ fonttools.exe
│  │  ├─ futurize.exe
│  │  ├─ httpx.exe
│  │  ├─ normalizer.exe
│  │  ├─ numpy-config.exe
│  │  ├─ pasteurize.exe
│  │  ├─ pip.exe
│  │  ├─ pip3.13.exe
│  │  ├─ pip3.exe
│  │  ├─ pyftmerge.exe
│  │  ├─ pyftsubset.exe
│  │  ├─ python.exe
│  │  ├─ pythonw.exe
│  │  ├─ ttx.exe
│  │  ├─ uvicorn.exe
│  │  └─ websockets.exe
│  └─ share
│     └─ man
│        └─ man1
│           └─ ttx.1
└─ __pycache__
   └─ main.cpython-313.pyc

```