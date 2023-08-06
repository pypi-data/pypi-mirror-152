<table>
  <tr>
    <th>ci</th>
    <td>
      <a>
        <img alt="Tests" src="https://img.shields.io/github/workflow/status/demberto/tlhelp32/test?label=tests"/>
      </a>
      <a>
        <img alt="Build" src="https://img.shields.io/github/workflow/status/demberto/tlhelp32/release"/>
      </a>
      <a href="https://tlhelp32.rtfd.io/en/latest">
        <img alt="Docs" src="https://readthedocs.org/projects/tlhelp32/badge/?version=latest"/>
      </a>
    </td>
  </tr>
  <tr>
    <th>pypi</th>
    <td>
      <a href="https://github.com/demberto/tlhelp32/releases">
        <img alt="Version" src="https://img.shields.io/pypi/v/tlhelp32"/>
      </a>
      <a href="https://github.com/demberto/tlhelp32/blob/master/LICENSE">
        <img alt="License" src="https://img.shields.io/pypi/l/tlhelp32"/>
      </a>
      <a href="https://pypi.org/project/tlhelp32/#history">
        <img alt="Python Versions" src="https://img.shields.io/pypi/pyversions/tlhelp32"/>
      </a>
    </td>
  </tr>
  <tr>
    <th>qa</th>
    <td>
      <a href="https://github.com/PyCQA/bandit">
        <img alt="security: bandit" src="https://img.shields.io/badge/security-bandit-yellow.svg"/>
      </a>
      <a href="https://github.com/psf/black">
        <img alt="code style: black" src="https://img.shields.io/badge/code%20style-black-black.svg"/>
      </a>
    </td>
  </tr>
</table>

# TlHelp32

> An idiomatic Python API for the Windows Tool Help library.

## Installation

Python 3.7+ is required.

```
pip install tlhelp32
```

[More](https://tlhelp32.rtfd.io/en/latest/installation) installation methods.

## Getting Started

Traversing a snapshot:

```python
import tlhelp32

with tlhelp32.Snapshot() as snapshot:
    print([repr(heap) for heap in snapshot.heaps])
    print([repr(module) for module in snapshot.modules])
    print([repr(process) for process in snapshot.processes])
    print([repr(thread) for thread in snapshot.threads])
```

[More](https://github.com/demberto/tlhelp32/tree/master/examples) examples.

## License

The code in this project is licensed under the **ISC license**.
