`root` is not one of the three class of permissions, they are : owner, group, other.

`root` overrides the permissions even if the permissions are `0000`. It does it through the `CAP_DAC_OVERRIDE` capability.

So "I want root to be able to read this" is never a question to ask when you choose a mode. What you are actually choosing is the right of the **owner**, and the owner is whoever created the file.

A mode is a policy for everybody except root. If you need to restrict root itself, permissions are the wrong tool.

See [[File ownership]]
