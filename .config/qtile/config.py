from libqtile.config import Key, Screen, Group, Drag, Click
from libqtile.command import lazy
from libqtile import layout, bar, widget

mod = "mod4"

keys = [
    # Switch between windows in current stack pane
    Key(
        [mod], "k",
        lazy.layout.up(),
    ),
    Key(
        [mod], "j",
        lazy.layout.down(),
    ),
    Key(
        [mod], "h",
        lazy.layout.previous(),  # stack
        lazy.layout.left(),      # monad-tall
    ),
    Key(
        [mod], "l",
        lazy.layout.next(),      # stack
        lazy.layout.right(),     # monad-tall
    ),

    # Switch window focus to other pane(s) of stack
    Key(
        [mod], "space",
        lazy.layout.next()
    ),

    # Swap panes of split stack
    Key(
        [mod, "shift"], "space",
        lazy.layout.rotate(),
        lazy.layout.flip(),       # monad-tall
    ),
    # Move windows up or down in current stack
    Key(
        [mod, "shift"], "k",
        lazy.layout.shuffle_up(),       # Stack, xmonad-tall
    ),
    Key(
        [mod, "shift"], "j",
        lazy.layout.shuffle_down(),       # Stack, xmonad-tall
    ),

    Key(
        [mod, "control"], "k",
        lazy.layout.grow(),             # xmonad-tall
    ),
    Key(
        [mod, "control"], "j",
        lazy.layout.shrink(),               # xmonad-tall
    ),
    Key([mod, "control"], "r", lazy.restart()),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"], "Return",
        lazy.layout.toggle_split()
    ),
    Key([mod], "Return", lazy.spawn("xterm")),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.nextlayout()),
    Key([mod, "control"], "w", lazy.window.kill()),

    Key([mod, "control"], "r", lazy.restart()),
    Key([mod, "control"], "q", lazy.shutdown()),
    Key([mod], "r", lazy.spawncmd()),
    Key([mod, "control"], "l", lazy.spawn("xscreensaver-command --lock")),
]

groups = [Group(i) for i in "asdfuiop"]

for i in groups:
    # mod1 + letter of group = switch to group
    keys.append(
        Key([mod], i.name, lazy.group[i.name].toscreen())
    )

    # mod1 + shift + letter of group = switch to & move focused window to group
    keys.append(
        Key([mod, "shift"], i.name, lazy.window.togroup(i.name))
    )

layouts = [
    layout.Max(),
    layout.Stack(num_stacks=2),
    layout.MonadTall(),
]

widget_defaults = dict(
    font='Arial',
    fontsize=16,
    padding=3,
)

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.GroupBox(urgent_alert_method='text',),
                widget.Prompt(),
                widget.WindowName(foreground="a0a0a0",),
                widget.Notify(),
                widget.Systray(),
                widget.Volume(foreground="70ff70"),
                widget.Battery(
                    energy_now_file='charge_now',
                    energy_full_file='charge_full',
                    power_now_file='current_now',
                    update_delay=5,
                    foreground="7070ff",),
                widget.Systray(),
                widget.Clock(
                    foreground="a0a0a0",
                    format='%Y-%m-%d %a %I:%M %p'),
            ],
            22,    # our bar is (xx)px high
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []
main = None
follow_mouse_focus = False
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating()
auto_fullscreen = True
wmname = "qtile"
