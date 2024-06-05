def posesion() -> list:
    return list (
            [
                #[{"LOWER":"posesión"}],#posesión                
                [{"LOWER":"semi"},{"LOWER":" "},{"LOWER":"cerrado"}], #semi cerrado
                [{"LOWER":"semi"},{"LOWER":"cerrado"}],#semicerrado
                [{"LOWER":"semicerrado"}],
                [{"LOWER":"semicerrada"}],
                [{"LOWER":"semi-cerrado"}],
                [{"LOWER":"semi-cerrada"}],
                [{"LOWER":"semiprivado"}],
                [{"LOWER":"semi-privado"}],
                [{"LOWER":"semi-privada"}]

            ]
    )
    
  