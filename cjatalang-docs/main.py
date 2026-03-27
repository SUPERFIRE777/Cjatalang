def define_env(env):
    """MkDocsの環境にマクロを注入するエントリーポイント"""
    
    @env.macro
    def r(text, ruby):
        """ルビ(ふりがな)タグを生成する短いマクロ"""
        return f'<ruby><span class="ruby-base">{text}</span><rt>{ruby}</rt></ruby>'

def main():
    print("Hello from document!")


if __name__ == "__main__":
    main()
