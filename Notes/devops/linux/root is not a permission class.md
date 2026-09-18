`root` is not one of the three class of permissions, they are : owner, group, other.

`root` overrides the permissions even if the permissions are `0000`. It does it through the `CAP_DAC_OVERRIDE` capability.

So "I want root to be able to read this" is never a question to ask when you choose a mode. What you are actually choosing is the right of the **owner**, and the owner is whoever created the file.

A mode is a policy for everybody except root. If you need to restrict root itself, permissions are the wrong tool.

See [[File ownership]]

## Cards
Q: what are the three permission classes?
A: owner, group, other. `root` is not one of them.

Q: how does root bypass a `0000` mode?
A: through the `CAP_DAC_OVERRIDE` capability, which overrides the permission check entirely.

Q: "I want root to be able to read this" — why is that not a question when choosing a mode?
A: root already can, whatever you choose. What you are actually choosing is the right of the **owner**.

Q: if you need to restrict root itself, what do you use?
A: not permissions — they are a policy for everybody except root. You need a different tool.
