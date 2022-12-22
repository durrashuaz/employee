<template>
    <div class="border rounded bg-secondary shadow p-4">
        <div class="h1">
            {{ title }}
        </div>
        <div>
            Name: {{ name }}
            <input class="form-control" name="name" v-model="name">
            Email: {{ email }}
            <input class="form-control" name="email" v-model="email">
            Date Joined: {{ date_joined }}
            <input class="form-control" name="date" v-model="date_joined">
            Salary: {{ annual_salary }}
            <input class="form-control" name="salary" v-model="annual_salary">
            <button @click="addEmployee">Save</button>
        </div>
    </div>
</template>


<script>
    export default {
        props: ["title"],
        data() {
            return {
                name: "",
                email: "",
                date_joined: "",
                annual_salary: "",
            }
        },
        methods: {
            async addEmployee() {
                let response = await fetch( "http://localhost:8000/api/employees" );
                let data = await response.json();
                this.employees = data.employees;
                // form_data = new FormData();
                // form_data.append('name', this.name);
                // form_data.append('email', this.email);
                // form_data.append('date_joined', this.date_joined);
                // form_data.append('annual_salary', this.annual_salary);
                // let response = await fetch( "http://localhost:8000/api/employees",
                //     {
                //         method: 'POST',
                //         body: form_data
                //     }
                // );
                // return response.json();
            }
        }
    }
</script>