package com.internship.tool.controller;

import com.internship.tool.entity.Compliance;
import com.internship.tool.service.ComplianceService;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/api/compliance")
public class ComplianceController {

    private final ComplianceService service;

    public ComplianceController(ComplianceService service) {
        this.service = service;
    }

    // Create
    @PostMapping
    public Compliance create(@RequestBody Compliance compliance) {
        return service.createCompliance(compliance);
    }

    // Get all
    @GetMapping
    public List<Compliance> getAll() {
        return service.getAllCompliance();
    }

    // Get by ID
    @GetMapping("/{id}")
    public Compliance getById(@PathVariable Long id) {
        return service.getComplianceById(id);
    }

    // Update
    @PutMapping("/{id}")
    public Compliance update(@PathVariable Long id, @RequestBody Compliance compliance) {
        return service.updateCompliance(id, compliance);
    }

    // Delete
    @DeleteMapping("/{id}")
    public String delete(@PathVariable Long id) {
        service.deleteCompliance(id);
        return "Deleted successfully";
    }
}