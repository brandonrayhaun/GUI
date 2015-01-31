import WebSocket as W
import Graphics.Input (..)
import Graphics.Element (..)
import Signal as S
import Text (..)

keys : S.Channel String
keys = S.channel "0"

symmetry : S.Signal String
symmetry = S.subscribe keys

buttons : Element 
buttons = flow down [button (S.send keys "0") "Send Hello", button (S.send keys "1") "Send Goodbye"]

main = S.map2 (\s1 s2 -> flow down [plainText s1, plainText s2, buttons]) symmetry <| W.connect """ws://localhost:8275/""" symmetry