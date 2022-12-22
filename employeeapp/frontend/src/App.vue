<template>
    <div>
        <button @click="toggleShow">Show All Employees</button>
        <table v-if="this.show == true" class="table">
            <thead>
                <tr>
                    <th scope="col">Name</th>
                    <th scope="col">Email</th>
                    <th scope="col">Date Joined</th>
                    <th scope="col">Salary</th>
                    <th scope="col" colspan="2">Actions</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="employee in employees">
                    <td v-if ="this.editMode != employee.id">{{ employee.name }}</td>
                    <td v-if="this.editMode == employee.id">
                        <input id="editName" type="text" :value="employee.name"/>
                    </td>
                    <td v-if ="this.editMode != employee.id">{{ employee.email }}</td>
                    <td v-if="this.editMode == employee.id">
                        <input id="editEmail" type="email" :value="employee.email"/>
                    </td>
                    <td v-if ="this.editMode != employee.id">{{ employee.date_joined }}</td>
                    <td v-if="this.editMode == employee.id">
                        <input id="editDate" type="date" :value="employee.date_joined"/>
                    </td>
                    <td v-if ="this.editMode != employee.id">{{ employee.annual_salary }}</td>
                    <td v-if="this.editMode == employee.id">
                        <input id="editSalary" type="number" :value="Number(employee.annual_salary)"/>
                    </td>
                    <td>
                        <button v-if="this.editMode != employee.id" @click="toggleEdit(employee.id)" type="button" class="btn btn-success">Edit</button>
                        <button v-if="this.editMode == employee.id" @click="editEmployee(employee.id)" type="button" class="btn btn-success">Save</button>
                    </td>
                    <td>
                        <button @click="deleteEmployee(employee.id)" type="button" class="btn btn-danger">Delete</button>
                    </td>
                </tr>
            </tbody>
        </table>
    </div>
        <h3>Add Employee</h3>
        <form>
           <div class="form-group">
            <label for="name">Full Name</label>
            <input id="name" class="form-control" placeholder="John Smith">
           </div>
           <div class="form-group">
            <label for="email">Email address</label>
            <input id="email" class="form-control" type="email" placeholder="johnsmith@email.com">
           </div>
           <div class="form-group">
            <label for="date">Date Joined</label>
            <input id="date" class="form-control" type="date">
            </div>
            <div class="form-group">
            <label for="salary">Salary</label>
            <input id="salary" class="form-control" name="salary" type="number">
            </div>
            <button type="button" class="btn btn-primary" @click="addEmployee">Add</button>
        </form>
</template>

<script>

export default {
    data() { //objects can be accessed using this.field_name
        return {
            employees: [],
            show: false,
            editMode: null
        }
    },
    async created() {
            //Perform an Ajax request to fetch the list of employees
            let response = await fetch( "http://127.0.0.1:8000/api/employees/" );
            let data = await response.json();
            this.employees = data.employees;
            console.log(this.employees);
    },
    methods: {
        async toggleShow() {
            this.show = !this.show;
        },
        async addEmployee() {
            let name = document.getElementById("name");   
            let email = document.getElementById("email");
            let date_joined = document.getElementById("date");
            let annual_salary = document.getElementById("salary");
            let response = await fetch( "http://127.0.0.1:8000/api/employees/",
                {
                    method: 'POST',
                    body: JSON.stringify({
                        "name": name.value,
                        "email": email.value,
                        "date": date_joined.value,
                        "salary": annual_salary.value
                    })
                }
            ); //response stored in data
            let data = await response.json();
            this.employees.push( data );
        },
        async deleteEmployee( id ) {
            if(confirm("Are you sure want to delete this employee")) {
                let response = await fetch( "http://127.0.0.1:8000/api/employees/", {
                    method: "DELETE",
                    body: JSON.stringify({
                        "id": id
                    })
                });
                let res = await response.json();
                if( res.id == id ) {
                    this.employees = this.employees.filter( employee => employee.id != id );
                }
            }
        },
    async toggleEdit( id ) { //a way to show that the edit button has been clicked, and which employee's edit button was clicked
        this.editMode = id;
    },

    async editEmployee( id ) {
        this.editMode = null;
        let response = await fetch( "http://127.0.0.1:8000/api/employees/", {
            method: "PUT",
            body: JSON.stringify({
                "id": id,
                "name": document.getElementById( "editName" ).value,
                "email": document.getElementById( "editEmail" ).value,
                "date": document.getElementById( "editDate" ).value,
                "salary": document.getElementById( "editSalary" ).value,
            })
        });
        let res = await response.json();

        for ( let i = 0; i < this.employees.length; i++ ) { //could either update data state using this or clearing the employee array and filiing all of it again wit
            if( this.employees[i].id == id ) {
                this.employees[i].name = res.name;
                this.employees[i].email = res.email;
                this.employees[i].date_joined = res.date_joined;
                this.employees[i].annual_salary = res.annual_salary;
                break;
            }
        }
    }
   }

}
</script>

