import sys
from platforms_android import firebase, univesal_analytics, gtm
from interface import show_error_message, show_program_finished
from tools import ui_data, utils


if __name__ == "__main__":
    operating_system = ui_data.OperatingSystem()
    instructions = ui_data.Instructions(operating_system.ANDROID)

    args, platform = utils.get_arguments_and_option(instructions)
    platforms = ui_data.Platform()

    no_argument: bool = True if (len(sys.argv) == 1) else False

    try:
        match (platform):
            case platforms.GA4:
                firebase.no_arguments() if (no_argument) else firebase.with_arguments(args)
            case platforms.GAU:
                univesal_analytics.no_arguments() if (no_argument) else univesal_analytics.with_arguments(args)
            # options without filter
            case platforms.GTM:
                gtm.main()
            case ui_data.Option.QUIT.value:
                show_program_finished()
                sys.exit(0)
            case _:
                show_error_message(ui_data.Error.CHOICE_OPTION.value)
    except Exception as error:
        show_error_message(str(error))
        sys.exit(1)
