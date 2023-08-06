##  Thư viện kiểm tra extension file.

### Cài đặt:

```bash
 $ pip3 install validate-extension-file
 ```

### Sử dụng
```python
from truestrive.libs.filetypes.file import File
from truestrive.libs.filetypes.common import ExtensionImage

File.check_filetype_by_file_extensions(
    file_binary=file, # Check filetype của định dạng file binary.Mặc định None
    file_path=file_path, # Check filetype của path file
    extensions=[ExtensionImage.PNG] # Danh sách extension cần check.
)

```

#### Lấy extensions support
- Extension Image:
```python
from truestrive.libs.filetypes.common import ExtensionImage
ExtensionImage.LIST_EXTENSION_SUPPORTED
```
- Extension Document:
```python
from truestrive.libs.filetypes.common import ExtensionDocument
ExtensionDocument.LIST_EXTENSION_SUPPORTED
```
- Extension Audio:
```python
from truestrive.libs.filetypes.common import ExtensionAudio
ExtensionAudio.LIST_EXTENSION_SUPPORTED
```

