from collections.abc import Mapping, MutableMapping, Sequence
from typing import Any, Optional

import markdown_it
from markdown_it.token import Token
from markdown_it.utils import OptionsDict

_md_escape_table = {
    ord('*'): '\\*',
    ord('<'): '\\<',
    ord('['): '\\[',
    ord('`'): '\\`',
    ord('.'): '\\.',
    ord('#'): '\\#',
    ord('&'): '\\&',
    ord('\\'): '\\\\',
}
def md_escape(s: str) -> str:
    return s.translate(_md_escape_table)

class Renderer(markdown_it.renderer.RendererProtocol):
    def __init__(self, manpage_urls: Mapping[str, str], parser: Optional[markdown_it.MarkdownIt] = None):
        self._manpage_urls = manpage_urls
        self.rules = {
            'text': self.text,
            'paragraph_open': self.paragraph_open,
            'paragraph_close': self.paragraph_close,
            'hardbreak': self.hardbreak,
            'softbreak': self.softbreak,
            'code_inline': self.code_inline,
            'code_block': self.code_block,
            'link_open': self.link_open,
            'link_close': self.link_close,
            'list_item_open': self.list_item_open,
            'list_item_close': self.list_item_close,
            'bullet_list_open': self.bullet_list_open,
            'bullet_list_close': self.bullet_list_close,
            'em_open': self.em_open,
            'em_close': self.em_close,
            'strong_open': self.strong_open,
            'strong_close': self.strong_close,
            'fence': self.fence,
            'blockquote_open': self.blockquote_open,
            'blockquote_close': self.blockquote_close,
            'dl_open': self.dl_open,
            'dl_close': self.dl_close,
            'dt_open': self.dt_open,
            'dt_close': self.dt_close,
            'dd_open': self.dd_open,
            'dd_close': self.dd_close,
            'myst_role': self.myst_role,
            "container_{.note}_open": self.note_open,
            "container_{.note}_close": self.note_close,
            "container_{.important}_open": self.important_open,
            "container_{.important}_close": self.important_close,
            "container_{.warning}_open": self.warning_open,
            "container_{.warning}_close": self.warning_close,
        }
    def render(self, tokens: Sequence[Token], options: OptionsDict,
               env: MutableMapping[str, Any]) -> str:
        def do_one(i: int, token: Token) -> str:
            if token.type == "inline":
                assert token.children is not None
                return self.renderInline(token.children, options, env)
            elif token.type in self.rules:
                return self.rules[token.type](tokens[i], tokens, i, options, env)
            else:
                raise NotImplementedError("md token not supported yet", token)
        return "".join(map(lambda arg: do_one(*arg), enumerate(tokens)))
    def renderInline(self, tokens: Sequence[Token], options: OptionsDict,
                     env: MutableMapping[str, Any]) -> str:
        def do_one(i: int, token: Token) -> str:
            if token.type in self.rules:
                return self.rules[token.type](tokens[i], tokens, i, options, env)
            else:
                raise NotImplementedError("md token not supported yet", token)
        return "".join(map(lambda arg: do_one(*arg), enumerate(tokens)))

    def text(self, token: Token, tokens: Sequence[Token], i: int, options: OptionsDict,
             env: MutableMapping[str, Any]) -> str:
        raise RuntimeError("md token not supported", token)
    def paragraph_open(self, token: Token, tokens: Sequence[Token], i: int, options: OptionsDict,
                       env: MutableMapping[str, Any]) -> str:
        raise RuntimeError("md token not supported", token)
    def paragraph_close(self, token: Token, tokens: Sequence[Token], i: int, options: OptionsDict,
                        env: MutableMapping[str, Any]) -> str:
        raise RuntimeError("md token not supported", token)
    def hardbreak(self, token: Token, tokens: Sequence[Token], i: int, options: OptionsDict,
                  env: MutableMapping[str, Any]) -> str:
        raise RuntimeError("md token not supported", token)
    def softbreak(self, token: Token, tokens: Sequence[Token], i: int, options: OptionsDict,
                  env: MutableMapping[str, Any]) -> str:
        raise RuntimeError("md token not supported", token)
    def code_inline(self, token: Token, tokens: Sequence[Token], i: int, options: OptionsDict,
                    env: MutableMapping[str, Any]) -> str:
        raise RuntimeError("md token not supported", token)
    def code_block(self, token: Token, tokens: Sequence[Token], i: int, options: OptionsDict,
                   env: MutableMapping[str, Any]) -> str:
        raise RuntimeError("md token not supported", token)
    def link_open(self, token: Token, tokens: Sequence[Token], i: int, options: OptionsDict,
                  env: MutableMapping[str, Any]) -> str:
        raise RuntimeError("md token not supported", token)
    def link_close(self, token: Token, tokens: Sequence[Token], i: int, options: OptionsDict,
                   env: MutableMapping[str, Any]) -> str:
        raise RuntimeError("md token not supported", token)
    def list_item_open(self, token: Token, tokens: Sequence[Token], i: int, options: OptionsDict,
                       env: MutableMapping[str, Any]) -> str:
        raise RuntimeError("md token not supported", token)
    def list_item_close(self, token: Token, tokens: Sequence[Token], i: int, options: OptionsDict,
                        env: MutableMapping[str, Any]) -> str:
        raise RuntimeError("md token not supported", token)
    def bullet_list_open(self, token: Token, tokens: Sequence[Token], i: int, options: OptionsDict,
                         env: MutableMapping[str, Any]) -> str:
        raise RuntimeError("md token not supported", token)
    def bullet_list_close(self, token: Token, tokens: Sequence[Token], i: int, options: OptionsDict,
                          env: MutableMapping[str, Any]) -> str:
        raise RuntimeError("md token not supported", token)
    def em_open(self, token: Token, tokens: Sequence[Token], i: int, options: OptionsDict,
                env: MutableMapping[str, Any]) -> str:
        raise RuntimeError("md token not supported", token)
    def em_close(self, token: Token, tokens: Sequence[Token], i: int, options: OptionsDict,
                 env: MutableMapping[str, Any]) -> str:
        raise RuntimeError("md token not supported", token)
    def strong_open(self, token: Token, tokens: Sequence[Token], i: int, options: OptionsDict,
                    env: MutableMapping[str, Any]) -> str:
        raise RuntimeError("md token not supported", token)
    def strong_close(self, token: Token, tokens: Sequence[Token], i: int, options: OptionsDict,
                     env: MutableMapping[str, Any]) -> str:
        raise RuntimeError("md token not supported", token)
    def fence(self, token: Token, tokens: Sequence[Token], i: int, options: OptionsDict,
              env: MutableMapping[str, Any]) -> str:
        raise RuntimeError("md token not supported", token)
    def blockquote_open(self, token: Token, tokens: Sequence[Token], i: int, options: OptionsDict,
                        env: MutableMapping[str, Any]) -> str:
        raise RuntimeError("md token not supported", token)
    def blockquote_close(self, token: Token, tokens: Sequence[Token], i: int, options: OptionsDict,
                         env: MutableMapping[str, Any]) -> str:
        raise RuntimeError("md token not supported", token)
    def note_open(self, token: Token, tokens: Sequence[Token], i: int, options: OptionsDict,
                  env: MutableMapping[str, Any]) -> str:
        raise RuntimeError("md token not supported", token)
    def note_close(self, token: Token, tokens: Sequence[Token], i: int, options: OptionsDict,
                   env: MutableMapping[str, Any]) -> str:
        raise RuntimeError("md token not supported", token)
    def important_open(self, token: Token, tokens: Sequence[Token], i: int, options: OptionsDict,
                       env: MutableMapping[str, Any]) -> str:
        raise RuntimeError("md token not supported", token)
    def important_close(self, token: Token, tokens: Sequence[Token], i: int, options: OptionsDict,
                        env: MutableMapping[str, Any]) -> str:
        raise RuntimeError("md token not supported", token)
    def warning_open(self, token: Token, tokens: Sequence[Token], i: int, options: OptionsDict,
                     env: MutableMapping[str, Any]) -> str:
        raise RuntimeError("md token not supported", token)
    def warning_close(self, token: Token, tokens: Sequence[Token], i: int, options: OptionsDict,
                      env: MutableMapping[str, Any]) -> str:
        raise RuntimeError("md token not supported", token)
    def dl_open(self, token: Token, tokens: Sequence[Token], i: int, options: OptionsDict,
                env: MutableMapping[str, Any]) -> str:
        raise RuntimeError("md token not supported", token)
    def dl_close(self, token: Token, tokens: Sequence[Token], i: int, options: OptionsDict,
                 env: MutableMapping[str, Any]) -> str:
        raise RuntimeError("md token not supported", token)
    def dt_open(self, token: Token, tokens: Sequence[Token], i: int, options: OptionsDict,
                env: MutableMapping[str, Any]) -> str:
        raise RuntimeError("md token not supported", token)
    def dt_close(self, token: Token, tokens: Sequence[Token], i: int, options: OptionsDict,
                 env: MutableMapping[str, Any]) -> str:
        raise RuntimeError("md token not supported", token)
    def dd_open(self, token: Token, tokens: Sequence[Token], i: int, options: OptionsDict,
                env: MutableMapping[str, Any]) -> str:
        raise RuntimeError("md token not supported", token)
    def dd_close(self, token: Token, tokens: Sequence[Token], i: int, options: OptionsDict,
                 env: MutableMapping[str, Any]) -> str:
        raise RuntimeError("md token not supported", token)
    def myst_role(self, token: Token, tokens: Sequence[Token], i: int, options: OptionsDict,
                  env: MutableMapping[str, Any]) -> str:
        raise RuntimeError("md token not supported", token)
