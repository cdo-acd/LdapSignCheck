from typing import List, Tuple

from outflank_stage1.task.base_bof_task import BaseBOFTask
from outflank_stage1.task.enums import BOFArgumentEncoding


class LDAPSignCheckBOF(BaseBOFTask):
    def __init__(self):
        super().__init__("ldapsigncheck")

        self.parser.description = (
            "Check DC for relaying possibilities"
        )
        self.parser.epilog = "Synopsis: ldapsigncheck <DC>"

        self.parser.add_argument(
            "target",
            help=f"Target DC to check ldap signing for."
        )

    def _encode_arguments_bof(
        self, arguments: List[str]
    ) -> List[Tuple[BOFArgumentEncoding, str]]:
        parser_arguments = self.parser.parse_args(arguments)

        return [
            (BOFArgumentEncoding.WSTR, parser_arguments.target),
            (BOFArgumentEncoding.WSTR, "LDAP/" + parser_arguments.target)
        ]
