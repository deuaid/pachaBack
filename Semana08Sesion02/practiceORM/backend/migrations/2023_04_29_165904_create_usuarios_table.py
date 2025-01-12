from orator.migrations import Migration


class CreateUsuariosTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("usuarios") as table:
            table.increments("id")
            table.text("name")
            table.string("email").unique()
            table.string("password")
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("usuarios")
