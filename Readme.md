# 🟩 lua5.4-subprocess

**Thanks to [@xlq](https://github.com/xlq/lua-subprocess) for commit ahead to port lua-subprocess in Lua 5.3**

Tested on Alpine Linux with `musl`

Get package on system

 ```css
  $: apk add --update musl musl-dev pkgconfig asciidoc lua5.4 lua5.4-dev lua5.4-libs
  ```
  
  - Set PATH for pkgconfig
  
  ```css
  $: export PKG_CONFIG_PATH=/usr/lib/pkgconfig
  ```
  
  - Set git clone lua5.4-subprocess
  
  ```css
  $: git clone https://github.com/huakim/lua-subprocess.git lua5.4-subprocess
  ```
  
  - Build it !
  
  ```css
  $: make
  ```
  
  - Copy to Lua libs /usr/lib/lua/5.4 !
  
  ```css
  $:  cp git/lua-subprocess/subprocess.so /usr/lib/lua/5.4
  ```
  Enjoy !
  
# 🟨 lua5.3-subprocess

Tested on Alpine Linux with `musl`

Get package on system

 ```css
  $: apk add --update musl musl-dev pkgconfig asciidoc lua5.3 lua5.3-dev lua5.3-libs
  ```
  
  - Set PATH for pkgconfig
  
  ```css
  $: export PKG_CONFIG_PATH=/usr/lib/pkgconfig
  ```
  
  - Set git clone lua5.4-subprocess
  
  ```css
  $: git clone https://github.com/huakim/lua-subprocess.git lua5.3-subprocess
  ```
  
  - Build it !
  
  ```css
  $: make
  ```
  
  - Copy to Lua libs /usr/lib/lua/5.3 !
  
  ```css
  $:  cp git/lua-subprocess/subprocess.so /usr/lib/lua/5.3
  ```
  Enjoy !

  <h2>🤝 Credits</h2>

**Joshua Phillips** - https://github.com/xlq/lua-subprocess - **To commit ahead** in past years, for fix all code to port Lua 5.3
<br>
**Ted Trask** - https://github.com/tdtrask/lua-subprocess - For alpine apk pkg
<br>
**Trinity Labs** - https://github.com/trinity-labs/lua5.4-subprocess - For README.md and for fix all code to port Lua 5.4
<br>
